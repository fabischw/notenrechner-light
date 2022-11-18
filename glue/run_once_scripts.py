"""
This file contains functions which are only ever required to run once (at max), this includes small scripts to init file structures and similar

This file's code is not well structured which I would like to apaologize for in advance ;D

These functions are not meant to be used by anyone who is not familar with the project structure !

# ! DO NOT USE THESE FUNCTIONS UNLESS YOU KNOW WHAT YOU ARE DOING !
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
    This function initializes the csv structure in the csv files to make sure read operations don't result in an exception
    """

    data = data_core.init_pd_dataframes()

    for keys, elements in data.items():
        path_to_element = user_data / f"{keys}.csv"
        print(f"Applying structure to {path_to_element}")
        elements.to_csv(path_to_element,sep=",")


def paste_file_specific_csv_structure(name):
    """
    This function does the same as the paste_csv_structure_to_files but for only one specific file 
    """

    data = data_core.init_pd_dataframes()

    specific_data = data.get(name)

    path_to_element = user_data / f"{name}.csv"
    print(f"Applying structure to {path_to_element}")
    specific_data.to_csv(path_to_element,sep=",")





def generate_userdata_structure():
    """
    This function intializes the essential NTR file structre
    (this does not include settings)
    # ! NOTE THAT THIS FUNCTION RESETS ALL PRESENT DATA
    """
    data = data_core.init_pd_dataframes()

    for keys in data:
        path = user_data / f"{keys}.csv"
        print(f"Resetting/creating file: {path}")

        with open(path,"w") as file:
            file.write("")
    

    paste_csv_structure_to_files()



def generate_default_tables():
    """
    this function generates the data for the tables that is normally already present unless the user data was reset
    # ! NOTE: this function will reset any present data for these tables:
        - fach
    """

    #fach table default values
    fname_arr = [
        "Mathematik",
        "Deutsch",
        "Englisch",
        "Naturwissenschaften",
        "Physik",
        "Sport",
        "Erdkunde",
        "Politik",
        "Geschichte",
        "Religion (katholisch)",
        "Religion (evangelisch)",
        "Chemie",
        "Bildende Kunst",
        "Seminarfach",
        "Informatik",
        "Spanisch",
        "Französisch",
        "Latein",
    ]


    fach_id_arr = [ i for i in range(1,len(fname_arr)+1)]
    cre_userid_arr = ["run_once_scripts" for i in range(len(fname_arr))]
    cre_date_arr = [datetime.datetime(2022,10,31) for i in range(len(fname_arr))]
    chg_userid_arr = [None for i in range(len(fname_arr))]
    chg_date_arr = [None for i in range(len(fname_arr))]


    fach_table = pd.DataFrame({
		"fach_id": fach_id_arr,
		"fname": fname_arr,
		"cre_userid": cre_userid_arr,
		"cre_date": cre_date_arr,
		"chg_userid": chg_userid_arr,
		"chg_date": chg_date_arr
	})




    filename = "fach.csv"
    path_to_file = user_data / filename

    print(f"writing to {path_to_file}")
    fach_table.to_csv(path_to_file, sep=",")








def main():
    """
    paste function you want to use below 
    """









if __name__ == "__main__":
    main()