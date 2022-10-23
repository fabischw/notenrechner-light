import streamlit as st
import PIL
import pathlib
import sys
import importlib.util
import json

#file paths
here = pathlib.Path(__file__)

project = here.parent.parent.parent
glue_layer = project / "glue"# /glue
resources_dir = project / "frontend" / "resources"# /frontend/resources
appdata = project / "appdata"
frontend_layer = project / "frontend"

settings_path = appdata / "user_data" / "notenrechnersettings.json"



#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core





#set the page icon
here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="Einstellungen",page_icon=icon_load)


#sidebar
st.sidebar.success("Funktion / Modul wählen")


# ! not functional yet
# function to update the settings
def update_settings(type):
    if type == "number_input":#updating the number input
        if number_inpt_choice != st.session_state["inpt_prefered"]:
            st.session_state["inpt_prefered"] = number_inpt_choice

            #change the setting and save it again
            with open(settings_path, "r")as file:
                setting_data = file.read()

            setting_data = json.loads(setting_data)
            
            setting_data["settigs"]["settings"]["inpt_prefered"] = number_inpt_choice

            with open(settings_path, "w") as file:
                file.write(json.dumps(setting_data))



st.markdown("## Einstellungen")


# Festlegen, ob der Nutzer die Eingabe mit slider oder mit Eingabefeld möchte
st.markdown("#### Zahlen Eingabe")


current_choice = None
choose_prefered_inpt_setting = True

if st.session_state.get("inpt_prefered") == "slider":
    current_choice = 1
elif st.session_state.get("inpt_prefered") == "inpt_field":
    current_choice = 0
else:
    choose_prefered_inpt_setting = False
    st.markdown(st.session_state.inpt_prefered)


if choose_prefered_inpt_setting:
    number_inpt_choice = st.radio("Eingabe Möglichkeit wählen",("Eingabefeld","slider"),index=current_choice,on_change=update_settings("number_input"))