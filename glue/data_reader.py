"""
this module provides the functionality to read / write csv and json files
this module only serves as an 'API' and does the checking if the data given makes sense
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


if "security_settings" not in st.session_state:
    #re-starting the data config using utility funcs
    utility_funcs.rerun_init_phase() ! recursion error

security_settings = st.session_state["security_settings"]
#loading the security settings
security_settings= {
        "write": {
            "check_dangerous": st.session_state.get("check_dangerous"),
            "check_path_existence": st.session_state.get("check_path_existence"),
            "check_if_data_already_present": st.session_state.get("check_if_data_already_present"),
            "check_indexing": st.session_state.get("check_indexing"),
            "check_length": st.session_state.get("check_length"),
            "enforce_required": st.session_state.get("enforce_required"),
            "check_general_format": st.session_state.get("check_general_format")
        },
        "read": {
            "check_dangerous": st.session_state.get("check_dangerous"),
            "check_path_existence": st.session_state.get("check_path_existence"),
            "check_if_data_already_present": st.session_state.get("check_if_data_already_present")
        }
}




def translate_plsql_dtype_to_py(inpt: str):
    """
    This function 'translates' PL/SQL datatypes to python datatypes

    return syntax:
    returns an array which has this syntax:
    [0]: corresponding datatype
    [1]: max_len
    [2]: REQ (true false ) -> None as default, true / false if 100% certain
    """

    result_arr = [None,None,None]
    # doing if / elif / else for *all possibly PL/SQL datatypes *(meaning all present formats in the notenrechner)

    if "NUMBER" in inpt or "number" in inpt:
        result_arr[0] = float
        max_len = inpt[inpt.find("NUMBER")+7:inpt.find(")")]
        result_arr[1] = float(max_len)
        # leaving REQ in current state since NUMBER does not pass a req 'parameter'

    elif "VARCHAR" in inpt: 
        result_arr[0] = str
        max_len = inpt[inpt.find("(")+1:inpt.find(")")]
        result_arr[1] = float(max_len)

        # find if its VARCHAR or VARCHAR2
        if inpt.find("VARCHAR2") > -1:
            result_arr[2] = False


    elif "DATE" in inpt:
        result_arr[0] = datetime.datetime

    else:
        return None


    return result_arr





def write_data(target: str,data):
    # ! requires testing
    """
    This function writes data to a file (pd dataframe -> csv file)

    params:
    - target: targetfile(full path)
    - data: data as a dictionairy

    For this there are multiple steps:

    1. validate data
    perform the checks which are proposed in the settings


    2. write data
        2.1 write the data to the target file

    3. return success value(True / False)
    """


    # pre-validate:
    # get the checks that have to be performed on data that is being saved
    security_settings_write = security_settings.get("write")

    if not security_settings:
        return False# failing write when the data can't get loaded in


    # 1. validate data:
    #perform the checks on the data that are enabled in the global settings






        data_copy = copy.deepcopy(data.values)# create a dictionairy with the data contained in the pandas dataframe




    # actually writing the data to the csv file
    try:
        pd.to_csv(data)#writing the dataframe to the csv file
        return True#returning success value
    except:#doing bare except to prevent file corruption
        return False



def read_data(target: str):
    # ! requires testing
    """
    This function reads data from a file (csv file -> pd dataframe)
    
    This action is performed on the initial page load or if any additional data is required or checks are performed
    """


    if ".csv" not in str(target): # returning False as success for non-csv files
        return False

    # TODO do security checks


    #attempting to load the data from the csv file
    try:
        data = pd.read_csv(target,sep=",")
    except FileNotFoundError:
        return False# return success

    return data












#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError