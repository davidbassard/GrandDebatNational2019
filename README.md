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
* `data/`: will contain the raw data in csv format after executing the python code in the `data_dowloading.py` file (more information [here](https://github.com/davidbassard/GrandDebatNational2019/blob/master/data/readme.txt))
* `database`: this is a package that contains all python files needed to create and structure the MySQL database. To create and structure the MySQL database, execute the python code in the `database_builder.py` file
* `download/`: this is a package that contains all python files needed to scrap and download the open data

## Additional folders

* `.mysql_dumps/`: contains the database model and the enhanced entity-relationship diagram (`gdn_db_model.mwb`), all the queries needed to recreate the database (`gdn_db_build.sql`) and all the queries used in back-end of the dasboard (`gdn_db_queries.sql`). This files were created from MySQL Workbench 8.0.
* `pictures/`: contains the `user_case_diagram.png` and the `dashboard.gif`

## Use case diagram

![Use case diagram of the application](https://github.com/davidbassard/GrandDebatNational2019/blob/master/.pictures/user_case_diagram.PNG)

## Database model



For the moment the application downloads the data, builds a MySQL database and presents some results of the ecological transition questionnaire.
The results are displayed using the web Flask microframework.

---

- To download the data, run the code of python file "./data_downloading.py"

- In the folder "./.private/" create a JSON file named "mysql_settings.json" containing the login credentials to 
  the MySQL database.

  The file "./.private/mysql_settings.json" is structured as follows:

  {
	  "myhost": "[host]",
	  "myuser": "[user]",
	  "mypassword": "[password]"
  }

- To create and structure the database that will store the data folder of the Great National Debate run the code of 
  python file "./database_builder.py"

    - The Python application requires a prior installation of MySQL Community Server.
    - You can download MySQL Community Server - GPL here: https://dev.mysql.com/downloads/
      Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

- To launch the web application, follow the instructions in the file "./dashboard.py"

