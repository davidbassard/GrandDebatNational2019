# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

# Libraries
import os
import re
import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------------------------------------------------------------


def url_zipcode():

    """Retrieves the content of the web page https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/ 
    and scraping the download URLs of zip code.

    Returns:
        {list} -- List of URLs
        A backup file in csv format is created in the "data" folder and named "backup_url_zipcode"
    """

    # Creates the CSV file and opens it for writing
    folder_path = "./data/"
    backup_file_name = "backup_url_zipcode"
    file_extension = ".csv"
    backup_file = backup_file_name + file_extension

    url_zc = open(os.path.join(folder_path, backup_file), "w", encoding = "utf-8")
    url_zc.write('\"' + 'Reference' + '\"' + ',' + '\"' + 'Download URL'  + '\"' + '\n')

    # Retrieve the content of the web page
    web_adress = "https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/"

    repatriate_content = requests.get(str(web_adress))
    page_content = repatriate_content.content

    html_analysis = BeautifulSoup(page_content, features= 'html.parser')

    # Scraping the download URLs from the web page

    html_href_url = html_analysis.find_all("a", class_="btn btn-sm btn-primary")

    # List of URLs
    url_zipcode = []

    for link in html_href_url:

        get_url = link.get('href')

        if get_url != None:

            url_zipcode.append(get_url)

    # Scraping the URL's titles from the web page
    html_title = html_analysis.find_all("h4", class_="ellipsis")

    # List of Titles
    url_title = []

    for title in html_title:

        url_title.append(title.text)

    # Write the CSV file backup_url_zipcode.csv
    for i in range(len(url_zipcode)):

        url_zc.write('\"' + str(url_title[i]) + '\"' + ',')
        url_zc.write('\"' + str(url_zipcode[i]) + '\"')
        url_zc.write('\n')

    url_zc.close()

    return url_zipcode

# ------------------------------------------------------------------------------------------------------------------
# Test of the url_zipcode() function

if __name__ == "__main__":

    url_zipcode()
    url_zipcode()[1]