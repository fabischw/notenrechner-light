import streamlit as st
import PIL
import pathlib
import pandas as pd

#set the page icon
here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="Notenanalye",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Notenanalyse")
st.markdown("## Diese Funktion dient zur Analyse der Noten-Daten")

st.markdown("### Hier 'Noten.csv' hochladen.")

#noten_data = st.file_uploader("Notendaten hochladen",type="csv",help="Hier Noten.csv hinziehen, Wenn Sie dieses Programm noch nie genutzt haben, drücken Sie auf 'Datensatz erstellen'.")

