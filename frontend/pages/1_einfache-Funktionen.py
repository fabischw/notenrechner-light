import streamlit as st
import PIL
import pathlib


here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'

icon = resources_dir = resources_dir / 'page_icon.ico'



#initializing the page
icon_load = PIL.Image.open(icon)
st.set_page_config(page_title="Funktionen",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")