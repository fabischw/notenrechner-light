"""
This file contains the frontend logic to do a database query for possible database connections (ORA, 'csv')
"""



import streamlit as st
import PIL
import pathlib
import sys
import importlib.util


# useful paths
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





# loading the page icon
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="data query",page_icon=icon_load)


#sidebar
st.sidebar.success("Funktion / Modul wählen")




st.markdown("## Database query")
