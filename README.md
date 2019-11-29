# GrandDebatNational2019
Project carried out to obtain the professional certificate of Data Analyst

---

The project aims to develop a Python application for the analysis of quantitative data from the Great National Debate held in France in 2019.

---

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

