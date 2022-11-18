"""
This file generates test data for different backend files and provides an easy way to communicate with other important functions

As this file requires some session_stete data, there's no easy way around starting this file as a streamlit app
In building this as a webapp, it is also easier to help people debug their app as this file is delivered with every version

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
test_gen_folder = glue_layer / "gluetest"



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

#importing run_once_scripts
run_once_scripts_spec=importlib.util.spec_from_file_location("run_once_scripts",glue_layer / "run_once_scripts.py")
run_once_scripts = importlib.util.module_from_spec(run_once_scripts_spec)
run_once_scripts_spec.loader.exec_module(run_once_scripts)
sys.modules["run_once_scripts"] = run_once_scripts

#importing the generate manager
generatemanager_spec=importlib.util.spec_from_file_location("generatemanager",test_gen_folder / "generatemanager.py")
generatemanager = importlib.util.module_from_spec(generatemanager_spec)
generatemanager_spec.loader.exec_module(generatemanager)
sys.modules["generatemanager"] = generatemanager



# TODO remove and link via generatemanager
#importing generatemanager
gen_schule_spec=importlib.util.spec_from_file_location("gen_schule",test_gen_folder / "gen_schule.py")
gen_schule = importlib.util.module_from_spec(gen_schule_spec)
gen_schule_spec.loader.exec_module(gen_schule)
sys.modules["gen_schule"] = gen_schule




# logic to check if the page was being reload, if yes, initialize the app again
if "DATA" not in st.session_state:
    frontend_funcs.init_phase()#initializing the app, if page is reload



# app layout
st.title("Insert test data")
st.header("Test-Data-Manager")





# initializing the faker module
faker.Faker.seed(0)
fake = faker.Faker("de_DE")




st.markdown("### WICHTIG !")
st.markdown("Fast alle verfügbaren Funktionen löschen alle existenten Daten, wenn keine Angaben gemacht werden, gehen Sie davon aus, dass die Funktion die Daten zurücksetzt")


with st.expander("Zurücksetzen und ersetzen"):
    #this code provides functions for resetting data and similar actions
    choice = st.radio("Option wählen",(
        "generate_default_tables",
        "generate_userdata_structure",
        "paste_csv_structure_to_files",
        "paste_file_specific_csv_structure"
        ),
        index=0
    )

    submitted = st.button("Aktion ausführen")

    if submitted:

        match choice:#running the requested feature from the run_once_scripts
            case "generate_default_tables":
                run_once_scripts.generate_default_tables()
            case "generate_userdata_structure":
                run_once_scripts.generate_userdata_structure()
            case "paste_csv_structure_to_files":
                run_once_scripts.paste_csv_structure_to_files()
            case "paste_file_specific_csv_structure":
                filechoice = st.multiselect("table wählen",st.session_state["notenrechner_datasource_arr"])#running for a list of a files to reset
                if st.button("Aktion ausführen"):
                    for elements in filechoice:
                        run_once_scripts.paste_file_specific_csv_structure(elements)



#section for generating and saving testdata to work with later on
with st.expander("Testdaten generieren"):
    choice = st.radio("Datensatz wählen",(
        "schule",
        "schueler",
        "lehrer",
        "kurs"
        ),
        index=0
    )

    #getting the number of data rows being generated
    if st.session_state["inpt_prefered"] == "slider":
        number = st.slider("Anzahl der generierten Datensätze wählen.")
    elif st.session_state["inpt_prefered"] == "Eingabefeld":
        number = st.slider("Anzahl der generierten Datensätze wählen.",min_value=1,step=1,max_value=100)




    if st.button("Generieren",key="generate_btn"):#generating the data
        dataset = generatemanager.manager(number,choice)
        dataset.generate()
        st.markdown("data generated.")
        
    if st.button("Inspect",key="inspect_btn"):#giving the user the option to inspect the generated data
        st.markdown("Data shown below:")
        st.table(dataset.gendata)# TODO fix NameError: name 'dataset' is not defined



