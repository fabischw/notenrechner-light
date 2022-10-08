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


#content
st.title("einfache Funktionen")

#Zeugnisdurchschnittsrechner
st.markdown("### Zeugnisdurchschnittsrechner")
st.markdown(" -Diese Funktion rechnet den Zeugnisnotendurchschnitt basierend auf eingegebenen Noten aus")



#Note für Zeugnis vorberechnen
st.markdown("### Note für Zeugnis vorberechnen")


#Prozent in Arbeit ausrechnen
st.markdown("### Prozent in Arbeit ausrechnen")



#Punktezähler für Arbeit
st.markdown("### Punktezähler für Arbeit")

