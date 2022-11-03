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
import datetime


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



# TODO:
# 1. build the UI
# 2. give data to data_core:
#     -> check logic
#     -> save logic



# loading important data from the session state
inpt_preference = st.session_state["inpt_prefered"]
DATA = st.session_state["DATA"]

# getting the 'fach' data which is important for some selections
fach_data = DATA["fach"]
faecher = []# TODO read actual data 


def convert(list):
    return tuple(i for i in list)

faecher_tuple = convert(faecher)#converting feacher into a tuple


# code for adding data
with st.expander("Daten hinzufügen"):
    if st.session_state["notenrechner_data_config"] == 1:
        
        # code for adding a grade for config 1

        # NOTE: for this config there are many different tables which results in a big number of input forms

        # forms to build(german names because frontend is rendered in german):
        # - Noten -> noten.csv
        # - Arbeiten -> arbeiten.csv
        # - Kurs -> kurs.csv
        # - Lehrer -> lehrer.csv
        # - Schüler -> schueler.csv
        # - Stunden -> stunden.csv
        # - Schulevents -> schulevents.csv

        # - Kalender -> kalender.csv  # ** this is a special table since it's being generated automaticly (not yet implemented)
        # - Fach -> fach.csv # ** this table will be automaticly created and updated

        # REFs (these REF Tables will have to be dynamicly integrated into the form(via radio buttons or similar))

        # kursschuelerref (link student to a course)
        # kursschuleventsref (link a course to a school 'event')
        # kursstundenref (link a course to a time when that course is being offered)

        


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
                # form for the 'noten' input
                
                with st.form("Noten",clear_on_submit=True):
                    arbeit_type = ["(Arbeit / Kursarbeit)","(Test / Hausaufgabenüberprüfung / Mitarbeit)"]
                    kurs_tuple = ()# TODO: add way to query the kurs data
                    
                    if inpt_preference == "slider":# ** inpt as slider
                        score = st.slider("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                        arbeit_type = st.select_slider("Bitte Typ des Leistungsnachweises wählen",arbeit_type)
                        kommentar = st.text_area("Kommentar zur Note eingeben")# mark as not required field
                        doclink = st.text_area("Link zu Dokument einfügen")# mark as not required field
                        ndate = st.date_input("Datum, an welchem die Arbeit geschrieben wurde")
                        anz_year = st.number_input("Die wievielte Note ist das ?",min_value=0,max_value = 20,step=1,value = 0)
                        kurs = st.selectbox("Bitte Kurs auswählen",kurs_tuple)


                    elif inpt_preference == "Eingabefeld":# ** inpt as input fields
                        score = st.number_input("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                        arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",arbeit_type)
                        kommentar = st.text_area("Kommentar zur Note eingeben")# mark as not required field
                        doclink = st.text_area("Link zu Dokument einfügen")# mark as not required field
                        ndate = st.date_input("Datum, an welchem die Arbeit geschrieben wurde")
                        anz_year = st.number_input("Die wievielte Note ist das ?",min_value=0,max_value = 20,step=1,value = 0)
                        kurs = st.selectbox("Bitte Kurs auswählen",kurs_tuple)


                    noten = pd.DataFrame({
                        "noten_id": [],
                        "score":  [],
                        "ntype": [],
                        "kommentar": [],
                        "doclink": [],
                        "ndate": [],
                        "anz_year": [],
                        "kurs_id": [],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        
                        # give data to data_core
                        


            case "Schüler":
                
                # form for the 'schueler' input
                
                with st.form("Schüler",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        
                        # give data to data_core
                        


            case "Arbeiten":
                
                # form for the 'arbeiten' input
                
                with st.form("Arbeiten",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        
                        # give data to data_core
                        


            case "Kurse":
                
                # form for the 'kurs' input
                
                with st.form("Kurse",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        
                        # give data to data_core
                        


            case "Lehrer":
                
                # form for the 'lehrer' input
                
                with st.form("Lehrer",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        
                        # give data to data_core
                        


            case "Stunden":
                
                # form for the 'stunden' input
                
                with st.form("Stunden",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """


            case "Schulevents":
                
                # form for the 'schulevents' input
                
                with st.form("Schulevents",clear_on_submit=True):
                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        """
                        give data to data_core
                        """





    elif st.session_state["notenrechner_data_config"] == 0:
        
        # code for adding a grade for config 1

        # NOTE: for this config there is only a single table

        # forms to build:
        # Noten -> noten_simplified.csv
        

        with st.form("Noten",clear_on_submit=True):
            # ! NOTE: this part if not functional due to the facher variable not containing any data yet
            
            # form for the simplified Noten input
            
            arbeit_type = ["(Arbeit / Kursarbeit)","(Test / Hausaufgabenüberprüfung / Mitarbeit)"]

            if inpt_preference == "slider":# getting input for slider as prefered input
                score = st.slider("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                fach = st.select_slider("Bitte Fach auswählen",faecher)
                arbeit_type = st.select_slider("Bitte Typ des Leistungsnachweises wählen",arbeit_type)
                count = st.slider("Die wievielte Note ist das ?",min_value=0,max_value = 20,step=1,value = 0)
                
            elif inpt_preference == "Eingabefeld":# getting input for other input as prefered input
                score = st.number_input("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                fach = st.selectbox("Bitte Fach auswählen",faecher_tuple)
                arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",faecher_tuple)
                count = st.number_input("Die wievielte Note ist das ?",min_value=0,max_value = 20,step=1,value = 0)

            #setting creation/change user and data
            cre_userid = "notenanalyse"
            cre_date = datetime.date.today()
            chg_userid = None
            chg_date = None

            #creating a pandas Dataframe with current data to append to existing data later on
            current_df = pd.DataFrame({
                "score": [score],
                "fach": [fach],
                "type": [arbeit_type],
                "count": [count],
                "cre_userid": [cre_userid],
                "cre_date": [cre_date],
                "chg_userid": [chg_userid],
                "chg_date": [chg_date]
            })

            submitted = st.form_submit_button("Daten übernehmen")
            if submitted:
                
                # give data to data_core
                

