import streamlit as st
import PIL

#initializing the page
icon_load = PIL.Image.open("../resources/page_icon.ico")# ! ERROR: file path incorrect
st.set_page_config(page_title="data query",page_icon=icon_load)


#sidebar
st.sidebar.success("Funktion / Modul wählen")




st.markdown("## Database query")
st.markdown("- Diese Funktion erlaubt es, Anfragen direkt an die Datenbank zu schreiben")

db_request = st.text_input("Hier query eingeben [Oracle PL/SQL]: ")