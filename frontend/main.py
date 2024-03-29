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
from enum import Enum


#file paths
here = pathlib.Path(__file__)

project = here.parent.parent
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


#enumeration class for the Notenrechner settings
class ntr_config(Enum):
	full_local_csv = 0
	simplified_local_csv = 1
	full_local_DB = 2
	web = -1




# ** This read operation is not performed by the data_reader since it's the main read required for the app, data_reader will perform any requests that repeat

def loadsettings():

	#file paths
	here = pathlib.Path(__file__)

	project = here.parent.parent
	glue_layer = project / "glue"# /glue
	resources_dir = project / "frontend" / "resources"# /frontend/resources
	appdata = project / "appdata"

	settings_path = appdata / "notenrechnersettings.json"


	#extracting the settings from settings.json
	with open(settings_path,"r") as file:
		settings_data = file.read()
	settings = json.loads(settings_data)




	#getting the version details
	settings = settings.get("settings")
	version_info = settings.get("version")



	version_platform = version_info.get("platform")
	if "version_platform" not in st.session_state:
		st.session_state["version_platform"] = version_platform
	version_type = version_info.get("type")
	if "version_type" not in st.session_state:
		st.session_state["version_type"] = version_type
	version_version = version_info.get("version")
	if "version_version" not in st.session_state:
		st.session_state["version_version"] = version_version
	version_keyword = version_info.get("keyword")
	if "version_keyword" not in st.session_state:
		st.session_state["version_keyword"] = version_keyword
	version_full = version_info.get("full")
	if "version_full" not in st.session_state:
		st.session_state["version_full"] = version_full


	#getting the datasource details
	datasource = settings.get("datasource")

	datasource_location = datasource.get("location")
	if "datasource_location" not in st.session_state:
		st.session_state["datasource_location"] = datasource_location
	datasource_type = datasource.get("type")
	if "datasource_type" not in st.session_state:
		st.session_state["datasource_type"] = datasource_type
	datasource_size = datasource.get("size")
	if "datasource_size" not in st.session_state:
		st.session_state["datasource_size"] = datasource_size
	datasource_db_link = datasource.get("db_link")
	if "datasource_db_link" not in st.session_state:
		st.session_state["datasource_db_link"] = datasource_db_link


	datasource_db_type_info = datasource.get("db_type")
	if "datasource_db_type_info" not in st.session_state:
		st.session_state["datasource_db_type_info"] = datasource_db_type_info
	datasource_db_type_name = datasource_db_type_info.get("db_name")
	if "datasource_db_type_name" not in st.session_state:
		st.session_state["datasource_db_type_name"] = datasource_db_type_name
	datasource_db_type_username = datasource_db_type_info.get("db_username")
	if "datasource_db_type_username" not in st.session_state:
		st.session_state["datasource_db_type_username"] = datasource_db_type_username
	datasource_db_type_userpass = datasource_db_type_info.get("db_userpass")
	if "datasource_db_type_userpass" not in st.session_state:
		st.session_state["datasource_db_type_userpass"] = datasource_db_type_userpass
	datasource_db_type_specific = datasource_db_type_info.get("db_specific")
	if "datasource_db_type_specific" not in st.session_state:
		st.session_state["datasource_db_type_specific"] = datasource_db_type_specific


	#get the settings
	settings_internal = settings.get("settings")
	inpt_prefered = settings_internal.get("inpt_prefered")
	if "inpt_prefered" not in st.session_state:
		st.session_state["inpt_prefered"] = inpt_prefered
	theme = settings_internal.get("theme")
	if "theme" not in st.session_state:
		st.session_state["theme"] = theme


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
		"stunden.csv",
		"fach.csv"
	]


	# list of the files that make up all the data in the 'Konfiguration 1'
	config_1_files = ["noten_simplified.csv"]






	notenrechner_data_cofig = None
	notenrechner_datasource_arr = None
	notenrechner_data_path = None


	#defining files to access
	if datasource_location == "local":#local datasource
		if datasource_type == "appdata/user_data":#not a DB datasource
			if datasource_size == "full":#full config
				notenrechner_data_config = 1
				notenrechner_datasource_arr = konfig_0_files
				notenrechner_data_path = appdata_user_data
			elif datasource_size == "simplified":#simplified config
				notenrechner_data_config = 0
				notenrechner_datasource_arr = config_1_files
				notenrechner_data_path = appdata_user_data
			else:
				st.error("an notenrechner error occured: datasource_size is not valid")
		else:
			st.error("This is not configured yet: datasource_type is not valid.")# ? This error is only temporary and will get removed as soon as this is accessible


	else:
		if datasource_db_link:
			notenrechner_data_config = 2
		elif not datasource_db_link:
			notenrechner_data_config = "web"


	if "notenrechner_data_config" not in st.session_state:
		st.session_state["notenrechner_data_config"] = notenrechner_data_config
	if "notenrechner_datasource_arr" not in st.session_state:
		st.session_state["notenrechner_datasource_arr"] = notenrechner_datasource_arr
	if "notenrechner_data_path" not in st.session_state:
		st.session_state["notenrechner_data_path"] = notenrechner_data_path


	# loading security settings
	security_settings = settings.get("security")
	read_security_settings = security_settings.get("read")
	write_security_settings = security_settings.get("write")

	security_settings_dict = {}# creating a dedicated dictionairy to host the security settings


	write_check_dangerous = write_security_settings.get("check_dangerous")
	if "write_check_dangerous" not in security_settings_dict:
		security_settings_dict["write_check_dangerous"] = write_check_dangerous
	write_check_path_existence = write_security_settings.get("check_path_existence")
	if "write_check_path_existence" not in security_settings_dict:
		security_settings_dict["write_check_path_existence"] = write_check_path_existence
	write_check_if_data_already_present = write_security_settings.get("check_if_data_already_present")
	if "write_check_if_data_already_present":
		security_settings_dict["write_check_if_data_already_present"] = write_check_if_data_already_present
	write_check_indexing = write_security_settings.get("check_indexing")
	if "write_check_indexing" in security_settings_dict:
		security_settings_dict["write_check_indexing"] = write_check_indexing
	write_check_length = write_security_settings.get("check_length")
	if "write_check_length" in security_settings_dict:
		security_settings_dict["write_check_length"] = write_check_length
	write_enforce_required = write_security_settings.get("enforce_required")
	if "write_enforce_required" not in security_settings_dict:
		security_settings_dict["write_enforce_required"] = write_enforce_required
	write_check_general_format = write_security_settings.get("check_general_format")
	if "write_check_general_format" not in security_settings_dict:
		security_settings_dict["write_check_general_format"] = write_check_general_format


	read_check_dangerous = read_security_settings.get("check_dangerous")
	if "read_check_dangerous" in security_settings_dict:
		security_settings_dict["read_check_dangerous"] = read_check_dangerous
	read_check_path_existence = read_security_settings.get("check_path_existence")
	if "read_check_path_existence" not in security_settings_dict:
		security_settings_dict["read_check_path_existence"] = read_check_path_existence
	read_check_if_data_already_present = read_security_settings.get("check_if_data_already_present")
	if "read_check_if_data_already_present" not in security_settings_dict:
		security_settings_dict["read_check_if_data_already_present"] = read_check_if_data_already_present



	st.session_state["security-settings"] = security_settings_dict



	#list of keys that are likely to be null / None
	list_of_possible_null_keys = ["datasource_db_type_userpass","datasource_db_type_name","datasource_db_type_username"]
	#making sure all the required data is present
	for keys in st.session_state:
		if st.session_state[keys] == None and keys not in list_of_possible_null_keys:
			st.error("an critical error occured, please contact the developer with this information: key="+str(keys))





def init_data_management():
	data_core.init_data_core()


# ! export exception to different file and test
#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError
