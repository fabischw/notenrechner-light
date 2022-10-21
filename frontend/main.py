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


# ** This read operation is not performed by the data_reader since it's the main read required for the app, data_reader will perform any requests that repeat

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



# getting the file paths and datasource for current configuration



appdata_user_data = appdata / "user_data"#path to appdata/user_data

# list of the files that make up all the data in the 'Konfiguration 0'
konfig_0_files = [
	"arbeiten.csv",
	"kalender.csv",
	"kurs.csv",
	"kursschuelerref.csv",
	"kursschuleventsref.csv",
	"kursstundenref.csv",
	"lehrerfachref.csv",
	"noten.csv",
	"notenschuelerref.csv",
	"schueler.csv",
	"schulevents.csv",
	"stunden.csv"
]


# list of the files that make up all the data in the 'Konfiguration 1'
konfig_1_files = ["noten_simplified.csv"]



# ! setting these variables as global because they are required everywhere
# * I know it's bad practice to do this but I want these variables to easily be accessible everywhere without parsing them
global notenrechner_data_config
notenrechner_data_cofig = None
global notenrechner_datasource_arr
notenrechner_datasource_arr = None
global notenrechner_data_path
notenrechner_data_path = None


#defining files to access
if datasource_location == "local":#local datasource
	if datasource_type == "appdata/user_data":#not a DB datasource
		if datasource_size == "full":#full konfig
			notenrechner_data_cofig = 0
			notenrechner_datasource_arr = konfig_0_files
			notenrechner_data_path = appdata_user_data
		elif datasource_size == "simplified":#simplified konfig
			notenrechner_data_cofig = 1
			notenrechner_datasource_arr = konfig_1_files
			notenrechner_data_path = appdata_user_data
		else:
			st.error("an notenrechner error occured: datasource_size is not valid")
	else:
		st.error("This is not configured yet: datasource_type is not valid.")# ? This error is only temporary and will get removed as soon as this is accessible

else:
	st.error("This is not configured yet: datasource_location is not valid.")# ? This error is only temporary and will get removed as soon as this is accessible

# ! Maybe change the code above to something like this:
# if not datasource_location == "local":
# 	st.error("This is not configured yet: datasource_location is not valid.")
# else if not ...





# ! D.R.Y - Don't Repeat Yourself - Define the exception in a seperate file if you use it all over the project.
#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError
