"""
This file contains functions which are only ever required to run once (at max), this includes small scripts to init file structures and similar

This file's code is not well structured which I would like to apaologize for in advance ;D

These functions are not meant to be used by anyone who is not familar with the project structure !
"""


import pandas as pd
import datetime
import streamlit as st
import sys
import pathlib
import importlib.util
import os




# ! importing local modules using the 'normal' import method as this file is not being imported as an module
import data_core

here = pathlib.Path(__file__)
project = here.parent.parent

appdata = project / "appdata"
user_data = appdata/ "user_data"



def paste_csv_structure_to_files():
    """
    This function initializes the csv structure in the csv files to make sure rea operations don't result in an exception
    """

    data = data_core.init_pd_dataframes()

    for keys, elements in data.items():
        path_to_element = user_data / f"{keys}.csv"
        elements.to_csv(path_to_element,sep=",")




paste_csv_structure_to_files()
