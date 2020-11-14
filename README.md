# GrandDebatNational2019

## Background

Project carried out to obtain the professional certificate of Data Analyst.

---

This project aimed to develop a Python application for the analysis of quantitative data from the Great National Debate which took place in France in 2019. <br>
Open data from the Great National Debate are available by following this [link](https://granddebat.fr/pages/donnees-ouvertes).<br>

**4 topics of contribution:**
* The ecological transition
* Taxation and public spending
* Democracy and citizenship
* The organization of the State and public services

**2 categories of data by topic**
* The dataset of proposals:
  * Open questions proposed by the State
  * Open-ended answers from the participants
  * Several update dates available
* The dataset of quick questions:
  * Closed and multiple-choice questions proposed by the State
  * Predetermined answers

This project was completed in 20 days, so I chose to deal in the final dashboard only with the dataset of quick questions on the theme of ecological transition.<br>

## Folder structure

* `.private/`: should contain the JSON file with the login credentials to the MySQL database (more information [here](https://github.com/davidbassard/GrandDebatNational2019/tree/master/.private))
* `app/`: this is a package that contains the Flask web application (back and front-end). Instructions to launch the web application are given [here](https://github.com/davidbassard/GrandDebatNational2019/blob/master/app/readme.txt)
* `data/`: will contain the raw data in csv format after executing the Python code in the `data_dowloading.py` file (more information [here](https://github.com/davidbassard/GrandDebatNational2019/blob/master/data/readme.txt))
* `database`: this is a package that contains all Python files needed to create and structure the MySQL database. To create and structure the MySQL database, execute the Python code in the `database_builder.py` file
* `download/`: this is a package that contains all Python files needed to scrap and download the open data

## Additional folders

* `.mysql_dumps/`: contains the database model and the enhanced entity-relationship diagram (`gdn_db_model.mwb`), all the queries needed to recreate the database (`gdn_db_build.sql`) and all the queries used in back-end of the dasboard (`gdn_db_queries.sql`). This files were created from MySQL Workbench 8.0.
* `pictures/`: contains the `user_case_diagram.png` and the `dashboard.gif`

## Requirements

* Python 3.7 or above
* MySQL 8.0 or above
* Libraries:
  * beautifulsoup4==4.8.1
  * requests==2.22.0
  * mysql-connector==2.2.9
  * Flask==1.1.1
  * plotly==4.3.0

## Use case diagram

![Use case diagram of the application](https://github.com/davidbassard/GrandDebatNational2019/blob/master/.pictures/user_case_diagram.PNG)

## Database model

![database model](https://github.com/davidbassard/GrandDebatNational2019/blob/master/.pictures/gdn_db_model.PNG)

## Dashboard

![dashboard](https://github.com/davidbassard/GrandDebatNational2019/blob/master/.pictures/dashboard.gif)

## 

* Download and install the latest version of Python: [here](https://www.python.org/downloads/)

* Create a [virtual environment](https://docs.python.org/fr/3/library/venv.html) and install all [libraries](https://pip.pypa.io/en/stable/user_guide/)

* Download and install the latest version of MySQL Community Server - GPL [here](https://dev.mysql.com/downloads/)
  Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

* To download the data, execute the Python code of `./data_downloading.py` file

* In the folder `./.private/` create a JSON file named `mysql_settings.json` containing the login credentials to
  the MySQL database.

  The file `./.private/mysql_settings.json` is structured as follows:

    ```

    {
	    "myhost": "[host]",
	    "myuser": "[user]",
	    "mypassword": "[password]"
    }

    ```

* To create and structure the database, execute the Python code of `./database_builder.py` file

* To launch the web application, follow the instructions in the file `./dashboard.py`

