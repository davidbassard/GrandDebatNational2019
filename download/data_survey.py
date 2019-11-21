# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

# Libraries
import os
import requests
from download import scrap_gdn as sc

# ------------------------------------------------------------------------------------------------------------------

def survey(theme_gdn = "ecologique"):

    """ Downloads the survey data for the chosen theme, only in CSV format.

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
    """

    url = sc.url_gdn(theme_gdn, "csv")["2019-04-08"]
    response = requests.get(url = url)

    with open(os.path.join("./data/", "survey_raw.csv"), mode = "wb") as f:
        f.write(response.content)
        f.close()

# ------------------------------------------------------------------------------------------------------------------

# Test of the url_gdn() function
if __name__ == "__main__":

    survey()

