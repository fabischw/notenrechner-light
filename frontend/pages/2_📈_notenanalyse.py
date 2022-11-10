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


convert = lambda a: tuple(i for i in a)


faecher_tuple = convert(faecher)#converting feacher into a tuple
school_list = []# TODO get the list of schools a user has alread input

kurs_raw_data = DATA.get("kurs")
# TODO code comprehension function to transfer DATA from session state to local dict

kurse = {
    "kurs_name": [],
    "kurs_id": []
}


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

        # ? add functionality to import templates (for example teacher and school templates)




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
                "Schule",
                "Fächer"
            ),
            index=0,
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
                        kommentar = st.text_area("Kommentar zur Note eingeben")# TODO mark as not required field
                        doclink = st.text_area("Link zu Dokument einfügen")# TODO mark as not required field
                        ndate = st.date_input("Datum, an welchem die Arbeit geschrieben wurde")
                        anz_year = st.number_input("Die wievielte Note ist das ?",min_value=1,max_value = 20,step=1,value = 1)
                        kurs = st.selectbox("Bitte Kurs auswählen",kurs_tuple)


                    elif inpt_preference == "Eingabefeld":# ** inpt as input fields
                        score = st.number_input("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                        arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",arbeit_type)
                        kommentar = st.text_area("Kommentar zur Note eingeben")# TODO mark as not required field
                        doclink = st.text_area("Link zu Dokument einfügen")# TODO mark as not required field
                        ndate = st.date_input("Datum, an welchem die Arbeit geschrieben wurde")
                        anz_year = st.number_input("Die wievielte Note ist das ?",min_value=1,max_value = 20,step=1,value = 1)
                        kurs = st.selectbox("Bitte Kurs auswählen",kurs_tuple)

                    # get kurs_id from the selected kurs

                    # TODO add id capturing to automaticly get the noten_id
                    noten = pd.DataFrame({
                        "noten_id": [],
                        "score":  [score],
                        "ntype": [arbeit_type],
                        "kommentar": [kommentar],
                        "doclink": [doclink],
                        "ndate": [ndate],
                        "anz_year": [anz_year],
                        "kurs_id": [],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        # 



            case "Schüler":
                
                # form for the 'schueler' input
                
                with st.form("Schüler",clear_on_submit=True):

                    if inpt_preference == "slider":
                        vorname = st.text_input("Bitte Vorname des Schülers / der Schülerin eingeben")
                        nachname = st.text_input("Bitte Nachname des Schülers / der Schülerin eingeben")
                        zweiter_vorname = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")# TODO add check if email is valid
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen.",school_list)
                        stufe = st.slider("Bitte Klassenstufe auswählen",min_value=1,max_value=13,step=1)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        salter = st.slider("Alter in Jahren",min_value=1,max_value=99,step=1)
                        gebdatum = st.date_input("Geburtsdatum")
                        

                    elif inpt_preference == "Eingabefeld":
                        vorname = st.text_input("Bitte Vorname des Schülers / der Schülerin eingeben")
                        nachname = st.text_input("Bitte Nachname des Schülers / der Schülerin eingeben")
                        zweiter_vorname = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")# TODO add check if email is valid
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen.",school_list)
                        stufe = st.number_input("Bitte Klassenstufe auswählen",min_value=1,max_value=13,step=1)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        salter = st.number_input("Alter in Jahren",min_value=1,max_value=99,step=1)
                        gebdatum = st.date_input("Geburtsdatum")



                    schueler= pd.DataFrame({
                        "schueler_id": [],
                        "vorname": [vorname],
                        "nachname": [nachname],
                        "vorname2": [vorname2],
                        "email": [email],
                        "an_schule_seit": [an_schule_seit],
                        "schule": [schule],
                        "stufe": [stufe],
                        "adresse": [adresse],
                        "salter": [salter],
                        "gebdatum": [gebdatum],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })


                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        


            case "Arbeiten":
                
                # form for the 'arbeiten' input
                
                with st.form("Arbeiten",clear_on_submit=True):
                    if inpt_preference == "slider":
                        arbeit_type = st.select_slider("Bitte Typ des Leistungsnachweises wählen",arbeit_type)
                        kurs = st.selectbox("Kurs auswählen",kurse)# TODO get id by kurs
                        datum = st.date_input("Datum der Arbeit eingeben")
                        acount = st.slider("die wievielte Arbeit dieses Typs ist dies ?",min_value=1,max_value=20,step=1,value = 0)


                    elif inpt_preference == "Eingabefeld":
                        arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",arbeit_type)# TODO get id by kurs
                        kurs = st.selectbox("Kurs auswählen",kurse)# TODO get id by kurs
                        datum = st.date_input("Datum der Arbeit eingeben")




                    arbeiten = pd.DataFrame({
                        "arbeiten_id": [],
                        "atype": [],
                        "kurs_id": [],
                        "datum": [],
                        "acount": [],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        


            case "Kurse":
                
                # form for the 'kurs' input
                
                with st.form("Kurse",clear_on_submit=True):
                    if inpt_preference == "slider":
                        stufe = st.slider("Bitte Klassenstufe auswählen",min_value=1,max_value=13,step=1)
                        stundenzahl = st.slider("Anzahl der Wochenstunden",min_value=1,max_value=8,step=1,value=2)


                    elif inpt_preference == "Eingabefeld":
                        stufe = st.number_input("Bitte Klassenstufe auswählen",min_value=1,max_value=13,step=1)
                        stundenzahl = st.number_input("Anzahl der Wochenstunden",min_value=1,max_value=8,step=1,value=2)


                    kurs = pd.DataFrame({
                        "kurs_id": [],
                        "lehrer_id": [],
                        "fach_id": [],
                        "stundenzahl": [stundenzahl],
                        "stufe": [stufe],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        


            case "Lehrer":
                
                # form for the 'lehrer' input
                
                with st.form("Lehrer",clear_on_submit=True):
                    if inpt_preference == "slider":
                        vorname = st.text_input("Bitte Vorname des Schülers / der Schülerin eingeben")
                        nachname = st.text_input("Bitte Nachname des Schülers / der Schülerin eingeben")
                        zweiter_vorname = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")
                        kuerzel = st.text_input("Lehrer-Kürzel")
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen", school_list)
                        origin = st.multiselect("Schule auswählen", school_list)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        gebdatum = st.date_input("Geburtsdatum")



                    elif inpt_preference == "Eingabefeld":
                        vorname = st.text_input("Bitte Vorname des Schülers / der Schülerin eingeben")
                        nachname = st.text_input("Bitte Nachname des Schülers / der Schülerin eingeben")
                        zweiter_vorname = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")
                        kuerzel = st.text_input("Lehrer-Kürzel")
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen", school_list)
                        origin = st.multiselect("Schule auswählen", school_list)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        gebdatum = st.date_input("Geburtsdatum")


                    # check if email is valid:
                    # TODO add better email check using module later on
                    if "@" not in email:
                        st.warning("Email ungültig.",icon="⚠️")
                        



                    lehrer = pd.DataFrame({
                        "vorname": [vorname],
                        "nachname": [nachname],
                        "vorname2": [vorname2],
                        "email": [email],
                        "kuerzel": [kuerzel],
                        "an_schule_seit": [an_schule_seit],
                        "schule": [schule],
                        "origin": [origin],
                        "adresse": [adresse],
                        "gebdatum": [gebdatum],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        


            case "Stunden":
                
                # form for the 'stunden' input
                
                with st.form("Stunden",clear_on_submit=True):
                    if inpt_preference == "slider":
                        sday = st.selectbox("Wochentag auswählen",("Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samtag","Sonntag"))
                        scount = st.slider("Die wievielte Stunde ist dies an dem betreffenden Tag",min_value=1,max_value=10,step=1)

                    elif inpt_preference == "Eingabefeld":
                        sday = st.selectbox("Wochentag auswählen",("Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samtag","Sonntag"))
                        scount = st.number_input("Die wievielte Stunde ist dies an dem betreffenden Tag",min_value=1,max_value=10,step=1)


                    stunden = pd.DataFrame({
                        "stunen_id": [],
                        "sday": [sday],
                        "scount": [scount],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        


            case "Schulevents":
                
                # form for the 'schulevents' input
                
                with st.form("Schulevents",clear_on_submit=True):
                    if inpt_preference == "slider":
                        descript = st.text_area("Beschreibung des Events")
                        datum = st.date_input("Datum wählen")

                    elif inpt_preference == "Eingabefeld":
                        descript = st.text_area("Beschreibung des Events")
                        datum = st.date_input("Datum wählen")


                    schulevents = pd.DataFrame({
                        "schulevents_id": [],
                        "descript": [descript],
                        "datum": [datum],
                        "cre_userid": [],
                        "cre_date": [],
                        "chg_userid": [],
                        "chg_date": []
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        





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
                #fach = st.select_slider("Bitte Fach auswählen",faecher) # ** commented out to allow for easier testing
                arbeit_type = st.select_slider("Bitte Typ des Leistungsnachweises wählen",arbeit_type)
                count = st.slider("Die wievielte Note ist das ?",min_value=0,max_value = 20,step=1,value = 0)
                
            elif inpt_preference == "Eingabefeld":# getting input for other input as prefered input
                score = st.number_input("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                #fach = st.selectbox("Bitte Fach auswählen",faecher_tuple) # ** commented out to allow for easier testing
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
                #"fach": [fach], # ** commented out to allow for easier testing
                "type": [arbeit_type],
                "count": [count],
                "cre_userid": [cre_userid],
                "cre_date": [cre_date],
                "chg_userid": [chg_userid],
                "chg_date": [chg_date]
            })

            submitted = st.form_submit_button("Daten übernehmen")
            #if submitted:
                
                # give data to data_core
                

