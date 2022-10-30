# Running in Container
## Pre-requisites
Make sure you have the following installed and appropriate **$PATH** modifications done in your OS of choice (MacOS / Linux / Windows):

* **git** (_version 2.37.x_)
* **docker** (_version 20.x_) (_[Docker Desktop](https://www.docker.com/products/docker-desktop/) recommended_)
* Atleast **3 GB** of space for the docker images and container

_NOTE : I have not tested this to older versions of above pre-requisites_

__IMPORTANT NETWORK REQUIREMENT__: 
* Make sure you **ARE NOT** running this in your private organization's / personal VPN or proxy IPs and that commandline access to pip / apt-get / yum / docker / docker-compose (*whichever is your preferred installation method*) is not blocked or hindered.  

* Make sure the following ports are not blocked on host:
    * **3306**&nbsp;&nbsp;: for My SQL TCP/IP connection
    * **8081**&nbsp;&nbsp;: for phpMyAdmin client to view SQL tables

## Installation
* ### Cloning the Repo
    ```console
    % cd ~/{your-project-directory}
    % git clone  https://github.com/maiden7705/boxed-assignment-demo-1.git
    % cd ~/{your-project-directory}/boxed-assignment-demo-1
    ```
* ### Creating Docker containers
    ```console
    % docker-compose --verbose build --no-cache
    % docker-compose up -d
    ```
    The above command will create:
    * [mySql-8.0](https://hub.docker.com/_/mysql), (_your backend database_)
    * [python-3.10-bullseye](https://hub.docker.com/_/python), (_your ETL Code_)
    * [phpmyadmin-5.0](https://hub.docker.com/_/phpmyadmin), (_Database web client_: to view tables)
## Running ETL Code
```console
% docker exec -i -t python3.10 bash
% python ETL-json-to-SQL.py
```
This will put normalized 2NF table structure into database called **web_scraping** _(I previously thought this was a web scraping bot json :smiley: )_
## Checking Database
    http://localhost:8081/

![sql client homepage](/documentations/sql_client_homepage.png)

Expand the database **web_scraping** to see the 2NF normalized table structure

![sql client tables](/documentations/sql_client_checking_tables.png)

## Stopping docker containers and removing compose image
```console
% cd ~/{your-project-directory}/boxed-assignment-demo-1
% docker-compose down
% docker image rm --force $(docker images | grep boxed* | awk '{print $1}')
```

# Running in Host (VS Code) [OPTIONAL]
If you choose to see or debug the project in [VS code](https://code.visualstudio.com/), perform the following steps:

* ## Pre-requisites
    Make sure you have following installed:  

    * [VS code](https://code.visualstudio.com/)
    * [python 3.11](https://www.python.org/downloads/)
        ```console
        % python3 --version
        Python 3.10.7
        ```
    * [pip3](https://pypi.org/project/pip/)
        ```console
        python -m pip install --upgrade pip
        ```

* ## Cloning the Repo
    ```console
    % cd ~/{your-project-directory}
    % git clone https://github.com/maiden7705/boxed-assignment-demo-1.git
    % cd ~/{your-project-directory}/boxed-assignment-demo-1
    ```

* ## Open VS Code from project folder
    ```console
    % cd ~/{your-project-directory}/boxed-assignment-demo-1
    % code .
    ```

* ## Install python virtual environment
    Open a new [VS Code Terminal](https://code.visualstudio.com/docs/terminal/basics) in project root folder
    ```console
    % python3 -m pip install virtualenv
    % mkdir .env
    % cd .env
    % python3 -m virtualenv .
    ```

* ## Install all the pre-requisite libraries
    
    * ### Linux / macOS
        ```console
        % pip install -r ./docker/python3/requirements.txt
        ```
    * ### Windows powershell
        ```console
        % pip install -r .\docker\python3\requirements.txt
        ```

* ## Installing the VS Code extensions
    run the following command in terminal window
    * ### Linux / macOS
        open a terminal window and run this from project directory root:
        ```console
        % ./extensions/vs_code_extensions.sh
        ```
    * ### Windows powershell
        open a powershell prompt from start menu and cd into project root directory and run this:
        ```console
        :\> cmd.exe /c ".\extensions\vs_code_extensions.bat"
        ```

* ## Running the code
    Open and run the file **ETL-json-to-SQL.py**
    ![Run the scripot](/documentations/running_the_Script.png)

# Understanding of JSON structure
To understand the design justification of 2NF normalized form of seperate tables, refer to this [jupyter notebook](/Requirement/understanding_json_structure.ipynb)

_NOTE : I have modified the **[testEventData-1.txt](Requirement/testEventData-1.txt)** file at line 251 to test out multi dictionary list of **properties.variants**_

* ## Table Schema Design
    ![Schema Design](/documentations/Boxed-Demo-DDL-schema.png)

* ## DDL scripts
    The DDL scripts to above schema can be found [here](DDL_scripts.sql)