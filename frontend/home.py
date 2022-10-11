# frontend appss

#installing dependencies
import PIL
import streamlit as st
import frontend_funcs
import pathlib


here = pathlib.Path(__file__)

icon_path_jmp1 = here / 'resources'
icon_path_fnl = icon_path_jmp1 / 'page_icon.ico'

#set the page icon and title
icon_load = PIL.Image.open(icon_path_fnl)
st.set_page_config(page_title="Notenrechner light home",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")

#title the page
st.title("Notenrechner light") 




