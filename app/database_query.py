# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

# Libraries

import json
import mysql.connector
from mysql.connector import errorcode

# ------------------------------------------------------------------------------------------------------------------
# QUESTION 1
# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 1 : Global

def sr_eco1(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 1 : Global.

        Keyword Arguments:
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr1) AS reponse "
        "FROM respSurveyEco AS rs "
        "GROUP BY id_sr1 ORDER BY id_sr1"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response

# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 1 : na

def sr_econa1(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 1 when author type is not available.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr1) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 1 "
        "GROUP BY id_sr1 ORDER BY id_sr1"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 1 : citizen

def sr_ecocc1(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 1 when author is citizen.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr1) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 2 "
        "GROUP BY id_sr1 ORDER BY id_sr1"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 1 : Elected official and institution

def sr_ecoeei1(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 1 when author is an elected official or institution.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr1) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 3 "
        "GROUP BY id_sr1 ORDER BY id_sr1"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 1 : for-profit organization

def sr_ecoobl1(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 1 when author is for-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr1) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 4 "
        "GROUP BY id_sr1 ORDER BY id_sr1"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 1 : non-profit organization

def sr_ecoobnl1(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 1 when author is non-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr1) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 5 "
        "GROUP BY id_sr1 ORDER BY id_sr1"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# QUESTION 2
# ------------------------------------------------------------------------------------------------------------------
# Get responses to the question 2 : Global

def sr_eco2(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 2 : Global.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr2) AS reponse "
        "FROM respSurveyEco AS rs "
        "GROUP BY id_sr2 ORDER BY id_sr2"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 2 : na

def sr_econa2(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 2 when author type is not available.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr2) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 1 "
        "GROUP BY id_sr2 ORDER BY id_sr2"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 2 : citizen

def sr_ecocc2(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 2 when author is citizen.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr2) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 2 "
        "GROUP BY id_sr2 ORDER BY id_sr2"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 2 : Elected official and institution

def sr_ecoeei2(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 2 when author is an elected official or institution.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr2) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 3 "
        "GROUP BY id_sr2 ORDER BY id_sr2"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 2 : for-profit organization

def sr_ecoobl2(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 2 when author is for-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr2) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 4 "
        "GROUP BY id_sr2 ORDER BY id_sr2"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 2 : non-profit organization

def sr_ecoobnl2(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 2 when author is non-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr2) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 5 "
        "GROUP BY id_sr2 ORDER BY id_sr2 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# QUESTION 3
# ------------------------------------------------------------------------------------------------------------------
# Get responses to the question 3 : Global

def sr_eco3(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 3 : Global.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr3) AS reponse "
        "FROM respSurveyEco AS rs "
        "GROUP BY id_sr3 ORDER BY id_sr3 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 3 : na

def sr_econa3(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 3 when author type is not available.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr3) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 1 "
        "GROUP BY id_sr3 ORDER BY id_sr3 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 3 : citizen

def sr_ecocc3(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 3 when author is citizen.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr3) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 2 "
        "GROUP BY id_sr3 ORDER BY id_sr3 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response



# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 3 : Elected official and institution

def sr_ecoeei3(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 3 when author is an elected official or institution.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr3) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 3 "
        "GROUP BY id_sr3 ORDER BY id_sr3 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 3 : for-profit organization

def sr_ecoobl3(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 3 when author is for-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr3) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 4 "
        "GROUP BY id_sr3 ORDER BY id_sr3 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 3 : non-profit organization

def sr_ecoobnl3(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 3 when author is non-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr3) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 5 "
        "GROUP BY id_sr3 ORDER BY id_sr3 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# QUESTION 4
# ------------------------------------------------------------------------------------------------------------------
# Get responses to the question 4 : Global

def sr_eco4(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 4 : Global.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr4) AS reponse "
        "FROM respSurveyEco AS rs "
        "GROUP BY id_sr4 ORDER BY id_sr4 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 4 : na

def sr_econa4(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 4 when author type is not available.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr4) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 1 "
        "GROUP BY id_sr4 ORDER BY id_sr4 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 4 : citizen

def sr_ecocc4(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 4 when author is citizen.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr4) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 2 "
        "GROUP BY id_sr4 ORDER BY id_sr4 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 4 : Elected official and institution

def sr_ecoeei4(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 4 when author is an elected official or institution.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr4) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 3 "
        "GROUP BY id_sr4 ORDER BY id_sr4 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 4 : for-profit organization

def sr_ecoobl4(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 4 when author is for-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr4) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 4 "
        "GROUP BY id_sr4 ORDER BY id_sr4 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 4 : non-profit organization

def sr_ecoobnl4(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 4 when author is non-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr4) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 5 "
        "GROUP BY id_sr4 ORDER BY id_sr4 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# QUESTION 5
# ------------------------------------------------------------------------------------------------------------------
# Get responses to the question 5 : Global

def sr_eco5(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 5 : Global.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr5) AS reponse "
        "FROM respSurveyEco AS rs "
        "GROUP BY id_sr5 ORDER BY id_sr5 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response

# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 5 : na

def sr_econa5(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 5 when author type is not available.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr5) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 1 "
        "GROUP BY id_sr5 ORDER BY id_sr5 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 5 : citizen

def sr_ecocc5(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 5 when author is citizen.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr5) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 2 "
        "GROUP BY id_sr5 ORDER BY id_sr5 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 5 : Elected official and institution

def sr_ecoeei5(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 5 when author is an elected official or institution.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr5) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 3 "
        "GROUP BY id_sr5 ORDER BY id_sr5 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 5 : for-profit organization

def sr_ecoobl5(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 5 when author is for-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr5) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 4 "
        "GROUP BY id_sr5 ORDER BY id_sr5 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 5 : non-profit organization

def sr_ecoobnl5(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 5 when author is non-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr5) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 5 "
        "GROUP BY id_sr5 ORDER BY id_sr5 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# QUESTION 6
# ------------------------------------------------------------------------------------------------------------------
# Get responses to the question 6 : Global

def sr_eco6(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 6 : Global.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr6) AS reponse "
        "FROM respSurveyEco AS rs "
        "GROUP BY id_sr6 ORDER BY nb "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 6 : na

def sr_econa6(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 6 when author type is not available.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr6) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 1 "
        "GROUP BY id_sr6 ORDER BY nb"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 6 : citizen

def sr_ecocc6(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 6 when author is citizen.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr6) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 2 "
        "GROUP BY id_sr6 ORDER BY nb"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 6 : Elected official and institution

def sr_ecoeei6(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 6 when author is an elected official or institution.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr6) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 3 "
        "GROUP BY id_sr6 ORDER BY nb"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 6 : for-profit organization

def sr_ecoobl6(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 6 when author is for-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr6) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 4 "
        "GROUP BY id_sr6 ORDER BY nb"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 6 : non-profit organization

def sr_ecoobnl6(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 6 when author is non-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr6) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 5 "
        "GROUP BY id_sr6 ORDER BY nb"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# QUESTION 7
# ------------------------------------------------------------------------------------------------------------------
# Get responses to the question 7 : Global

def sr_eco7(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 7 : Global.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr7) AS reponse "
        "FROM respSurveyEco AS rs "
        "GROUP BY id_sr7 ORDER BY id_sr7 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 7 : na

def sr_econa7(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 7 when author type is not available.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr7) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 1 "
        "GROUP BY id_sr7 ORDER BY id_sr7 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 7 : citizen

def sr_ecocc7(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 7 when author is citizen.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr7) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 2 "
        "GROUP BY id_sr7 ORDER BY id_sr7 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 7 : Elected official and institution

def sr_ecoeei7(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 7 when author is an elected official or institution.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr7) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 3 "
        "GROUP BY id_sr7 ORDER BY id_sr7 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 7 : for-profit organization

def sr_ecoobl7(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 7 when author is for-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr7) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 4 "
        "GROUP BY id_sr7 ORDER BY id_sr7 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response



# ------------------------------------------------------------------------------------------------------------------
# Get response to the question 7 : non-profit organization

def sr_ecoobnl7(settings, DB_NAME = "gdn_db"):

    """ Get responses to the question 7 when author is non-profit organization.

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT count(*) AS nb, "
            "(SELECT label FROM responseType AS rt "
                "WHERE rt.id = rs.id_sr7) AS reponse "
        "FROM respSurveyEco AS rs "
        "WHERE id_authorType = 5 "
        "GROUP BY id_sr7 ORDER BY id_sr7 "
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response


# ------------------------------------------------------------------------------------------------------------------
# TIME
# ------------------------------------------------------------------------------------------------------------------
# Number of contributions over time : Global

def sr_ecotime(settings, DB_NAME = "gdn_db"):

    """ Number of contributions over time : Global.

        Keyword Arguments:
        settings {dict} -- connexion credentials of Mysql \n
        DB_NAME {str} -- name of the database - (default: {"gdn_db"})
    """

    # Connecton to database

    cnx = mysql.connector.connect(**settings)
    db_name = DB_NAME.upper()

    try:

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("USE {}".format(db_name))
    
    except mysql.connector.Error as error:

        print("Database {} does not exist.".format(db_name))
        print(error)

    else:

        print("Database {} is connected.".format(db_name))


    try:

        cursor.execute(
        "SELECT `date`, COUNT(*) AS nb FROM respSurveyEco "
        "GROUP BY `date` ORDER BY `date`"
        )

        response = cursor.fetchall()

    except mysql.connector.Error as error:

        print(error)

    else:

        cursor.close()
        cnx.close()

    return response

# ------------------------------------------------------------------------------------------------------------------
