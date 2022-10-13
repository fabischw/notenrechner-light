# frontend appss

#installing dependencies
import PIL
from importlib_metadata import version
import streamlit as st
import frontend_funcs
import pathlib

__author__ = "fabischw"
__version__ = ("DEV","0.001","early-testing")


here = pathlib.Path(__file__)
here = here.parent

icon_path_jmp1 = here / 'resources'
icon_path_fnl = icon_path_jmp1 / 'page_icon.ico'


try:
    #set the page icon and title
    icon_load = PIL.Image.open(icon_path_fnl)
    st.set_page_config(page_title="Notenrechner light home",page_icon=icon_load)
except:
    st.write("unable to load icon.")



#sidebar
st.sidebar.success("Funktion / Modul wählen")

#title the page
st.title("Notenrechner light") 

st.markdown("Version",__version__[0]+__version__[1]+" ,",__version__[2])
st.markdown("## Dieses Projekt befindet sich noch in der Entwicklungsphases")




