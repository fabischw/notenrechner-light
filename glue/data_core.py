#notenrechner project data core
"""
This file contains all the code required to handling and managing the data for the notenrechner.
This includes loading from either a local machine database, a cloud service or drag n' drop csv files
"""



"""
Currently supported database source options:

planned / in development:
- local oracle DB (21c XE, notenrechner layout)
- csv drag n' drop
"""
#importing modules
from tkinter import E
import pandas as pd
import os
import pathlib
import importlib.util
import sys
from enum import Enum
import streamlit as st
import json






#paths
here = pathlib.Path(__file__)
glue_layer = here.parent
user_data_path = here.parent.parent / "appdata" / "user_data"
project = here.parent.parent


#importing local modules
# ** importing data_objcts
data_objcts_spec=importlib.util.spec_from_file_location("data_objcts",glue_layer / "data_objcts.py")
data_objcts = importlib.util.module_from_spec(data_objcts_spec)
data_objcts_spec.loader.exec_module(data_objcts)
sys.modules["data_objcts"] = data_objcts

# ** importing data_reader
data_reader_spec=importlib.util.spec_from_file_location("data_reader",glue_layer / "data_reader.py")
data_reader = importlib.util.module_from_spec(data_reader_spec)
data_reader_spec.loader.exec_module(data_reader)
sys.modules["data_reader"] = data_reader

# ** importing data_formats
data_formats_spec=importlib.util.spec_from_file_location("data_formats",glue_layer / "data_formats.py")
data_formats = importlib.util.module_from_spec(data_formats_spec)
data_formats_spec.loader.exec_module(data_formats)
sys.modules["data_formats"] = data_formats




#function for creating the initial dataframes, data can later be appended
def init_pd_dataframes():
	noten = pd.DataFrame({
		"noten_id": [],
		"score":  [],
		"ntype": [],
		"kommentar": [],
		"doclink": [],
		"ndate": [],
		"anz_year": [],
		"kurs_id": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	schueler= pd.DataFrame({
		"schueler_id": [],
		"vorname": [],
		"nachname": [],
		"vorname2": [],
		"email": [],
		"an_schule_seit": [],
		"schule_id": [],
		"stufe": [],
		"adresse": [],
		"salter": [],
		"gebdatum": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	kurs = pd.DataFrame({
		"kurs_id": [],
		"lehrer_id": [],
		"fach_id": [],
		"stundenzahl": [],
		"stufe": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	stunden = pd.DataFrame({
		"stunden_id": [],
		"sday": [],
		"scount": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	lehrer = pd.DataFrame({
		"vorname": [],
		"nachname": [],
		"vorname2": [],
		"email": [],
		"kuerzel": [],
		"an_schule_seit": [],
		"schule_id": [],
		"origin": [],
		"adresse": [],
		"gebdatum": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	stunden = pd.DataFrame({
		"stunen_id": [],
		"sday": [],
		"scount": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	schulevents = pd.DataFrame({
		"schulevents_id": [],
		"descript": [],
		"datum": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	arbeiten = pd.DataFrame({
		"arbeiten_id": [],
		"atype": [],
		"kurs_id": [],
		"datum": [],
		"acount": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	kalender = pd.DataFrame({
		"kalender_id": [],
		"events_descript": [],
		"events_date": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	kursschuleventsref = pd.DataFrame({
		"kursschuleventsref_id": [],
		"kurs_id": [],
		"schulevents_id": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	kursstundenref = pd.DataFrame({
		"kursstundenref_id": [],
		"kurs_id": [],
		"stunden_id": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})


	fach = pd.DataFrame({
		"fach_id": [],
		"fname": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})

	schule = pd.DataFrame({
		"schule_id": [],
		"name": [],
		"stype": [],
		"adresse": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})


	kursschuelerref = pd.DataFrame({
		"kursschuelerref_id": [],
		"kurs_id": [],
		"schueler_id": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	lehrerfachref = pd.DataFrame({
		"lehrerfachref_id": [],
		"lehrer_id": [],
		"fach_id": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	notenschuelerref = pd.DataFrame({
		"notenschuelerref_id": [],
		"noten_id": [],
		"schueler_id": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})


	noten_simplified = pd.DataFrame({
		"score": [],
		"fach": [],
		"type": [],
		"count": [],
		"cre_userid": [],
		"cre_date": [],
		"chg_userid": [],
		"chg_date": []
	})



	# ** dictionairy with all the objects, keeping arr for debugging reasons but commentd out because it's not required
	# dataframes_arr = [noten,schueler,kurs,stunden,lehrer,schulevents,arbeiten,kalender,kursschuleventsref,kursstundenref,kursschuelerref,lehrerfachref,notenschuelerref]
	dataframes_dict = {
		"noten": noten,
		"schueler": schueler,
		"kurs": kurs,
		"stunden": stunden,
		"lehrer": lehrer,
		"schulevents": schulevents,
		"arbeiten": arbeiten,
		"kalender": kalender,
		"fach": fach,
		"schule": schule,
		"kursschuleventsref": kursschuleventsref,
		"kursstundenref": kursstundenref,
		"kursschuelerref": kursschuelerref,
		"lehrerfachref": lehrerfachref,
		"notenschuelerref": notenschuelerref,
		"noten_simplified": noten_simplified
	}


	return dataframes_dict




def do_initial_read(datasources):
	"""
	This function does the initial data_read, which does the following steps:

	- read data from csv's according to the datasources param which should contain a list of files containing the data
	- merge the data onto the existing pd_dataframes
	"""

	store_data = st.session_state["DATA"]# data currently stored in session_state



	# load data from all the csv's
	for elements in datasources:
		# getting the data as a pd DataFrame

		#turn datasources into actual file paths
		elements_path = user_data_path / elements

		data = data_reader.read_data(elements_path)


		current_element = elements[:elements.find(".csv")]# current element (serves as key in store_data)


		merge = pd.concat([data,store_data[current_element]])# merging the two pandas DataFrames

		st.session_state["DATA"][current_element] = merge# storing the new data in session_state




def init_additional_data():
	"""
	function to load additional data which can be set in the settings
	"""

	eingabeoptionen_path = project / "appdata" / "eingabeoptionen.json"
	with open(eingabeoptionen_path,"r") as file:
		eingabeoptionen = file.read()
	eingabeoptionen = json.loads(eingabeoptionen)

	eingabeoptionen_options = eingabeoptionen.get("options")
	
	leistungsnachweisformen = eingabeoptionen_options.get("leistungsnachweisformen")
	schulformen = eingabeoptionen_options.get("schulformen")


	additional_data = {
		"leistungsnachweisformen": leistungsnachweisformen,
		"schulformen": schulformen
	}






	st.session_state["additional_data"] = additional_data





class NTR_CONFIGURATION_ERROR(Exception):
	def __init__(self,message="There was an critical error with the Notenrechenr configuration. try to change the configuration and contact the developer team."):
		self.message = message
		super().__init__(self.message)



class NTR_READ_ERROR(Exception):
	def __init__(self,message="There was an critical error when trying to read data."):
		self.message = message
		super().__init__(self.message)



def init_data_core():
	"""
	this function initilizes the data_core, this includes

	- creating the pd dataframes
	- reading the avilable data

	"""
	# ! Do not change the call order, can lead to problems
	DATA = init_pd_dataframes()  # generates the initial pandas dataframes
	if "DATA" not in st.session_state: # saving data in the session state, this will be all the data the app works with !
		st.session_state["DATA"] = DATA
	
	here = pathlib.Path(__file__)
	user_data_path = here.parent.parent / "appdata" / "user_data"

	# checking if all the files required for the configuration is valid

	# ! fix elements only being file names, NOT paths -> error is raised
	for elements in st.session_state["notenrechner_datasource_arr"]:
		current_element_path = user_data_path / elements
		if not os.path.exists(current_element_path):
			raise NTR_CONFIGURATION_ERROR

	# ** doing initial data read
	do_initial_read(st.session_state["notenrechner_datasource_arr"])

	init_additional_data()



# TODO add functionality for reading, writing -> file read, file write, file modify(append/remove)


def find_current_id(tablename: str):
	"""
	this function checks for a given table name, what the currently highest id is to find out which id is the next on ewhich has to be applied
	"""

	DATA = st.session_state["DATA"]

	return len(DATA.get(tablename).index)




def write_data_csv(target,data):
	"""
	This function writes a pandas dataframe to a csv file
	# ! NOTE: this function is not eant for appending new user data but rather writing entire blocks of data
	# ! this means that this function will overwrite any present data

	parameters:

	target: the file the data gets written to
	data: the pandas dataframe that is supposed to be written

	# TODO:
		- add the syntax checking etc.
	"""

	




def read_data_csv(targetfile,add_to):
	"""
	This function reads data from a csv file and returns the data as a pandas dataframe
	# ! this function does not replace the initial read but rather serves as a method to check data writing success and similar

	parameters:
	target: the file that gets read
	add_to: the dataframe to add data to
	"""

	data = data_reader.read_data(targetfile)

	if not data:
		raise NTR_READ_ERROR
	else:
		pass

	if add_to:
		final = pd.concat([add_to,data])
		return final



def append_data(target, data):
	"""
	This function appends some data to a csv file

	parameters:
	target: the file that is being appended to


	# TODO:
		- add the syntax checking etc.
	"""



def remove_data():
	"""
	this function removes data from a csv file
	"""






#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)


#checking if file is being run as main
if __name__ == "__main__":
	raise  FileExecutionError

