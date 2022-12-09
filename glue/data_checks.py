"""
this file contains all the tests for the data that is being written / read
"""

#importing modules
import pandas as pd
import os
import pathlib
import importlib.util
import sys
import json
import os.path
import streamlit as st
import copy
import datetime
import utility_funcs as util_func



#paths
here = pathlib.Path(__file__)
glue_layer = here.parent


#importing local modules

# ** importing data_formats
data_formats_spec=importlib.util.spec_from_file_location("data_formats",glue_layer / "data_formats.py")
data_formats = importlib.util.module_from_spec(data_formats_spec)
data_formats_spec.loader.exec_module(data_formats)
sys.modules["data_formats"] = data_formats

# ** importing utility_funcs
utility_funcs_spec=importlib.util.spec_from_file_location("utility_funcs",glue_layer / "utility_funcs.py")
utility_funcs = importlib.util.module_from_spec(utility_funcs_spec)
utility_funcs_spec.loader.exec_module(utility_funcs)
sys.modules["utility_funcs"] = utility_funcs


# loading important data from the session state
DATA = st.session_state["DATA"]
additional_data = st.session_state["additional_data"]




def check_dangerous(inpt_str: str):
    """
    this function checks if an input is potentially dangerous

    PARAMS:
    inpt_Str: the string being checked
    """


def check_path_existence(inpt_path: str):
    """
    this function checks if a given absolute path exists

    PARAMS:
    inpt_path: the path that is being tested
    """


def check_if_data_already_present(data, targetfile):
    """
    this function checks if data supposed to get saved into a file is already present in that file

    PARAMS:
    data: the data that is being checked
    targetfile: the targetfile (absolute path) the data should be written to
    """


def check_indexing(data, targetfile):
    """
    check if the indexes are correct and continues

    PARAMS:
    data: the data that is being checked
    targetfile: the targetfile (absolute path) the data should be written to
    """


def check_length(data, targetfile):
    """
    check if the defined length from the PL/SQL database schemes are correct, if this is turnedof, maximum length can be ignored, makes connecting to DB impossible!

    PARAMS:
    data: the data that is being checked
    targetfile: the targetfile (absolute path) the data should be written to
    """


def enforce_required(data, targetfile):
    """
    enforce the required datatypes and similar, should always be on !

    PARAMS:
    data: the data that is being checked
    targetfile: the targetfile (absolute path) the data should be written to
    """


def check_general_format(data, targetfile):
    """
    check whether the general format of the data being written is correct, should always be on !

    PARAMS:
    data: the data that is being checked
    targetfile: the targetfile (absolute path) the data should be written to
    """


