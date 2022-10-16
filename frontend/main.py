"""
! Even tho this file is called main.py, it is not the actual main file
This file simply manages a lot of things which I do not want to do in home.py
when launching this dashboard you should lanch home.py, NOT this script
"""


#importing modules
import streamlit as st
import PIL
import pathlib
import pandas as pd
import sys
import importlib.util
import json


#file paths
here = pathlib.Path(__file__)

project = here.parent.parent.parent
glue_layer = project / "glue"# /glue
resources_dir = project / "frontend" / "resources"# /frontend/resources
appdata = project / "appdata"

settings = appdata / "user_data" / "notenrechnersettings.json"



#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core







#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError