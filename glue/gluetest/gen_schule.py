"""
this file includes methods to generate test data for the 'schule'-table
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
    this function generates x rows of test data for the schule.csv file.
    """

    #dictionairy for saving the generated data
    data_dict = {
        "schule_id": [],
        "name": [],
        "stype": [],
        "adresse": [],
        "cre_userid": [],
        "cre_date": [],
        "chg_userid": [],
        "chg_date": []
    }





    for i in range(0,it_count):


        def generate_schule_table_row():

            def generate_school_type():# function to get a random school type


                # small selection of possible values for the school type
                stype = [
                "Gymnasium",
                "Gemeinschaftsschule",
                "Grundschule",
                "Universität",
                "duale Hochschule",
                "Fachhochschule"
                ]

                
                return(stype[random.randint(0,len(stype)-1)])




            def generate_random_school_name():# small helper function to generate the school type by combining other parameters
                name = fake.name()
                city = fake.city()
                stype = generate_school_type()

                schoolname = f"{name}-{stype} {city}"
                return(schoolname)

            adresse = fake.address()
            name = generate_random_school_name()
            stype = generate_random_school_name()

            return({
                "adresse": adresse,
                "name": name,
                "stype": stype
            })

        

        dataset = generate_schule_table_row()

        #writing the data into the dictionairy
        data_dict["schule_id"].append(data_core.find_current_id("schule")+1+i)
        data_dict["name"].append(dataset["name"])
        data_dict["stype"].append(dataset["stype"])
        data_dict["adresse"].append(dataset["adresse"])
        data_dict["cre_userid"].append("glue/gluetest/testgenerate")
        data_dict["cre_date"].append(datetime.date.today())
        data_dict["chg_userid"].append(None)
        data_dict["chg_date"].append(None)


    return(data_dict)








