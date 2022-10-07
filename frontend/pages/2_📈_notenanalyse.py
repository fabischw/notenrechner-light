import streamlit as st
import PIL


#initializing the page
icon_load = PIL.Image.open("../resources/page_icon.ico")# ! ERROR: file path incorrect
st.set_page_config(page_title="Notenanalyse",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Notenanalyse")