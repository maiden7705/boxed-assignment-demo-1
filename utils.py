# Imports
import os, yaml
import pandas as pd

# variables
distinct_elements = []
node_tree_list = []
distinct_flat_node_tree_list = []
flat_list = []
edges = []
TABLE_SCHEMA_DICT = {}
TABLE_SCHEMA_LIST = []
VALUE_AS_LIST = []

def get_last_elements(node):
  if (len(node.split(':')) > 1):
    return node.rsplit(':', 2)[-2]
  return ''

def keys(d, c = []):
  return [i for a, b in d.items() for i in ([c+[a]] if not isinstance(b, dict) else keys(b, c+[a]))]

def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]

def flatten_nested_list(lst):
  return [item for sublist in lst for item in sublist]

def item_in_this_list(item, lst):
  last_match = 0
  nodeLst = item.split(':')
  if len(nodeLst) == 1:
    return None
  for i, node in enumerate(nodeLst):
    if node in lst:
      last_match = i
      continue;
    return nodeLst[last_match] if last_match == 0 else ':'.join(nodeLst[0:last_match + 1])

def distinct_list_elements(lst):
  for node in lst:
    if node not in distinct_flat_node_tree_list:
        distinct_flat_node_tree_list.append(node)

def distinct_depth_nodes(d, root):
  ''' Simple function to find json's nested dictionary depth
  '''
  for a, b in d.items():
      if isinstance(b, dict):
        edges.append((root, a))
        distinct_depth_nodes(b, a)

def distinct_col_list(cols: list):
    return [last_element(col) for col in cols]

def last_element(col: str):
    col_splited = col.split('.')
    return col_splited[len(col_splited) - 1]

def fill_dict(parent, child):
    if parent not in TABLE_SCHEMA_DICT.keys():
                TABLE_SCHEMA_DICT[parent] = []

    if (child not in TABLE_SCHEMA_DICT[parent]):
        TABLE_SCHEMA_DICT[parent].append(child)

def rename_cols(col_name, append_str):
    if col_name != 'eventId':
        return append_str + '.' + col_name
    return col_name

def distinct_depth_table_unique(d: dict, root: str, nest_parent_name=''):
    nest_names = lambda x : '.'.join(filter(None, [nest_parent_name, x])).replace('event.','')
    fill_dict(root, 'eventId')
    column_list = []
    table_to_schema = {}
    for a, b in d.items():
        # if a == 'properties':
        #     print('we\'ve arrived')
        col_with_dot_format = a.split('.')
        if(len(col_with_dot_format) > 1):
            parent = col_with_dot_format[len(col_with_dot_format) - 2]
            child = col_with_dot_format[len(col_with_dot_format) - 1]
            fill_dict(parent, nest_names(child))
        else:
            parent = root
            child = a
            if not isinstance(b, dict):
                fill_dict(parent, nest_names(child))
        if isinstance(b, dict):
            distinct_depth_table_unique(b, a, f'{root}.{a}')

def seperate_table_from_flattened_col_list(sorted_col_list: list):
  u''' 
      Purpose:
      --------
      using `.(dot)` as nesting seperator, recursively put columns at level `N` inside table `N-1`

      Example:
      --------
      from this flat table:\u000A
      `events`\u27A4\u000A
      `|event | eventId | properties.variants | properties.variants.variant | properties.variants.quantity | properties.address._id | properties.address.addressLine1 | properties.address.addressLine2`\u000A
      Creates a dictionary of list \u27A4 `dict(list)` of format:\u000A
      `{"table_name1":['column1', 'column2'], "table_name2":[], .... }`\u000A
      like:\u000A
      `{`\u000A
      \u2003\u2003\u2003`"events":['event', 'eventId']`\u000A
      \u2003\u2003\u2003`"events.properties":['eventId', 'variants']`\u000A
      \u2003\u2003\u2003`"events.properties.variants":['eventId', 'variant', 'quantity']`\u000A
      \u2003\u2003\u2003`"events.properties.address":['eventId', '_id', 'addressLine1', 'addressLine2']`\u000A
      `}`\u000A
      
      Parameters
      ----------
      `sorted_col_list` \u27A4 sorted list of dataframe columns (can be computer with `df.columns.tolist().sort()`)

      Returns
      -------
      \u27A4 `void` -- will add found values, to the dictionary of list in `TABLE_SCHEMA_DICT` global variable
  '''
  for col in sorted_col_list:
      col_depth_splitted = col.split('.')
      if(len(col_depth_splitted) > 1):
          parent = 'events.' + '.'.join(col_depth_splitted[0:len(col_depth_splitted) - 1])
          fill_dict(parent, col)
      else: fill_dict('events', col)
  for tables in TABLE_SCHEMA_DICT.keys():
      fill_dict(tables, 'eventId')

def find_values_as_list_of_dicts(d: dict, root=''):
  u''' 
      Purpose
      ----------
      finds all keys who's value are of type "list of dictionaries \u27A4 `list(dict)`"\u000A
      e.g. if we have a key called `variants` inside `properties` dict, like this:
      `"properties":{`\u000A
      `\u2003\u2003\u2003"variants": [`\u000A
      `\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003{"quantity": 1, "variant": "5277cc4a49041ca90b000028"},`\u000A
      `\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003{"quantity": 2, "variant": "5277cc4a49041ca90b000031"}`\u000A
      `\u2003\u2003\u2003]`\u000A
      `}`\u000A
      then this function adds full path to the global variable `VALUE_AS_LIST (list)`\u000A
      `\u27A4 VALUE_AS_LIST.append('properties.variants')`
      
      Parameters
      ----------
      `d` \u27A4 json dictionary to recursively search in

      `root [OPTIONAL]` \u27A4 root (parent) node to append current node to

      Returns
      -------
      \u27A4 `void` -- will add found values, to the list of keys in `VALUE_AS_LIST` global variable with it's parent structure
      
  '''
  nest_names = lambda x : '.'.join(filter(None, [root, x])).replace('event.','')
  for a, b in d.items():
    if isinstance(b, list) and (b not in VALUE_AS_LIST):
      if any(isinstance(e, dict) for e in b):
        VALUE_AS_LIST.append(nest_names(a))
    if isinstance(b, dict):
          find_values_as_list_of_dicts(b, nest_names(a))
  
def flatten_list_of_dict_keys_to_seperate_columns(events_denormalized_df : pd.DataFrame):
  u''' 
    Purpose
    ----------
    Using the list of properties found in global `VALUE_AS_LIST` e.g. `["properties.variants"]`\u000A
    Converts following table structure for all columns in the list:

    `|event - - - - - | eventId - - - - - - - | properties.variants\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003
\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003`\u000A
    `|viewMiniCart - -| 2359831743685152469 - | []\u2003\u2003\u2003|\u000A`
    `|viewCart - - - -| 2359831743685152470 - | [{"quantity": 1, "variant": "5277cc4a49041ca90b000028"},\u000A`
    `|\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|`
    `\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|`
    `{"quantity": 2, "variant": "5277cc4a49041ca90b000031"}]`  


   to this form:  

   
  `|event - - - - - | eventId - - - - - - - | properties.variants | properties.variants.variant | properties.variants.quantity`\u000A
  `|viewMiniCart - -| 2359831743685152469 - | []\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|`
  `\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|
\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|\u000A`
  `|viewCart - - - -| 2359831743685152470 - | \u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|`
  `1\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|
5277cc4a49041ca90b000028\u2003\u2003\u2003|`
  `|viewCart - - - -| 2359831743685152470 - | \u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|`
  `2\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003\u2003|
5277cc4a49041ca90b000031\u2003\u2003\u2003|`

    Parameters
    ----------
    events_denormalized_df \u27A4 `pandas.DataFrame`    
    
    Returns
    -------
    \u27A4 `pd.DataFrame`
  '''
  for key in VALUE_AS_LIST:
    df = events_denormalized_df.loc[:, ["eventId", key]]
    df = pd.json_normalize(df.to_dict('records'), key, ["eventId"])
    df.columns = [rename_cols(x, key) for x in df.columns]
    events_denormalized_df = pd.merge(events_denormalized_df, df, on="eventId", how="left")
    events_denormalized_df = events_denormalized_df.drop([key], axis=1)
  return events_denormalized_df

def get_host_name():
  u'''
  PURPOSE
  -------
  Detects if the code is running inside docker container\u000A
  Or simply from vs code or some IDE in host, and accordingly changes the hostname

  RETURNS
  -------
  `db` \u27A4 inside docker container\u000A
  `localhost` \u27A4 host machine IDE\u000A
  '''
  SECRET_KEY = os.environ.get('IS_RUNNING_IN_CONTAINER', False)
  return 'db' if SECRET_KEY else 'localhost'
      

def get_connection_string_to_mysql():
  u'''
  Purpose
  -------
  opens the `docker-compose.yml` file and uses database configurations to get values

  Returns
  -------
  returns connection string (`str`) to the database
  '''
  docker_compose = {}
  with open('docker-compose.yml', 'r') as f:
    docker_compose = yaml.safe_load(f)
  username="root"
  password=docker_compose['services']['db']['environment'][0].split('=')[1]
  hostname=get_host_name()
  port=docker_compose['services']['db']['ports'][0].split(':')[0]
  database_name=docker_compose['services']['db']['environment'][1].split('=')[1]

  return f'mysql://{username}:{password}@{hostname}:{port}/{database_name}'