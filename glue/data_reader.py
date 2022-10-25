# this module provides the functionality to read / write csv and json files
# this module only serves as an 'API' and does the checking if the data given makes sense


#importing modules
import pandas as pd
import os
import pathlib
import importlib.util
import sys
import json
import os.path


#paths
here = pathlib.Path(__file__)
glue_layer = here.parent


#importing local modules






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

    3. return success value
    """


    # 1. validate data

    














#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError