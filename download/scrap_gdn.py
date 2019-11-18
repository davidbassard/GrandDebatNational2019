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

def url_gdn(theme_gdn = "ecologique", file_format = "csv"):

    """Retrieve the content of the web page https://granddebat.fr/pages/donnees-ouvertes 
    and scraping the download URLs with the theme and file format as argument.

    Keyword Arguments:
        theme_gdn {str} -- theme of "Grand Débat National" - (default: {"ecologique"})
        There are themes: 
        - "LA_TRANSITION_ECOLOGIQUE",
        - "LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES",
        - "DEMOCRATIE_ET_CITOYENNETE",
        - "ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS"
        The last word in lowercase and without accent of each theme is sufficient 
        for scraping the corresponding URLs.
        eg.: "citoyennete" for the theme "DEMOCRATIE_ET_CITOYENNETE" 

        file_format {str} -- file format downloadable from the scraped URLs - (default: {"csv"})
        Two file formats available: "csv" and "json"

    Returns:
        {date : URL} -- dictionary of dates and URLs
        A backup file in csv format is created in the "data" folder containing all the srcaped URLs
    """

    # Creates the CSV file and opens it for writing
    folder_path = "./data/"
    backup_file_name = "backup_url"
    file_extension = ".csv"
    backup_file = backup_file_name + file_extension

    url_gdn = open(os.path.join(folder_path, backup_file), "w", encoding = "utf-8")
    url_gdn.write('"Date", "Download URL" \n')


    # Retrieve the content of the web page
    web_adress = "https://granddebat.fr/pages/donnees-ouvertes"

    repatriate_content = requests.get(str(web_adress))
    page_content = repatriate_content.content

    # Scraping the download URLs from the web page
    html_analysis = BeautifulSoup(page_content, features= 'html.parser')
    html_ref = theme_gdn.upper()
    html_ref_ext = "." + file_format
    html_href_url = html_analysis.find_all(href = re.compile(html_ref + html_ref_ext))

    # Dictionnary 
    dict_download_url = {}

    for i in range(len(html_href_url)):

        # Obtaining URLs in string format
        str_html_href_url = str(html_href_url[i])
        regex_str_html_href_url = re.search(r"\"[^\"\"]+\"" , str_html_href_url)
        regex_url =  regex_str_html_href_url.group()
        download_url = regex_url[1:-1]

        # Obtaining dates from URLs in string format
        regex_download_url = re.search(r"(\d\d\d\d-\d\d-\d\d)", download_url)
        date_download_url = regex_download_url.group()

        # Dictionary filling
        dict_download_url[date_download_url] = download_url

        # Write the CSV file DownloadUrl.csv
        url_gdn.write(date_download_url + ',')
        url_gdn.write(download_url)
        url_gdn.write('\n')

    url_gdn.close()
    return dict_download_url


# ------------------------------------------------------------------------------------------------------------------

# Test of the url_gdn() function
if __name__ == "__main__":

    url_gdn("publiques", "json")
    url_gdn("publiques", "json")["2019-04-08"]
