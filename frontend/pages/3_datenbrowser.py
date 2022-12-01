"""
This file contains the frontend functionality to browse the data stored in the local appdata/useer_data folder
"""



import streamlit as st
import PIL
import pathlib
import sys
import importlib.util


# collection of useful file paths
here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'
icon = resources_dir = resources_dir / 'page_icon.ico'
glue_layer = here.parent.parent.parent / "glue"# /glue
project = here.parent.parent.parent
frontend_layer = project / "frontend"



#importing frontend funcs
frontend_funcs_spec = importlib.util.spec_from_file_location("frontend_funcs",frontend_layer / "frontend_funcs.py")
frontend_funcs = importlib.util.module_from_spec(frontend_funcs_spec)
frontend_funcs_spec.loader.exec_module(frontend_funcs)
sys.modules["frontend_funcs"] = frontend_funcs


# logic to check if the page was being reload, if yes, initialize the app again
if "DATA" not in st.session_state:
    frontend_funcs.init_phase()#initializing the app, if page is reload


inpt_preference = st.session_state["inpt_prefered"]
DATA = st.session_state["DATA"]
additional_data = st.session_state["additional_data"] 


# loading the page icon
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="explore",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")

st.title("Datenbrowser")




st.markdown(" Diese Seite hilft dazu, die existierenden Daten anzusehen")# TODO fix bug where this markdown is shown as subheader
st.markdown(" Um Daten einzugeben, bitte besuchen Sie Seite 2 (Notenanalyse)")






with st.expander("Rohdaten ansehen"):
    if st.session_state["notenrechner_data_config"] == 1:
        # let user pick a table and check what data is currently present
        
        include_ref = st.radio("REF-Tabellen auch anzeigen ?",(
            "ja",
            "nein"
        ),
        index = 1
        )

        base_tables = (
            "kurs",
            "stunden",
            "fach",
            "schulevents",
            "arbeiten",
            "kalender",
            "schueler",
            "noten",
            "lehrer",
            "fach",
            "schule"
        )


        ref_tables = (
            "kursschuleventsref",
            "kursstundenref",
            "kursschuelerref",
            "lehrerfachref",
            "notenschuelerref"
        )


        if include_ref == "ja":
            tables = base_tables + ref_tables
        else:
            tables = base_tables

        tables_choice = st.multiselect("Tabelle zum Ansehen auswählen",tables)


        for elements in tables_choice:
            st.table(DATA.get(elements))




    elif st.session_state["notenrechner_data_config"] == 0:
        st.table(DATA.get("noten"))

