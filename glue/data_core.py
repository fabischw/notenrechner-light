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
import pandas as pd
import os
import pathlib
import importlib.util
import sys


#paths
here = pathlib.Path(__file__)
glue_layer = here.parent


#importing local modules

data_objcts_spec=importlib.util.spec_from_file_location("data_objcts",glue_layer / "data_objcts.py")
data_objcts = importlib.util.module_from_spec(data_objcts_spec)
data_objcts_spec.loader.exec_module(data_objcts)
sys.modules["data_objcts"] = data_objcts




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
		"schule": [],
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
		"schule": [],
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





def load_data_from_csv(inpt_csv):
	data = pd.read_csv(inpt_csv)

	table_type = pd.inpt_csv[:inpt_csv.find(".")]#loading the table into a 


	def appenddata(data):#append the read data to existing 
		#appending the read data into the tables
		# ! This will throw an error if the functions are not called in correct order
		if table_type == "noten":
			noten.append(data)
		elif table_type == "schueler":
			schueler.append(data)
		elif table_type == "kurs":
			kurs.append(data)
		elif table_type == "stunden":
			stunden.append(data)
		elif table_type == "schulevents":
			schulevents.append(data)
		elif table_type == "arbeiten":
			arbeiten.append(data)
		elif table_type == "kalender":
			kalender.append(data)
		elif table_type == "kursschuleventsref":
			kursschuleventsref.append(data)
		elif table_type == "kursstundenref":
			kursstundenref.append(data)
		elif table_type == "kursschuelerref":
			kursschuelerref.append(data)
		elif table_type == "lehrerfachref":
			lehrerfachref.append(data)
		elif table_type == "notenschuelerref":
			notenschuelerref.append(data)


	appenddata(table_type)#append the data onto the pandas DataFrame





#main function
def main():
	# ! Do not change the call order
	init_pd_dataframes()#generates the initial pandas dataframes


	"""
	generate path to local csvs, check if they exist or not
	if path does not exist -> app is running in konf 0
	if it does exist -> user is running in konf 1 / 2

	this can also be done reading from the settgs json but this technic is mroe reliable
	"""

	here = pathlib.Path(__file__)
	user_data_path = here.parent / "appdata" / "user_data"

	testcsv = user_data_path / "noten.csv"

	if os.path.exists(testcsv):
		konf = 1
	else:
		konf = 0






#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError

