"""
collection of functions to be used in the main app script
"""

# importing modules
import streamlit as st
import pathlib
import importlib
import sys



here = pathlib.Path(__file__).parent




project = here.parent#project folder
glue_layer = project / "glue"# /glue
frontend_layer = project / "frontend"
resources_dir = project / "frontend" / "resources"# /frontend/resources
appdata = project / "appdata"

settings_path = appdata / "user_data" / "notenrechnersettings.json"


#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core






main_spec=importlib.util.spec_from_file_location("main",frontend_layer / "main.py")
main = importlib.util.module_from_spec(main_spec)
main_spec.loader.exec_module(main)
sys.modules["main"] = main










# TODO export functions from main -> this


def load_custom_db_backends():
    """
    this function is supposed to get the required information to
    connect to a database depending on which databses are supported
    """



def init_phase():
    """
    This function does the initialization phase for reload on pages other than main
    """


    main.loadsettings()
    main.init_data_management()

