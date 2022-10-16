#importing modules
import streamlit as st
import PIL
import pathlib
import pandas as pd
import sys


#importing local modules
here = pathlib.Path(__file__)
glue_layer = here.parent.parent.parent / "glue"


data_core = glue_layer / "data_core.py"
sys.path.append(data_core)
import data_core # ! testing required !




#set the page icon
here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="Notenanalye",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Notenanalyse")
st.markdown("## Diese Funktion dient zur Analyse der Noten-Daten")

#starting up the datacore



if st.button("Rohdaten ansehen"):
    st.table()

