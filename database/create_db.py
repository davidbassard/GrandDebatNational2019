# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

import os
import json
import mysql.connector
from mysql.connector import errorcode

# ------------------------------------------------------------------------------------------------------------------
# Function to create database "gdn_db"

def create_database(settings, DB_NAME = "gdn_db"):

    """ Creates the MySQL database. 

        Keyword Arguments: \n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})

    """

    db_name = DB_NAME.upper()

    cnx = mysql.connector.connect(**settings)
    cursor = cnx.cursor()

    try:
        cursor.execute("USE {}".format(db_name))

    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))

        if error.errno == errorcode.ER_BAD_DB_ERROR:

            try:

                cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARSET = UTF8MB4".format(db_name))

                print("Database {} created successfully.".format(db_name))
                cnx.database = db_name

            except mysql.connector.Error as error:

                print("Failed creating database: {}".format(error))
                exit(1)

        else:

            print(error.msg)
            exit(1)

    cursor.close()
    cnx.close()


# ------------------------------------------------------------------------------------------------------------------
# Function to drop database "gdn_db"

def drop_database(settings, DB_NAME = "gdn_db"):

    """ Drop the MySQL database.

        Keyword Arguments:
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})

    """
    db_name = DB_NAME.upper()

    cnx = mysql.connector.connect(**settings)
    cursor = cnx.cursor()

    try:

        cursor.execute("DROP DATABASE {}".format(db_name))

    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)
        exit(1)

    else:

        print("Database {} dropped successfully".format(db_name))

    cursor.close()
    cnx.close()


# ------------------------------------------------------------------------------------------------------------------
# Test of the create_database() function

if __name__ == "__main__":


    path_json_creds = "./.private/mysql_settings.json"
    mysql_settings = json.load(open(path_json_creds, "r"))

    settings = {
        "host": mysql_settings["myhost"],
        "user": mysql_settings["myuser"],
        "password": mysql_settings["mypassword"],
        "raise_on_warnings" : True
    }

    DB_NAME = "test"

    create_database(settings, DB_NAME)


# ------------------------------------------------------------------------------------------------------------------
# Test of drop_database() function

if __name__ == "__main__":

    path_json_creds = "./.private/mysql_settings.json"
    mysql_settings = json.load(open(path_json_creds, "r"))

    settings = {
        "host": mysql_settings["myhost"],
        "user": mysql_settings["myuser"],
        "password": mysql_settings["mypassword"],
        "raise_on_warnings" : True
    }

    DB_NAME = "test"

    drop_database(settings, DB_NAME)


























