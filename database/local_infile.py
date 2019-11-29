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
# Set the gobal variable 'local_infile' to "ON" or "OFF"

def local_infile(settings, li = 'ON'):

    """ Set the gobal variable 'local infile' to "ON" or "OFF".

        Keyword Arguments:\n
        settings {dict} -- connexion credentials of Mysql \n 
        li {str} -- value of 'local infile' (default: {"ON"})
    """

    try:

        cnx = mysql.connector.connect(**settings)
        cursor = cnx.cursor()
        cursor.execute("SHOW GLOBAL VARIABLES LIKE 'local_infile'")
        li_state = cursor.fetchone()
        li = li.upper()

        if li_state[1] == li:

            print("The gobal variable 'local_infile' is already set to {}".format(li_state[1]))
            pass

        else:

            cursor.execute("SET GLOBAL local_infile = {}".format(li))
            cursor.execute("SHOW GLOBAL VARIABLES LIKE 'local_infile'")
            li_new_state = cursor.fetchone()
            print("The gobal variable 'local_infile' now switches from {} to {}".format(li_state[1], li_new_state[1]))

    except mysql.connector.Error as error:

        print(error.msg)

    else:

        cursor.close()
        cnx.close()
        print("Everything is ok!")


# ------------------------------------------------------------------------------------------------------------------
# Test of the local_infile() function

if __name__ == "__main__":


    path_json_creds = "./.private/mysql_settings.json"
    mysql_settings = json.load(open(path_json_creds, "r"))

    settings = {
        "host": mysql_settings["myhost"],
        "user": mysql_settings["myuser"],
        "password": mysql_settings["mypassword"],
        "raise_on_warnings" : True
    }

    local_infile(settings, li = 'ON')





