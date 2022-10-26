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


#paths
here = pathlib.Path(__file__)
glue_layer = here.parent


#importing local modules

# ** importing data_formats
data_formats_spec=importlib.util.spec_from_file_location("data_formats",glue_layer / "data_formats.py")
data_formats = importlib.util.module_from_spec(data_formats_spec)
data_formats_spec.loader.exec_module(data_formats)
sys.modules["data_formats"] = data_formats







# function to validate data (general validation)
def check_data(data,sec_priority):
    # ! requires testing
    """
    This function checks an input if it makes sense and is not dangerous before writing it to the csv / json files
    """
    # smaller functions
    def is_dangerous(data_inpt):
        with open("list_of_naughty_strings.txt","r") as sec_list:
            line = sec_list.readline()
            if data_inpt.find(line) > -1:
                return(True)
        return(False)


    def basic_type_check(data,sec_priority):
        if type(data) == int:
            return("input is safe")
        elif type(data) == str:
            #if priority is 1, check for string in the list of naughty strings
            if sec_priority == 1:
                dangerous = is_dangerous(data)
                if dangerous:
                    return("input is potentially dangerous")
                else:
                    return("input is safe")




    if type(data) == int or type(data) == str:
        finding = basic_type_check(data,sec_priority)
        return(finding)


    elif type(data) == list:
        finding = 0
        for elements in list:
            finding_current = basic_type_check
            if finding_current == "input is potentially dangerous":
                finding +=1
        if finding == 0:
            return("inpt is safe")
        elif finding > 0:
            return(f"there are {finding} problems in your data")






def read_data(target: str):
    # ! requires testing
    """
    This function reads data from a file (csv file -> pd dataframe)
    
    This action is performed on the initial page load or if any additional data is required or checks are performed
    """


    if not (target.find(".csv") > -1): # returning False as success for non-csv files
        return(False)

    #attempting to load the data from the csv file
    try:
        data = pd.DataFrame.from_csv(target,sep=",")
    except FileNotFoundError:
        return(False)# return success

    return(data)





def validate_inpt_13(data_dict: dict, comp_arr: list, req_arr: list, data_type: list, extra_conditions: list):
    # ! requires testing
    """
    This function is a component of the write_data function (step 1.3)

    It takes a dictionairy and an  comparison array(comp_arr) which contains strings as well as a required array (req_arr)  which also contains strings


    The function checks if all the strings in the comp_arr are keys in the data_dict and if the length of all the keys is the same and if the values in the array for the keys in req_arr are not None

    If the case given above is True, the function returns True, otherwise it returns False


    inpt_explanation:
    data_dict: a dictionairy containing keys, assigned to each key is an array
    comp_arr: a array containing all the keys which should be present in the data_dict
    req_arr: a array containing all the keys whose assigned array should always have a value instead of None
    data_type: datatype at each column (array), must be 'synced' with comp_arr

    extra_conditions: contains special conditions, must be 'synced' with comp_arr, condition representation as an array itself # ? not implemented yet


    conditions:
    1. length same as all others
    2. if in req_arr values in arr not None
    3. key in the comp_arr
    4. datatype correct (=> data_type)
    5. check if all elements in comp_arr are in the dict (if 3 is true and lengths same this is true)


    Y. check if extra_condition is met # ? not implemented yet



    """


    #variable for saving the length of the data arrays
    ex_len = data_dict[comp_arr[0]]# any key can picked here since the length should always be the same

    # ** condition 5:
    if len(data_dict) != len(comp_arr):
        return(False)


    for keys, values in data_dict.items:

        # ** condition 1:
        if len(values) != ex_len:
            return(False)

        # ** condition 2:
        if keys in req_arr:
            for elements in values:
                if elements == None:
                    return(False)

        # ** condition 3:
        if keys not in comp_arr:
            return False


        # function to find the index of the current key in the comp_arr:
        current_key_idx = None
        for idx,elements in enumerate(comp_arr):
            if elements == keys:
                current_key_idx = idx


        # ** condition 4:
        for elements in values:
            if type(elements) != type(data_type[current_key_idx]):
                return(False)








def write_data(target: str,data):
    # ! requires testing
    """
    This function writes data to a file (pd dataframe -> csv file)

    For this there are multiple steps:

    1. validate data
        1.1 check if the currently running version is permitted to export data to a file (ex. web version is not permitted to save data to a file)
        1.2 ensure the data is not dangerous
        1.3 check if the data format is valid (ex. writing data with missing arguments to a data file)

    2. write data
        2.1 write the data to the target file

    3. return success value(True / False)
    """


    # 1. validate data


    # 1.1



    # 1.3


    match target[:target.find(".csv")]:
        case "noten":

            data_copy = copy.deepcopy(data.values)# create a dictionairy with the data contained in the pandas dataframe
            # ** pass the data_dictionairy to the validate_inpt_13 function

    














#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError