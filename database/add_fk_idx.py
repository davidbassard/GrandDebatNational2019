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
# Function to add foreign keys and indexes

def fk_idx(settings, DB_NAME = "gdn_db"):

    """ Adds foreign keys and indexes to MySQL database tables.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})\n
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

    # ------------------------------------------------------------------------------------------------------------------
    # Add foreign keys and indexes
    # ------------------------------------------------------------------------------------------------------------------

    # Add foreign key on the column id_authorType to the table author

    counter = 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `author` "
        "ADD CONSTRAINT `fk_authorType_author` FOREIGN KEY (`id_authorType`) REFERENCES `authorType` (`id`)"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add foreign key on the column id_question, id_questionType and id_form to the table responseType
    # and an index fulltext on the column label

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `responseType` "
        "ADD CONSTRAINT `fk_question_responseType` FOREIGN KEY (`id_question`) REFERENCES `question` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `responseType` "
        "ADD CONSTRAINT `fk_questionType_responseType` FOREIGN KEY (`id_questionType`) REFERENCES `questionType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `responseType` "
        "ADD CONSTRAINT `fk_form_responseType` FOREIGN KEY (`id_form`) REFERENCES `form` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `responseType` "
        "ADD FULLTEXT `idx_full_responseType` (`label`)"
        )

    except mysql.connector.Error as error:

        if error.msg == "InnoDB rebuilding table to add column FTS_DOC_ID":

            print(error.msg, end = '')
            print(". Ok.")

        else:

            print("Something went wrong: {}".format(error))

    else:

        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Add foreign key on the column id_questionType, and id_form to the table question
    # and an index fulltext on the column label

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `question` "
        "ADD CONSTRAINT `fk_questionType_question` FOREIGN KEY (`id_questionType`) REFERENCES `questionType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `question` "
        "ADD CONSTRAINT `fk_form_question` FOREIGN KEY (`id_form`) REFERENCES `form` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `question` "
        "ADD FULLTEXT `idx_full_question` (`label`)"
        )

    except mysql.connector.Error as error:

        if error.msg == "InnoDB rebuilding table to add column FTS_DOC_ID":

            print(error.msg, end = '')
            print(". Ok.")

        else:

            print("Something went wrong: {}".format(error))

    else:

        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Add foreign key on the column id_author, id_authorType, id_sr1, id_sr2, id_sr3, id_sr4, isr5, id_sr 6 and id_sr7 to
    # the table respSurveyEco

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_author_respSurveyEco` FOREIGN KEY (`id_author`) REFERENCES `author` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_authorType_respSurveyEco` FOREIGN KEY (`id_authorType`) REFERENCES `authorType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_sr1_respSurveyEco` FOREIGN KEY (`id_sr1`) REFERENCES `responseType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_sr2_respSurveyEco` FOREIGN KEY (`id_sr2`) REFERENCES `responseType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_sr3_respSurveyEco` FOREIGN KEY (`id_sr3`) REFERENCES `responseType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_sr4_respSurveyEco` FOREIGN KEY (`id_sr4`) REFERENCES `responseType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_sr5_respSurveyEco` FOREIGN KEY (`id_sr5`) REFERENCES `responseType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_sr6_respSurveyEco` FOREIGN KEY (`id_sr6`) REFERENCES `responseType` (`id`)"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "ADD CONSTRAINT `fk_sr7_respSurveyEco` FOREIGN KEY (`id_sr7`) REFERENCES `responseType` (`id`)"
        )

    except mysql.connector.Error as error:


        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()

    cursor.close()
    cnx.close()

# ------------------------------------------------------------------------------------------------------------------
# Function to drop foreign keys and indexes

def drop_fk_idx(settings, DB_NAME = "gdn_db"):

    """ Drop foreign keys and indexes to MySQL database tables.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})\n
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

    # ------------------------------------------------------------------------------------------------------------------
    # Drop foreign key on the column id_authorType to the table author

    counter = 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `author` "
        "DROP FOREIGN KEY `fk_authorType_author`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Drop foreign key on the column id_question, id_questionType and id_form to the table responseType
    # and the index fulltext on the column label

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `responseType` "
        "DROP FOREIGN KEY `fk_question_responseType`"
        )

        cursor.execute(
        "ALTER TABLE `responseType` "
        "DROP FOREIGN KEY `fk_questionType_responseType`"
        )

        cursor.execute(
        "ALTER TABLE `responseType` "
        "DROP FOREIGN KEY `fk_form_responseType`"
        )

        cursor.execute(
        "ALTER TABLE `responseType` "
        "DROP INDEX `idx_full_responseType`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Drop foreign key on the column id_questionType, and id_form to the table question
    # and the index fulltext on the column label

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `question` "
        "DROP FOREIGN KEY `fk_questionType_question`"
        )

        cursor.execute(
        "ALTER TABLE `question` "
        "DROP FOREIGN KEY `fk_form_question`"
        )

        cursor.execute(
        "ALTER TABLE `question` "
        "DROP INDEX `idx_full_question`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Drop foreign key on the column id_author, id_authorType, id_sr1, id_sr2, id_sr3, id_sr4, isr5, id_sr 6and id_sr7 to 
    # the table respSurveyEco

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_author_respSurveyEco`"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_authorType_respSurveyEco`"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_sr1_respSurveyEco`"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_sr2_respSurveyEco`"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_sr3_respSurveyEco`"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_sr4_respSurveyEco`"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_sr5_respSurveyEco`"
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_sr6_respSurveyEco` "
        )

        cursor.execute(
        "ALTER TABLE `respSurveyEco` "
        "DROP FOREIGN KEY `fk_sr7_respSurveyEco`"
        )

    except mysql.connector.Error as error:


        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()

    cursor.close()
    cnx.close()


# ------------------------------------------------------------------------------------------------------------------
# Test of the fk_idx() function

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

    fk_idx(settings, DB_NAME)


# ------------------------------------------------------------------------------------------------------------------
# Test of the drop_fk_idx() function

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

    drop_fk_idx(settings, DB_NAME)


