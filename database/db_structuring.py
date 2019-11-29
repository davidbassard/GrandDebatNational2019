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
# Function to structure database

def db_structure(settings, DB_NAME = "gdn_db"):

    """ Structures all operations applied to the MySQL database (except foreign keys and index).

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
    # Insert from tables tmp_survey, tmp_zipcode
    # ------------------------------------------------------------------------------------------------------------------

    # Insert authorId, authorType, authorZipCode into table author from tmp_survey

    counter = 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "INSERT INTO `author` (`authorId`, `authorType`, `tmp_authorZipCode`)"
                "SELECT `authorId`, `authorType`, `authorZipCode`"
                    "FROM `tmp_survey`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Insert publishedAt, sr1, sr2, sr3, sr4, sr5, sr6, sr7 into table respSurveyEco from tmp_survey

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "INSERT INTO `respSurveyEco` (`authorId`, `authorType`, `date`, `sr1`, `sr2`, `sr3`, `sr4`, `sr5`, `sr6`, `sr7`)"
                "SELECT `authorId`, `authorType`, `publishedAt`, `sr1`, `sr2`, `sr3`, `sr4`, `sr5`, `sr6`, `sr7`"
                    "FROM `tmp_survey`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Insert cityName, zipCode, gps into table geo from table tmp_zipcode

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "INSERT INTO `geo` (`cityName`, `zipCode`, `gps`)"
                "SELECT `cityName`, `zipCode`, `gps`"
                    "FROM `tmp_zipcode`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Insert by hand
    # ------------------------------------------------------------------------------------------------------------------

    # Insert label into table authorType

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        sql = "INSERT INTO `authorType` (`label`) VALUES (%s)"

        val = [
        ('Non renseigné',),
        ('Citoyen / Citoyenne',),
        ('Élu / élue et Institution',),
        ('Organisation à but lucratif',),
        ('Organisation à but non lucratif',)
        ]

        cursor.executemany(sql, val)

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Insert label into table form

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        sql = "INSERT INTO `form` (`label`) VALUES (%s)"

        val = [
        ('Survey: ecological transition',),
        ('Contribution: ecological transition',),
        ('Survey: taxation and public expenditure',),
        ('Contribution: taxation and public expenditure',),
        ('Survey: democracy and citizenship',),
        ('Contribution: democracy and citizenship',),
        ('Survey: the organization of the State and public services',),
        ('Contribution: the organization of the State and public services',)
        ]

        cursor.executemany(sql, val)

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Insert label into table questionType

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        sql = "INSERT INTO `questionType` (`label`) VALUES (%s)"

        val = [
        ('Closed-ended question',),
        ('Multiple-choice question',),
        ('Open-ended question',)
        ]

        cursor.executemany(sql, val)

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Insert label into table question and id_questionType, id_form (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        sql = "INSERT INTO `question` (`label`, `id_questionType`, `id_form`) VALUES (%s, %s, %s)"

        val = [
        ("Pensez-vous que vos actions en faveur de l'environnement peuvent \
vous permettre de faire des économies ?", "1", "1"),
        ("Diriez-vous que vous connaissez les aides et dispositifs qui sont \
aujourd'hui proposés par l'Etat, les collectivités, les entreprises et \
les associations pour l'isolation et le chauffage des logements, et pour \
les déplacements ?", "1", "1"),
        ("Pensez-vous que les taxes sur le diesel et sur l’essence peuvent \
permettre de modifier les comportements des utilisateurs ?", "1", "1"),
        ("À quoi les recettes liées aux taxes sur le diesel et l’essence \
doivent-elles avant tout servir ?", "2", "1"),
        ("Selon vous, la transition écologique doit être avant tout financée par :", "2", "1"),
        ("Et qui doit être en priorité concerné par le financement de la \
transition écologique ?", "2", "1"),
        ("Que faudrait-il faire pour protéger la biodiversité et \
le climat tout en maintenant des activités agricoles et industrielles \
compétitives par rapport à leurs concurrents étrangers, notamment européens ?", "2", "1"),
        ]

        cursor.executemany(sql, val)

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Insert label into table responseType and id_question, id_questionType, id_form (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        sql = "INSERT INTO `responseType` (`label`, `id_question`, `id_questionType`, `id_form`) VALUES (%s, %s, %s, %s)"

        val = [
        ("Sans avis", "1", "1", "1"),
        ("Oui", "1", "1", "1"),
        ("Non", "1", "1", "1"),
        ('Sans avis', "2", "1", "1"),
        ("Oui", "2", "1", "1"),
        ("Non", "2", "1", "1"),
        ("Sans avis", "3", "1", "1"),
        ("Oui", "3", "1", "1"),
        ("Non", "3", "1", "1"),
        ("Sans avis", "4", "2", "1"),
        ("À baisser d’autres impôts comme par exemple l’impôt sur le revenu ?", "4", "2", "1"),
        ("À financer des investissements en faveur du climat ?", "4", "2", "1"),
        ("À financer des aides pour accompagner les Français dans la transition écologique ?", "4", "2", "1"),
        ("Sans avis", "5", "2", "1"),
        ("Par le budget général de l’État", "5", "2", "1"),
        ("Par la fiscalité écologique", "5", "2", "1"),
        ("Les deux", "5", "2", "1"),
        ("Je ne sais pas", "5", "2", "1"),
        ("Sans avis", "6", "2", "1"),
        ("Les administrations", "6", "2", "1"),
        ("Les administrations|Les entreprises", "6", "2", "1"),
        ("Les administrations|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Les administrations|Les entreprises|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les entreprises|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les administrations|Les particuliers", "6", "2", "1"),
        ("Les administrations|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Les administrations|Les particuliers|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les particuliers|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les administrations|Tout le monde", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Les entreprises", "6", "2", "1"),
        ("Les entreprises|Les administrations", "6", "2", "1"),
        ("Les entreprises|Les administrations|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Les administrations|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les administrations|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Les administrations", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les administrations|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les particuliers|Les administrations", "6", "2", "1"),
        ("Les particuliers", "6", "2", "1"),
        ("Les particuliers|Les administrations", "6", "2", "1"),
        ("Les particuliers|Les administrations|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Les administrations|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les administrations|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Les administrations", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les administrations|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les entreprises|Les administrations", "6", "2", "1"),
        ("Tout le monde", "6", "2", "1"),
        ("Tout le monde|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les administrations|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les particuliers|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les administrations|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les entreprises|Les administrations", "6", "2", "1"),
        ("Sans avis", "7", "2", "1"),
        ("Cofinancer un plan d’investissement pour changer les modes de production", "7", "2", "1"),
        ("Modifier les accords commerciaux", "7", "2", "1"),
        ("Taxer les produits importés qui dégradent l’environnement", "7", "2", "1")
        ]

        cursor.executemany(sql, val)

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok. => ", end = '')
        print(cursor.rowcount, "records inserted.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add column, update data and drop column
    # ------------------------------------------------------------------------------------------------------------------

    # Add column id_author to table respSurveyEco and update it with id of table author (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_author` MEDIUMINT UNSIGNED DEFAULT 0 AFTER `id`"
        )

        cursor.execute(
            "UPDATE `author`, `respSurveyEco`"
                "SET `respSurveyEco`.`id_author` = `author`.`id`" 
            "WHERE `author`.`authorId` = `respSurveyEco`.`authorId`"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `authorId`"
        )


    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Add column id_authorType to table respSurveyEco and update it with id of table authorType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_authorType` TINYINT UNSIGNED DEFAULT 0 AFTER `id_author`"
        )

        cursor.execute(
            "UPDATE `authorType`, `respSurveyEco`"
                "SET `respSurveyEco`.`id_authorType` = `authorType`.`id`" 
            "WHERE `authorType`.`label` = `respSurveyEco`.`authorType`"
        )

        cursor.execute(
            "UPDATE `respSurveyEco` "
                "SET `respSurveyEco`.`id_authorType`= 1 " 
            "WHERE `respSurveyEco`.`id_authorType`= ''"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `authorType`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add id_sr1 column to respSurveyEco and update it with id of table responseType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_sr1` SMALLINT UNSIGNED DEFAULT 0 AFTER `sr1`"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr1`= 1 "
            "WHERE `respSurveyEco`.`sr1`= ''"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr1`= 2 "
            "WHERE `respSurveyEco`.`sr1`= 'Oui'"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr1`= 3 "
            "WHERE `respSurveyEco`.`sr1`= 'Non'"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `sr1`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add id_sr2 column to respSurveyEco and update it with id of table responseType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_sr2` SMALLINT UNSIGNED DEFAULT 0 AFTER `sr2`"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr2`= 4 "
            "WHERE `respSurveyEco`.`sr2`= ''"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr2`= 5 "
            "WHERE `respSurveyEco`.`sr2`= 'Oui'"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr2`= 6 "
            "WHERE `respSurveyEco`.`sr2`= 'Non'"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `sr2`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()

    # ------------------------------------------------------------------------------------------------------------------
    # Add id_sr3 column to respSurveyEco and update it with id of table responseType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_sr3` SMALLINT UNSIGNED DEFAULT 0 AFTER `sr3`"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr3`= 7 "
            "WHERE `respSurveyEco`.`sr3`= ''"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr3`= 8 "
            "WHERE `respSurveyEco`.`sr3`= 'Oui'"
        )

        cursor.execute(
            "UPDATE `respSurveyEco`"
                "SET `respSurveyEco`.`id_sr3`= 9 "
            "WHERE `respSurveyEco`.`sr3`= 'Non'"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `sr3`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add id_sr4 column to respSurveyEco and update it with id of table responseType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_sr4` SMALLINT UNSIGNED DEFAULT 0 AFTER `sr4`"
        )

        cursor.execute(
            "UPDATE `responseType`, `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr4` = `responseType`.`id` " 
            "WHERE `responseType`.`label` = `respSurveyEco`.`sr4`"
        )

        cursor.execute(
            "UPDATE `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr4`= 10 " 
            "WHERE `respSurveyEco`.`sr4`= ''"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `sr4`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add id_sr5 column to respSurveyEco and update it with id of table responseType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_sr5` SMALLINT UNSIGNED DEFAULT 0 AFTER `sr5`"
        )

        cursor.execute(
            "UPDATE `responseType`, `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr5` = `responseType`.`id` " 
            "WHERE `responseType`.`label` = `respSurveyEco`.`sr5`"
        )

        cursor.execute(
            "UPDATE `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr5`= 14 " 
            "WHERE `respSurveyEco`.`sr5`= ''"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `sr5`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add id_sr6 column to respSurveyEco and update it with id of table responseType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_sr6` SMALLINT UNSIGNED DEFAULT 0 AFTER `sr6`"
        )

        cursor.execute(
            "UPDATE `responseType`, `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr6` = `responseType`.`id` " 
            "WHERE `responseType`.`label` = `respSurveyEco`.`sr6` "
        )

        cursor.execute(
            "UPDATE `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr6`= 19 " 
            "WHERE `respSurveyEco`.`sr6` = ''"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `sr6`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add id_sr7 column to respSurveyEco and update it with id of table responseType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `respSurveyEco` ADD COLUMN `id_sr7` SMALLINT UNSIGNED DEFAULT 0 AFTER `sr7`"
        )

        cursor.execute(
            "UPDATE `responseType`, `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr7` = `responseType`.`id` " 
            "WHERE `responseType`.`label` = `respSurveyEco`.`sr7`"
        )

        cursor.execute(
            "UPDATE `respSurveyEco` "
                "SET `respSurveyEco`.`id_sr7`= 84 " 
            "WHERE `respSurveyEco`.`sr7` = ''"
        )

        cursor.execute(
            "ALTER TABLE `respSurveyEco` DROP COLUMN `sr7`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()


    # ------------------------------------------------------------------------------------------------------------------
    # Add id_authorType column to author and update it with id of table authorType (FOREIGN KEY)

    counter += 1

    try:

        print("Step", counter, ": ", end = '')

        cursor.execute(
            "ALTER TABLE `author` ADD COLUMN `id_authorType` TINYINT UNSIGNED DEFAULT 0 AFTER `authorId`"
        )

        cursor.execute(
            "UPDATE `authorType`, `author`"
                "SET `author`.`id_authorType` = `authorType`.`id`" 
            "WHERE `authorType`.`label` = `author`.`authorType`"
        )

        cursor.execute(
            "ALTER TABLE `author` DROP COLUMN `authorType`"
        )

    except mysql.connector.Error as error:

        print("Something went wrong: {}".format(error))

    else:

        print("Ok.")
        cnx.commit()

    cursor.close()
    cnx.close()


# ------------------------------------------------------------------------------------------------------------------
# Test of the db_structure() function

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

    db_structure(settings, DB_NAME)


