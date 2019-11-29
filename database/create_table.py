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
# Function to create tables 

def create_table(settings, DB_NAME = "gdn_db"):

    """ Creates tables into the MySQL database.

        Keyword Arguments:
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
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

    # Dictionary of tables
 
    TABLES = {}

    TABLES['tmp_survey'] = (
        "CREATE TABLE IF NOT EXISTS tmp_survey ("
            "id VARCHAR(255),"
            "createdAt VARCHAR(255),"
            "publishedAt VARCHAR(255),"
            "updatedAt VARCHAR(255),"
            "authorId VARCHAR(255),"
            "authorType VARCHAR(255),"
            "authorZipCode VARCHAR(255),"
            "sr1 VARCHAR(255),"
            "sr2 VARCHAR(255),"
            "sr3 VARCHAR(255),"
            "sr4 VARCHAR(255),"
            "sr5 VARCHAR(255),"
            "sr6 VARCHAR(255),"
            "sr7 VARCHAR(255)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['tmp_contribution'] = (
        "CREATE TABLE IF NOT EXISTS tmp_contribution ("
            "reference VARCHAR(255),"
            "title VARCHAR(255),"
            "createdAt VARCHAR(255),"
            "publishedAt VARCHAR(255),"
            "updatedAt VARCHAR(255),"
            "trashed VARCHAR(255),"
            "trashedStatus VARCHAR(255),"
            "authorId VARCHAR(255),"
            "authorType VARCHAR(255),"
            "authorZipCode VARCHAR(255),"
            "cr1 TEXT,"
            "cr2 TEXT,"
            "cr3 TEXT,"
            "cr4 TEXT,"
            "cr5 TEXT,"
            "cr6 TEXT,"
            "cr7 TEXT,"
            "cr8 TEXT,"
            "cr9 TEXT,"
            "cr10 TEXT,"
            "cr11 TEXT,"
            "cr12 TEXT,"
            "cr13 TEXT,"
            "cr14 TEXT,"
            "cr15 TEXT,"
            "cr16 MEDIUMTEXT"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['tmp_zipcode'] = (
        "CREATE TABLE IF NOT EXISTS tmp_zipcode ("
            "inseeCode VARCHAR(255),"
            "cityName VARCHAR(255),"
            "zipCode VARCHAR(255),"
            "routingLabel VARCHAR(255),"
            "line5 VARCHAR(255),"
            "gps VARCHAR(255)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['author'] = (
        "CREATE TABLE IF NOT EXISTS author ("
            "id MEDIUMINT UNSIGNED AUTO_INCREMENT,"
            "authorId VARCHAR(255) UNIQUE NOT NULL DEFAULT '',"
            "authorType VARCHAR(255) NOT NULL DEFAULT '',"
            "tmp_authorZipCode VARCHAR(255) NOT NULL DEFAULT '',"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['authorType'] = (
        "CREATE TABLE IF NOT EXISTS authorType ("
            "id TINYINT UNSIGNED AUTO_INCREMENT,"
            "label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['question'] = (
        "CREATE TABLE IF NOT EXISTS question ("
            "id TINYINT UNSIGNED AUTO_INCREMENT,"
            "label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',"
            "id_questionType TINYINT UNSIGNED NOT NULL DEFAULT 0,"
            "id_form TINYINT UNSIGNED NOT NULL DEFAULT 0,"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['questionType'] = (
        "CREATE TABLE IF NOT EXISTS questionType ("
            "id TINYINT UNSIGNED AUTO_INCREMENT,"
            "label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['form'] = (
        "CREATE TABLE IF NOT EXISTS form ("
            "id TINYINT UNSIGNED AUTO_INCREMENT,"
            "label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['geo'] = (
        "CREATE TABLE IF NOT EXISTS geo ("
            "id SMALLINT UNSIGNED AUTO_INCREMENT,"
            "cityName VARCHAR(255) NOT NULL DEFAULT '',"
            "zipCode VARCHAR(255) NOT NULL DEFAULT '',"
            "gps VARCHAR(255) NOT NULL DEFAULT '',"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['responseType'] = (
        "CREATE TABLE IF NOT EXISTS responseType ("
            "id SMALLINT UNSIGNED AUTO_INCREMENT,"
            "label VARCHAR(255) NOT NULL DEFAULT '',"
            "id_question TINYINT UNSIGNED NOT NULL DEFAULT 0,"
            "id_questionType TINYINT UNSIGNED NOT NULL DEFAULT 0,"
            "id_form TINYINT UNSIGNED NOT NULL DEFAULT 0,"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")

    TABLES['respSurveyEco'] = (
        "CREATE TABLE IF NOT EXISTS respSurveyEco ("
            "id MEDIUMINT UNSIGNED AUTO_INCREMENT,"
            "authorId VARCHAR(255) UNIQUE NOT NULL DEFAULT '',"
            "authorType VARCHAR(255) NOT NULL DEFAULT '',"
            "date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
            "sr1 VARCHAR(255) NOT NULL DEFAULT '',"
            "sr2 VARCHAR(255) NOT NULL DEFAULT '',"
            "sr3 VARCHAR(255) NOT NULL DEFAULT '',"
            "sr4 VARCHAR(255) NOT NULL DEFAULT '',"
            "sr5 VARCHAR(255) NOT NULL DEFAULT '',"
            "sr6 VARCHAR(255) NOT NULL DEFAULT '',"
            "sr7 VARCHAR(255) NOT NULL DEFAULT '',"
            "PRIMARY KEY (id)"
            ") ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4")



    # Adds tables to database

    for table_name in TABLES:

        table_description = TABLES[table_name]

        try:

            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)

        except mysql.connector.Error as error:

            if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already exists.")

            else:

                print(error.msg)

        else:

            print("Ok.")

    cnx.commit()
    cursor.close()
    cnx.close()


# ------------------------------------------------------------------------------------------------------------------
# Function to drop tables

def drop_table(settings, DB_NAME = 'gdn_db', *TABLE_NAME):


    """ Creates tables into the MySQL database.

        Keyword Arguments:
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})\n
        TABLE_NAME {list} -- name(s) of tables 
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

    # Dictionary of tables 

    TABLES = {}

    TABLES['tmp_survey'] = ("DROP TABLE IF EXISTS tmp_survey")

    TABLES['tmp_contribution'] = ("DROP TABLE IF EXISTS tmp_contribution")

    TABLES['tmp_zipcode'] = ("DROP TABLE IF EXISTS tmp_zipcode")

    TABLES['author'] = ("DROP TABLE IF EXISTS author")

    TABLES['authorType'] = ("DROP TABLE IF EXISTS authorType")

    TABLES['question'] = ("DROP TABLE IF EXISTS question")

    TABLES['questionType'] = ("DROP TABLE IF EXISTS questionType")

    TABLES['form'] = ("DROP TABLE IF EXISTS form")

    TABLES['geo'] = ("DROP TABLE IF EXISTS geo")

    TABLES['responseType'] = ("DROP TABLE IF EXISTS responseType")

    TABLES['respSurveyEco'] = ("DROP TABLE IF EXISTS respSurveyEco")

    # Drop table(s) of database

    for table_name in TABLE_NAME:

        table_description = TABLES[table_name]

        try:

            print("Dropping table {}: ".format(table_name), end='')
            cursor.execute(table_description)

        except mysql.connector.Error as error:

            if error.errno == errorcode.ER_BAD_TABLE_ERROR:
                print("Table does not exist.")

            else:

                print(error.msg)

        else:

            print("Ok.")

    cnx.commit()
    cursor.close()
    cnx.close()


# ------------------------------------------------------------------------------------------------------------------
# Test of the create_table() function

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

    create_table(settings, DB_NAME)


# ------------------------------------------------------------------------------------------------------------------
# Test of the drop_table() function

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

    drop_table(settings, DB_NAME, 'tmp_survey', 'geo', 'author')


