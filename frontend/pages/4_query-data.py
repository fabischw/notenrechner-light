import streamlit as st
import PIL
import pathlib

#set the page icon
here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="data query",page_icon=icon_load)


#sidebar
st.sidebar.success("Funktion / Modul wählen")




st.markdown("## Database query")
st.markdown("- Diese Funktion erlaubt es, Anfragen direkt an die Datenbank zu schreiben")

db_request = st.text_input("Hier query eingeben [Oracle PL/SQL]: ")