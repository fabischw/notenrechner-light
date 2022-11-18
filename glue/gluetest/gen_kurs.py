"""
this file includes methods to generate test data for the 'kurs'-table
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
    this function generates x rows of test data for the kurs.csv file.
    # ! KEEP IN MIDN THIS FUNCTION WILL CHANGE THE FILES !!!
    """

    #dictionairy for saving the generated data
    data_dict = pd.DataFrame({
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




    for i in range(0,it_count):#generating data rows

        lehrer_id = random.randint(1,data_core.find_current_id("lehrer")+1+i)
        fach_id = random.randint(1,data_core.find_current_id("fach")+1+i)
        stundenzahl = random.randint(1,6)
        stufe = random.randint(1,13)


        data_dict["kurs_id"].append(data_core.find_current_id("kurs")+1+i)
        data_dict["lehrer_id"].append(lehrer_id)
        data_dict["fach_id"].append(fach_id)
        data_dict["stundenzahl"].append(stundenzahl)
        data_dict["stufe"].append(stufe)
        data_dict["cre_userid"].append("glue/gluetest/testgenerate")
        data_dict["cre_date"].append(datetime.date.today())
        data_dict["chg_userid"].append(None)
        data_dict["chg_date"].append(None)


    return(data_dict)








