"""
This file contains the frontend functionality for the analyses of exam results
This includes:
- graphing the grades etc.
- reading / writing data
- exporting the data to 3rd party applications(ex. MS excel)
"""




#importing modules
import streamlit as st
import PIL
import pathlib
import pandas as pd
import sys
import importlib.util


#file paths
here = pathlib.Path(__file__)

glue_layer = here.parent.parent.parent / "glue"# /glue
resources_dir = here.parent.parent / 'resources'# /frontend/resources



#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core







#set the page icon
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="Notenanalye",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Notenanalyse")
st.markdown("## Diese Funktion dient zur Analyse der Noten-Daten")

#starting up the datacore


# TODO: fix displaying data not working
with st.expander("Rohdaten ansehen"):
    if st.session_state["notenrechner_data_cofig"] == 1:
        st.table(st.session_state["DATA"]["noten_simplified"])
    elif st.session_state["notenrechner_data_config"] == 0:
        st.table(st.session_state["DATA"]["noten"])
