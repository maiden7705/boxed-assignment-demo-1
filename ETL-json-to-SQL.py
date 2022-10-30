import json, yaml, warnings
import pandas as pd
from sqlalchemy import create_engine
import utils as u


if __name__ == '__main__':
    events = []
    json_events = {}
    table_schema_json = {}
    docker_compose = {}

    #####################################
    ############# EXTRACT ###############
    #####################################
    with open('./Requirement/testEventData-1.txt', 'r') as f:
        events = [json.loads(line) for line in f]
    json_events["events"] = events

    ########################### TRANSFORM ##############################
    ############# FLATTENING AND NORMALIZATION OF TABLES ###############
    ####################################################################

    # This is de-normalized flat table which wont work as already discussed in notebook analysis
    # so we will try to normalize this into 2NF form as explain in notebook analysis
    events_denormalized_df = pd.json_normalize(events, max_level=4)

    # pandas's json_normalize() works like a charm on nested "dictionary of dictionaries"
    # but fails to implictly flatten value of a key if its "list of dictionaries".
    # so below code hack  (line #31 to #34) is needed
    for event in events:
        u.find_values_as_list_of_dicts(event)
    u.VALUE_AS_LIST = list(set(u.VALUE_AS_LIST))
    events_denormalized_df = u.flatten_list_of_dict_keys_to_seperate_columns(events_denormalized_df)

    # line #37 through #40 takes care of normalizing large flat table into seperate smaller tables dictionary
    sorted_col_list = events_denormalized_df.columns.tolist()
    sorted_col_list.sort()
    u.seperate_table_from_flattened_col_list(sorted_col_list)
    table_schema_json["events"] = u.TABLE_SCHEMA_DICT

    ############################ LOAD ##################################
    #################### LOAD INTO MYSQL DATABASE ######################
    ####################################################################
    mySql_str = u.get_connection_string_to_mysql()
            
    # Create the connection to Mysql docker container database
    cnx = create_engine(mySql_str, pool_pre_ping=True)
    warnings.warn("!DO NOT USE pandas for database manipulation in production code!!", DeprecationWarning)
    for k, v in u.TABLE_SCHEMA_DICT.items():
        # because we will try to update to sql in a loop, we might get this warning, so lets just disable it for now
        pd.options.mode.chained_assignment = None
        #########################################################
        # SOME TRANSFORMATION BEFORE WE SEND IT OFF TO DATABASE #
        
        # step-01 : replace or strip any white space or newline in column name
        df = events_denormalized_df[[col.replace('\n','').strip() for col in v]]
        # step-02 : rename the nested 'parent.child.child.column' format of column naming to only 'column'
        COLUMN_NAME_MAPPING_DICT = {}
        for col in v:
            last_dot_name = col.split('.')
            COLUMN_NAME_MAPPING_DICT[col] = last_dot_name[len(last_dot_name) - 1]
        df.rename(columns=COLUMN_NAME_MAPPING_DICT, inplace=True)
        # step-03 : since we seperated it out to multi table 2NF format, there would be many rows with blanks for every column except eventId
        #           only keeping rows which have non null in any column except eventId
        query = ' | '.join([f'(`{col}`.notna())' for col in df.columns if col != 'eventId'])
        df = df.query(query)
        #step-04 : for asthetic reasons, lets bring the primary key to the front of table structure
        eventId_col = df.pop('eventId')
        df.insert(0, 'eventId', eventId_col)
        
        # step-05 : Save this dataframe to mySQl table
        # NOTE: Pandas is, in no way, a fullfledged database connection and updation engine
        # but for purpose of this demo, we can use a quick 'to_sql' (simple yet powerful) function
        # to showcase the resulting schema, if table already exist it will simply "truncate and load" the table
        df.to_sql(k, con=cnx, index=False, if_exists="replace")
        pd.options.mode.chained_assignment = 'warn'
