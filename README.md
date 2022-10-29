# Pre-requisites
Make sure you have the following installed and appropriate **$PATH** modifications done in your OS of choice (MacOS / Linux / Windows):

* **git** (_version 2.37.x_)
* **docker** (_version 20.x_) (_[Docker Desktop](https://www.docker.com/products/docker-desktop/) recommended_)

_NOTE : I have not tested this to older versions of above pre-requisites_

__IMPORTANT NETWORK REQUIREMENT__: Also, make sure you **ARE NOT** running this in your private organization's / personal VPN or proxy IPs and that commandline access to pip / apt-get / yum / docker / docker-compose (*whichever is your preferred installation method*) is not blocked or hindered.  

_NOTE : modified the **testEventData-1.txt** file at line 251 to test out multi dictionary list of **properties.variants**_
# Installation
### Cloning the Repo
    % cd ~/{your-project-directory}
    % git clone  https://github.com/maiden7705/boxed-assignment-demo-1.git
    % cd ~/{your-project-directory}/boxed-assignment-demo-1
### Creating Docker containers
    % docker-compose --verbose build --no-cache
    % docker-compose up -d
The above command will create:
* [mySql-8.0](https://hub.docker.com/_/mysql), (_your backend database_)
* [python-3.10-bullseye](https://hub.docker.com/_/python), (_your ETL Code_)
* [phpmyadmin-5.0](https://hub.docker.com/_/phpmyadmin), (_Database web client_: to view tables)
### Running ETL Code
    % docker exec -i -t python3.11 bash
    % python ETL-json-to-SQL.py
### Checking Database
    http://localhost:8081/

![sql client homepage](/documentations/sql_client_homepage.png)


![sql client tables](/documentations/sql_client_checking_tables.png)

## Understanding of JSON structure
To understand the design justification of 2NF normalized form of seperate tables, refer to this [jupyter notebook](/Requirement/understanding_json_structure.ipynb)


