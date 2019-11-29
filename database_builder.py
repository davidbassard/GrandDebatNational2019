# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

# Libraries

import os
import json
import mysql.connector
from time import time
from mysql.connector import errorcode
from database import create_db as cdb
from database import create_table as ct
from database import local_infile as li
from database import loading_table as lt
from database import db_structuring as dbs
from database import add_fk_idx as afi

# ------------------------------------------------------------------------------------------------------------------
# Timestamp

start_time = time()

# ------------------------------------------------------------------------------------------------------------------
# Settings

mysql_settings = json.load(open("./.private/mysql_settings.json", "r"))

settings = {
    "host": mysql_settings["myhost"],
	"user": mysql_settings["myuser"],
	"password": mysql_settings["mypassword"],
    "raise_on_warnings" : True
}

# ------------------------------------------------------------------------------------------------------------------
# Creating datavase "gdn_db"

cdb.create_database(settings, DB_NAME = "gdn_db")

# ------------------------------------------------------------------------------------------------------------------
# Creating tables of the database

ct.create_table(settings, DB_NAME = "gdn_db")

# ------------------------------------------------------------------------------------------------------------------
# Loading tables with data from CSV file

li.local_infile(settings, li = 'ON')

lt.load_data(settings, TABLE_NAME = "tmp_survey", DB_NAME = "gdn_db", display_limit = 10)

lt.load_data(settings, TABLE_NAME = "tmp_contribution", DB_NAME = "gdn_db", display_limit = 10)

lt.load_data(settings, TABLE_NAME = "tmp_zipcode", DB_NAME = "gdn_db", display_limit = 10)

li.local_infile(settings, li = 'OFF')

# ------------------------------------------------------------------------------------------------------------------
# Database structuring

dbs.db_structure(settings, DB_NAME = "gdn_db")

# ------------------------------------------------------------------------------------------------------------------
# Adding foreign keys and indexes

afi.fk_idx(settings, DB_NAME = "gdn_db")

# ------------------------------------------------------------------------------------------------------------------
# Timestamp

print("Run time: {} seconds".format(time() - start_time))


