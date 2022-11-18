"""
This file is the generate-manager for the generate_test_data file
"""

import pathlib
import faker
import random
import streamlit as st
import PIL
import pathlib
import pandas as pd
import sys
import importlib.util
import datetime

#paths
here = pathlib.Path(__file__)
glue_layer = here.parent.parent
user_data_path = here.parent.parent.parent / "appdata" / "user_data"
project = here.parent.parent.parent
frontend_layer = project / "frontend"
test_gen_folder = glue_layer / "gluetest"
here = pathlib.Path(__file__)


#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core


def check_if_available(name):
    """
    function to check if a given choice is valid as the input
    """

    available = [
        "schule",
        "schueler",
        "lehrer",
        "kurs"
        ]

    if name not in available:
        return(False)
    else:
        return(True)



class AvailabilityError(Exception):
	def __init__(self,message="The given function is not avilable at this point in time."):
		self.message = message
		super().__init__(self.message)




class manager:
    """
    manager class for managing the write operations
    """
    def __init__(self,count,choice):
        self.__path = here
        self.__count = count
        self.__choice = choice

        if not check_if_available(self.__choice):
            raise AvailabilityError
        else:

            self.spec=importlib.util.spec_from_file_location(self.__choice,test_gen_folder / f"gen_{self.__choice}.py")
            self.module = importlib.util.module_from_spec(self.spec)
            self.spec.loader.exec_module(self.module)
            sys.modules["data_core"] = self.module

        self.gendata = None# data will be applied when the generate function is called

    def generate(self):
        """
        function to generate the data
        """
        self.gendata = self.module.generate_x_testdata(self.__count)


    def execute(self):
        """
        this function writes the data to the corresponding files using the data_reader
        """


        data_core.write_data


