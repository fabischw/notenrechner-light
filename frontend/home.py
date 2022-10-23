# frontend appss

#installing dependencies
import PIL
from importlib_metadata import version
import streamlit as st
import frontend_funcs
import pathlib
import importlib.util
import sys


__author__ = "fabischw"
__version__ = ("DEV","0.001","early-testing")

# ? reminder: maybe change variable name in future
here = pathlib.Path(__file__).parent

icon_path_jmp1 = here / 'resources'
icon_path_fnl = icon_path_jmp1 / 'page_icon.ico'



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

#importing main

main_spec=importlib.util.spec_from_file_location("main",frontend_layer / "main.py")
main = importlib.util.module_from_spec(main_spec)
main_spec.loader.exec_module(main)
sys.modules["main"] = main


main.loadsettings()




# loading page name and icon, since this isn't that important, let site continue to render if the build fails
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

version_msg = "Version "+str(__version__[0])+" "+str(__version__[1])+" , "+str(__version__[2])


st.markdown(version_msg)
st.markdown("Diese webversion bietet nicht die volle Funktionalität des Notenrechners. Für die Vollversion (ebenfalls kostenlos), gehen Sie auf den Link zum Projekt(siehe unten)")
st.markdown("## Dieses Projekt befindet sich noch in der Entwicklungsphase.")
st.markdown("- Link zu Github Projekt: https://github.com/fabischw/notenrechner-light")
