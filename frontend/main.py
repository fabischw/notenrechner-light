"""
! Even tho this file is called main.py, it is not the actual main file
This file simply manages a lot of things which I do not want to do in home.py
when launching this dashboard you should lanch home.py, NOT this script
"""


#importing modules
from psutil import version_info
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

settings_path = appdata / "user_data" / "notenrechnersettings.json"



#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core




#extracting the settings from settings.json
settings = json.load(settings_path)


#getting the theme
theme = settings.get("theme")


#getting the version details
version_info = settings.get("version")

version_platform = version_info.get("platform")
version_type = version_info.get("type")
version_version = version_info.get("version")
version_keyword = version_info.get("keyword")
version_full = version_info.get("full")


#getting the datasource details
datasource = settings.get("datasource")

datasource_location = datasource.get("local")
datasource_type = datasource.get("type")
datasource_size = datasource.get("size")
datasource_db_link = datasource.get("db_link")

datasource_db_type_info = datasource.get("db_type")
datasource_db_type_name = datasource_db_type_info.get("db_name")
datasource_db_type_username = datasource_db_type_info.get("db_username")
datasource_db_type_userpass = datasource_db_type_info.get("db_userpass")
datasource_db_type_specific = datasource_db_type_info.get("db_specific")










#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError