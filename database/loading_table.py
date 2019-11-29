# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

import os
import json
import mysql.connector
from mysql.connector import errorcode
from database import local_infile as li

# ------------------------------------------------------------------------------------------------------------------
# Function to load data of CSV file "survey_raw.csv" into temporary table "tmp_survey"

def load_data(settings, TABLE_NAME, DB_NAME = "gdn_db", display_limit = 10):

    """ Loads data from CSV file into temporary table.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        TABLE_NAME {str} -- name of table \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})\n
        dislay_limit {int} -- limit of the number of lines displayed after loading - (default: {10})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor()
        cursor.execute("USE {}".format(db_name))

    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))

    # Loading data into table

    try:

        if TABLE_NAME == "tmp_survey":

            sql = (
                "LOAD DATA LOCAL INFILE %s                          "
                "   INTO TABLE tmp_survey                           "
                "   CHARACTER SET UTF8MB4                           "
                "   FIELDS  TERMINATED              BY ','          "
                "           OPTIONALLY ENCLOSED     BY '\"'         "
                "   LINES   TERMINATED              BY '\n'         "
                "   IGNORE 1 LINES                                  "
                )

            csv_file = "survey_raw.csv"
            path_csv_file = os.path.join('./data/', csv_file)

            request = (path_csv_file, )

            cursor.execute(sql, request)

            print(cursor.rowcount, "records inserted.")

        if TABLE_NAME == "tmp_contribution":

            sql = (
                "LOAD DATA LOCAL INFILE %s                          "
                "   INTO TABLE tmp_contribution                     "
                "   CHARACTER SET UTF8MB4                           "
                "   FIELDS  TERMINATED              BY ','          "
                "           OPTIONALLY ENCLOSED     BY '\"'         "
                "   LINES   TERMINATED              BY '\n'         "
                "   IGNORE 1 LINES                                  "
                )

            csv_file = "contribution_raw.csv"
            path_csv_file = os.path.join('./data/', csv_file)

            request = (path_csv_file, )

            cursor.execute(sql, request)

            print(cursor.rowcount, "records inserted.")

        if TABLE_NAME == "tmp_zipcode":

            sql = (
                "LOAD DATA LOCAL INFILE %s                          "
                "   INTO TABLE tmp_zipcode                          "
                "   CHARACTER SET UTF8MB4                           "
                "   FIELDS  TERMINATED              BY ','          "
                "           OPTIONALLY ENCLOSED     BY '\"'         "
                "   LINES   TERMINATED              BY '\r\n'       "
                "   IGNORE 1 LINES                                  "
                )

            csv_file = "zipcode_raw.csv"
            path_csv_file = os.path.join('./data/', csv_file)

            request = (path_csv_file, )

            cursor.execute(sql, request)

            print(cursor.rowcount, "records inserted.")

    except mysql.connector.Error as error:

        print(error)

    else:

        cnx.commit()
        display_limit = str(display_limit)
        cursor.execute("SELECT * FROM {} LIMIT {}".format(TABLE_NAME, display_limit))
        result = cursor.fetchall()

        print("The first {} rows of the file:".format(display_limit))
        
        for row in result:

            print(row)

        print("Everything is ok!")

    cursor.close()
    cnx.close()


# ------------------------------------------------------------------------------------------------------------------
# Test of the load_survey() function

if __name__ == "__main__":


    path_json_creds = "./.private/mysql_settings.json"
    mysql_settings = json.load(open(path_json_creds, "r"))

    settings = {
        "host": mysql_settings["myhost"],
        "user": mysql_settings["myuser"],
        "password": mysql_settings["mypassword"],
        "raise_on_warnings" : True
    }

    li.local_infile(settings, li = 'ON')

    TABLE_NAME = "tmp_survey"
    DB_NAME = "test"
    load_data(settings, TABLE_NAME, DB_NAME, display_limit = 10)

    TABLE_NAME = "tmp_contribution"
    DB_NAME = "test"
    load_data(settings, TABLE_NAME, DB_NAME, display_limit = 10)

    TABLE_NAME = "tmp_zipcode"
    DB_NAME = "test"
    load_data(settings, TABLE_NAME, DB_NAME, display_limit = 10)

    li.local_infile(settings, li = 'OFF')










