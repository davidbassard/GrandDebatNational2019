# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------------
# Author: David Bassard
# Date: 15/11/2019
# ------------------------------------------------------------------------------------------------------------------

# Libraries

from time import time
from download import data_survey as ds
from download import data_contrib as dc
from download import data_zipcode as dz

# ------------------------------------------------------------------------------------------------------------------
# Timestamp

start_time = time()

# ------------------------------------------------------------------------------------------------------------------
# Choose the theme ("ecologique" or "depenses publiques" or "citoyennete" or "services publics")

theme = "ecologique"

# ------------------------------------------------------------------------------------------------------------------
# Choose the date of publication of the contributions

date = "2019-01-31"

# ------------------------------------------------------------------------------------------------------------------
# Download the data

ds.survey(theme_gdn = theme)

dc.contribution(theme_gdn = theme, file_date = date)

dz.zipcode()

# ------------------------------------------------------------------------------------------------------------------
# Timestamp

print("Run time: {} seconds".format(time() - start_time))
