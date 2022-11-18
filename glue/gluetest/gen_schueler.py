"""
this file includes methods to generate test data for the 'schueler'-table
"""




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



#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core

# importing frontend funcs
frontend_funcs_spec = importlib.util.spec_from_file_location("frontend_funcs",frontend_layer / "frontend_funcs.py")
frontend_funcs = importlib.util.module_from_spec(frontend_funcs_spec)
frontend_funcs_spec.loader.exec_module(frontend_funcs)
sys.modules["frontend_funcs"] = frontend_funcs



# logic to check if the page was being reload, if yes, initialize the app again
if "DATA" not in st.session_state:
    frontend_funcs.init_phase()#initializing the app, if page is reload





# initializing the faker module
faker.Faker.seed(0)
fake = faker.Faker("de_DE")



def generate_x_testdata(it_count: int):#explanation for name: generating x rows of testdata
    """
    this function generates x rows of test data for the schueler.csv file.
    """

    #dictionairy for saving the generated data
    data_dict= pd.DataFrame({
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




    for i in range(0,it_count):

        #generating all the necessary data
        vorname = fake.first_name()
        nachname = fake.last_name()
        vorname2 = fake.first_name()
        email = fake.email()
        an_schule_seit = fake.date()
        schule_id = random.randint(1,data_core.find_current_id("schule")+1+i)
        stufe = random.randint(1,13)
        adresse = fake.address()
        salter = random.randint(6,18)
        gebdatum = fake.datum()


        #writing the data into the dictionairy
        data_dict["schueler_id"].append(data_core.find_current_id("schueler")+1+i)
        data_dict["vorname"].append(vorname)
        data_dict["nachname"].append(nachname)
        data_dict["vorname2"].append(vorname2)
        data_dict["email"].append(email)
        data_dict["an_schule_seit"].append(an_schule_seit)
        data_dict["schule_id"].append(schule_id)
        data_dict["stufe"].append(stufe)
        data_dict["adresse"].append(adresse)
        data_dict["salter"].append(salter)
        data_dict["gebdatum"].append(gebdatum)
        data_dict["cre_userid"].append("glue/gluetest/testgenerate")
        data_dict["cre_date"].append(datetime.date.today())
        data_dict["chg_userid"].append(None)
        data_dict["chg_date"].append(None)


    return(data_dict)








