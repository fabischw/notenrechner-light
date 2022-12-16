"""
This file includes some utility functions which are being re-used often
"""
import streamlit as st
import pathlib
import importlib
import sys

here = pathlib.Path(__file__)
glue_layer = here.parent
project_layer = glue_layer.parent

frontend_layer = project_layer / "frontend"





def find_last_occurence_str(inptstr:str, target:str):
    """
    finds the last occurence of the substring 'target' in the 'inptstr'
    """
    current_match = 0

    for idx,chars in enumerate(inptstr):#looping trough the input string
        if chars == target:
            current_match = idx# setting the current match to be the current index if the char matches the target




def rerun_init_phase():
    """
    re-runs the init phase specified in frontend/frontend-funcs
    """

    frontend_funcs_spec=importlib.util.spec_from_file_location("frontend_funcs",frontend_layer / "frontend_funcs.py")
    frontend_funcs = importlib.util.module_from_spec(frontend_funcs_spec)
    frontend_funcs_spec.loader.exec_module(frontend_funcs)
    sys.modules["frontend_funcs"] = frontend_funcs

