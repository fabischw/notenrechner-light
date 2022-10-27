"""
This page has all the options / settings for the app, those are directly stored and updated in the appdata/notenrechnersettings.json

"""


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

settings_path = appdata / "notenrechnersettings.json"



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

number_inpt_choice = None



# function to update settings
def update_settings(type):
    if type == "number_input":#updating the number input
        if st.session_state.number_inpt_choice != st.session_state["inpt_prefered"] and number_inpt_choice != None:
            st.session_state["inpt_prefered"] = st.session_state.number_inpt_choice

            # loading the current settings
            with open(settings_path, "r")as file:
                setting_data = json.load(file)
            
            #changing the 'inpt_prefered'-setting
            setting_data["settings"]["settings"]["inpt_prefered"] = st.session_state.number_inpt_choice

            #saving the new settings as json into the old file -> overwriting old data
            with open(settings_path, "w") as file:
                file.write(json.dumps(setting_data, indent=4))

        # ? try to make this alert work so the user gets notified when the settings change and he gets actual feedback on the action
        #updt_msg = "alert('Einstellung aktualisiert')"
        #st.components.v1.html(f"<script>{updt_msg}</script>")





st.markdown("## Einstellungen")

# ** NOTE: for verious reasons the individual settings cannot be wrapped into functions

# setting for the default input method (slider vs number_input)
st.markdown("#### Zahlen Eingabe")

current_choice = None
choose_prefered_inpt_setting = True

#checking what the current choice is, this is done to set the default for the st.radio component
if st.session_state.get("inpt_prefered") == "slider":
    current_choice = 1
elif st.session_state.get("inpt_prefered") == "Eingabefeld":
    current_choice = 0
else:
    choose_prefered_inpt_setting = False
    st.markdown("Ein Fehler ist aufgetreten, Einstellungen zur Zeit nicht verfügbar")#


if choose_prefered_inpt_setting:#getting the user input
    number_inpt_choice = st.radio("Eingabe Möglichkeit wählen",("Eingabefeld","slider"),index=current_choice,on_change=update_settings, args=("number_input",),key="number_inpt_choice")

