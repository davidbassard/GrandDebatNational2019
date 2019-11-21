# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

# Libraries
import os
import csv
import requests
from download import scrap_zipcode as sz

# ------------------------------------------------------------------------------------------------------------------

def zipcode():

    """ 
    Downloads the french zip code data in CSV format.
    """

    # Retrieves the URL content and writes a temporary CSV file "zipcode_tmp.csv"
    url = sz.url_zipcode()[1]
    response = requests.get(url = url)

    with open(os.path.join("./data/", "zipcode_tmp.csv"), mode = "wb") as f:
        f.write(response.content)
        f.close()

    # Opens the temporary CSV file "zipcode_tmp.csv" for reading
    f_tmp = open(os.path.join("./data/", "zipcode_tmp.csv"), mode = "r", encoding = "utf-8", newline = '\n')
    reader = csv.reader(f_tmp, delimiter=';')

    # Opens the CSV file "zipcode_raw.csv" for writing and replaces ';' by ',' and adds '"' to strings
    f_raw = open(os.path.join("./data/", "zipcode_raw.csv"), mode = "w", encoding = "utf-8", newline = '\n')
    writer = csv.writer(f_raw, delimiter =',', quotechar ='"', quoting = csv.QUOTE_ALL)
    writer.writerows(reader)

    # Closes all files and deletes the temporary file "zipcode_tmp.csv"
    f_tmp.close()
    os.remove(os.path.join("./data/", "zipcode_tmp.csv"))
    f_raw.close()

# ------------------------------------------------------------------------------------------------------------------

# Test of the url_gdn() function
if __name__ == "__main__":

    zipcode()


