#!/usr/bin/env /share/share1/share_dff/anaconda3/bin/python

'''
Author: Lira Mota, lmota20@gsb.columbia.edu
Data: 2018-06
Code:
    Import data from WRDS using wrsd package.
    Largely inspired by Tuomas  data import files.

Notes:
------
check_primary_key_integrity
download_compustat_fund
download_aco_pnfnd
download_crsp_sf
merge_compustat_crsp

Cheat Sheet for WRDS query submission:
--------------------------------------
db.describe_table(library='compm', table='aco_pnfnda')
db.get_table()
db.list_tables(library='compm')
db.engine()
db.insp()
db.raw_sql()
db.get_row_count()
db.list_libraries()
db.schema_perm()
'''

#%% Import
import os
import wrds
import datetime
import warnings
import pandas as pd
import numpy as np
import time
from time import strptime, strftime
from lm_pytools.utils.check_primary_key_integrity import check_primary_key_integrity



def use_computer(COMPUTER=None):
    """Set all global constant parameters
    according to the computer that is being used
    """
    global WORKDIR
    global DATADIR
    global PAPERDIR
    global SQL_HOST
    global SQL_PORT
    global SQL_USER
    global SQL_PASSWORD
    global SQL_SCHEMA

    if (COMPUTER == None):
        COMPUTER = str(input("""Please enter the name of computer where you are running this program.
            Options: "Lira", "Simon", "GRID"
            Computer Name: """))
        # Fallback Case: "GRID"

    if COMPUTER == "Lira":
        WORKDIR = "C:/Users/lmota20/src/dmrs_source/"
        DATADIR = "C:/Users/lmota20/Dropbox/Projects/Characteristics/Data/"
        PAPERDIR = "C:/Users/lmota20/Dropbox/Projects/Characteristics/PaperInputs"
    os.chdir(WORKDIR)
