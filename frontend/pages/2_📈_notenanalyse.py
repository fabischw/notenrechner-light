"""
This file contains the frontend functionality for the analyses of exam results
This includes:
- graphing the grades etc.
- reading / writing data
- exporting the data to 3rd party applications(ex. MS excel)
"""




#importing modules
import streamlit as st
import PIL
import pathlib
import pandas as pd
import sys
import importlib.util


#file paths
here = pathlib.Path(__file__)

glue_layer = here.parent.parent.parent / "glue"# /glue
resources_dir = here.parent.parent / 'resources'# /frontend/resources



#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core







#set the page icon
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="Notenanalye",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Notenanalyse")
st.markdown("## Diese Funktion dient zur Analyse der Noten-Daten")

#starting up the datacore


with st.expander("Rohdaten ansehen"):
    if st.session_state["notenrechner_data_config"] == 1:
        st.table(st.session_state["DATA"]["noten_simplified"])
    elif st.session_state["notenrechner_data_config"] == 0:
        st.table(st.session_state["DATA"]["noten"])

"""
# TODO:
1. build the UI
2. give data to data_core:
    -> check logic
    -> save logic
"""

# code for adding data
with st.expander("Daten hinzufügen"):
    if st.session_state["notenrechner_data_config"] == 1:
        """
        code for adding a grade for config 1

        NOTE: for this config there are many different tables which results in a big number of input forms

        forms to build(german names because frontend is rendered in german):
        - Noten -> noten.csv
        - Arbeiten -> arbeiten.csv
        - Kurs -> kurs.csv
        - Lehrer -> lehrer.csv
        - Schüler -> schueler.csv
        - Stunden -> stunden.csv
        - Schulevents -> schulevents.csv

        - Kalender -> kalender.csv  # ** this is a special table since it's being generated automaticly (not yet implemented)
        - Fach -> fach.csv # ** this table will be automaticly created and updated

        REFs (these REF Tables will have to be dynamicly integrated into the form(via radio buttons or similar))

        kursschuelerref (link student to a course)
        kursschuleventsref (link a course to a school 'event')
        kursstundenref (link a course to a time when that course is being offered)

        """


        #creating a radio button to choose a table to add data to
        form_choice = st.radio(
            "Tabelle für das Hinzufügen von Daten auswählen",
            (
                "Noten",
                "Schüler",
                "Arbeiten",
                "Kurse",
                "Lehrer",
                "Stunden",
                "Schulevents",
            ),
            index="Noten",
        )



        match form_choice:
            case "Noten":
                """
                form for the 'noten' input
                """
                with st.form("Noten",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """


            case "Schüler":
                """
                form for the 'schueler' input
                """
                with st.form("Schüler",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """


            case "Arbeiten":
                """
                form for the 'arbeiten' input
                """
                with st.form("Arbeiten",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """


            case "Kurse":
                """
                form for the 'kurs' input
                """
                with st.form("Kurse",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """


            case "Lehrer":
                """
                form for the 'lehrer' input
                """
                with st.form("Lehrer",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """


            case "Stunden":
                """
                form for the 'stunden' input
                """
                with st.form("Stunden",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """


            case "Schulevents":
                """
                form for the 'schulevents' input
                """
                with st.form("Schulevents",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """





    elif st.session_state["notenrechner_data_config"] == 0:
        """
        code for adding a grade for config 1

        NOTE: for this config there is only a single table

        forms to build:
        Noten -> noten_simplified.csv
        """

        with st.form("Noten",clear_on_submit=True):
            submitted = st.form_submit_button("Daten übernehmen")
            if submitted:
                """
                give data to data_core
                """

