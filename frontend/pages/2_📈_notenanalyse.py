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
project = here.parent.parent.parent
frontend_layer = project / "frontend"



#importing local modules

#importing data core
data_core_spec=importlib.util.spec_from_file_location("data_core",glue_layer / "data_core.py")
data_core = importlib.util.module_from_spec(data_core_spec)
data_core_spec.loader.exec_module(data_core)
sys.modules["data_core"] = data_core

#importing frontend funcs
frontend_funcs_spec = importlib.util.spec_from_file_location("frontend_funcs",frontend_layer / "frontend_funcs.py")
frontend_funcs = importlib.util.module_from_spec(frontend_funcs_spec)
frontend_funcs_spec.loader.exec_module(frontend_funcs)
sys.modules["frontend_funcs"] = frontend_funcs


# logic to check if the page was being reload, if yes, initialize the app again
if "DATA" not in st.session_state:
    frontend_funcs.init_phase()#initializing the app, if page is reload


#set the page icon
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="Notenanalye",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Notenanalyse")
st.markdown("## Diese Funktion dient zur Analyse der Noten-Daten")





# TODO id's work:
    # kurs -> change tables

# TODO done id's:
    # fach


# TODO other:
    # add lehrer to kurs section
    # check which square brackets can be changed to .get

# loading important data from the session state
inpt_preference = st.session_state["inpt_prefered"]
DATA = st.session_state["DATA"]
additional_data = st.session_state["additional_data"] 



convert = lambda a: tuple(i for i in a)# function to convert arr into a tuple


school_data = DATA.get("schule")

# create a dictionairy where the key is the schule_id
if not school_data.empty:
    schule_exists = True
    schule_data = school_data["schule_id","name"]
    schule_display = school_data[["name"]]
    schule_datadict = {}# get id from name
    i = 0
    for elements in schule_data["name"]:
        schule_datadict[elements] = int(schule_data["schule_id"][i])
        i += 1

    schule_id_dict = {}# get name from id
    i = 0
    for elements in schule_data["schule_id"]:
        schule_id_dict[elements] = str(schule_data["name"][i])

elif school_data.empty:
    schule_exists = False# making sure other programs can check if this empty or not
    schule_display = []




# ** getting the 'fach' data which is important for some selections
fach_data = DATA["fach"]
fname_data = fach_data[["fach_id","fname"]]
fach_display = fach_data[["fname"]]# list of items to be displayed

# building a dictionairy with the fname as the key and id as the corresponding value
fach_datadict = {}
i = 0
for elements in fname_data["fname"]:# get id by name
    fach_datadict[elements] = int(fname_data["fach_id"][i])
    i += 1

fach_id_dict = {}
i= 0
for elements in fname_data["fach_id"]:# get name by id
    fach_id_dict[elements] = fname_data["fname"][i]
    i += 1


# creating the lehrer display data and ids to use for other inputs
lehrer_data = DATA["lehrer"]

if not lehrer_data.empty:# checking if the dataframe is empty or not
    # ? don't have to check for schule-table existence since user can't create a lehrer without first having generated a schule for it
    lehrer_exists = True

    lehrer_datadict = {}
    lehrer_display = []
    lehrer_id_dict = {}
    for i in range(0,len(lehrer_data)-1):#creating a lehrer 'name' which is generated by first name, last name and school
        lehrer_vorname = lehrer_data["vorname"][i]
        lehrer_nachname = lehrer_data["nachname"][i]
        lehrer_schule_id = lehrer_data["schule_id"][i]
        lehrer_schule = schule_id_dict[str(lehrer_schule_id)]
        lehrer_datadict[f"{lehrer_nachname}, {lehrer_vorname}, {lehrer_schule}"] = lehrer_data["lehrer_id"][i]# get the id by generated 'name'

        lehrer_display.append(f"{lehrer_nachname}, {lehrer_vorname}, {lehrer_schule}")#displayarr

        lehrer_id_dict[lehrer_data["lehrer_id"][i]] = f"{lehrer_nachname}, {lehrer_vorname}, {lehrer_schule}"

else:
    lehrer_exists = False
    lehrer_display = []



kurs_data = DATA.get("kurs")
if not kurs_data.empty:
    kurs_exists = True

    kurs_datadict = {}
    kurs_display = []
    kurs_id_dict = {}
    for i in range(0,len(kurs_data)-1):#creating a kurs 'name' which is generated by first name, last name and school
        kurs_lehrerid = kurs_data["lehrer_id"][i]
        kurs_lehrerdescript = lehrer_id_dict[kurs_lehrerid]# description of the teacher
        kurs_fachid = kurs_data["fach_id"][i]
        kurs_fachname = fach_id_dict[kurs_fachid]
        kurs_stufe = kurs_data["stufe"][i]
        kurs_stundenzahl = kurs_data["stundenzahl"][i]
        kurs_datadict[f"{kurs_fachname}; {kurs_stufe}; {kurs_lehrerdescript}"] = kurs_data["kurs_id"][i]# get the id by generated 'name'

        kurs_display.append(f"{kurs_fachname}; {kurs_stufe}; {kurs_lehrerdescript}")#displayarr

        kurs_id_dict[kurs_data["kurs_id"][i]] = f"{kurs_fachname}; {kurs_stufe}; {kurs_lehrerdescript}"

else:
    kurs_exists = False
    kurs_display = []






# ** getting additional data
schultypes = additional_data.get("schulformen")
leistungsnachweisformen = additional_data.get("leistungsnachweisformen")








with st.expander("Rohdaten ansehen"):
    if st.session_state["notenrechner_data_config"] == 1:
        st.table(DATA.get("noten_simplified"))
    elif st.session_state["notenrechner_data_config"] == 0:
        st.table(DATA.get("noten"))






# code for adding data
with st.expander("Daten-Eingabe"):
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

        # explanation of dataframe params:
        # "ASIGN_FROM_CURRENT": means that the value has to be calculated from exisiting information
        # ! "MISSING": a placeholder argument used during testing / dev, REMOVE / FIX for prod




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
                    kurs_tuple = ()# TODO: add way to query the kurs data
                    
                    if inpt_preference == "slider":# ** inpt as slider
                        score = st.slider("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                        arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",leistungsnachweisformen)# ** make user aware he can change the presets
                        kommentar = st.text_area("Kommentar zur Note eingeben")# TODO mark as not required field
                        doclink = st.text_area("Link zu Dokument einfügen")# TODO mark as not required field
                        ndate = st.date_input("Datum, an welchem die Arbeit geschrieben wurde")
                        anz_year = st.number_input("Die wievielte Note ist das ?",min_value=1,max_value = 20,step=1,value = 1)
                        kurs = st.selectbox("Bitte Kurs auswählen",kurs_display)


                    elif inpt_preference == "Eingabefeld":# ** inpt as input fields
                        score = st.number_input("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                        arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",leistungsnachweisformen)# ** make user aware he can change the presets
                        kommentar = st.text_area("Kommentar zur Note eingeben")# TODO mark as not required field
                        doclink = st.text_area("Link zu Dokument einfügen")# TODO mark as not required field
                        ndate = st.date_input("Datum, an welchem die Arbeit geschrieben wurde")
                        anz_year = st.number_input("Die wievielte Note ist das ?",min_value=1,max_value = 20,step=1,value = 1)
                        kurs = st.selectbox("Bitte Kurs auswählen",kurs_display)

                    if not kurs_exists:
                        submitblock = True

                    else:
                        kurs_id = kurs_datadict[kurs]

                        # TODO add id capturing to automaticly get the noten_id
                        noten = pd.DataFrame({
                            "noten_id": ["ASIGN_FROM_CURRENT"],
                            "score":  [score],
                            "ntype": [arbeit_type],
                            "kommentar": [kommentar],
                            "doclink": [doclink],
                            "ndate": [ndate],
                            "anz_year": [anz_year],
                            "kurs_id": [kurs_id],
                            "cre_userid": ["frontend-page2-userinpt"],
                            "cre_date": [datetime.date.today()],
                            "chg_userid": [None],
                            "chg_date": [None]
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
                        vorname2 = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")# TODO add check if email is valid
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen.",schule_display)
                        stufe = st.slider("Bitte Klassenstufe auswählen",min_value=1,max_value=13,step=1)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        salter = st.slider("Alter in Jahren",min_value=1,max_value=99,step=1)
                        gebdatum = st.date_input("Geburtsdatum")
                        

                    elif inpt_preference == "Eingabefeld":
                        vorname = st.text_input("Bitte Vorname des Schülers / der Schülerin eingeben")
                        nachname = st.text_input("Bitte Nachname des Schülers / der Schülerin eingeben")
                        vorname2 = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")# TODO add check if email is valid
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen.",schule_display)
                        stufe = st.number_input("Bitte Klassenstufe auswählen",min_value=1,max_value=13,step=1)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        salter = st.number_input("Alter in Jahren",min_value=1,max_value=99,step=1)
                        gebdatum = st.date_input("Geburtsdatum")


                    if not schule_exists:
                        submitblock = True#setting a var to stop submitting the answer


                    else:
                        schule_id = schule_datadict[schule]
                        submitblock = False


                        schueler= pd.DataFrame({
                            "schueler_id": ["ASIGN_FROM_CURRENT"],
                            "vorname": [vorname],
                            "nachname": [nachname],
                            "vorname2": [vorname2],
                            "email": [email],
                            "an_schule_seit": [an_schule_seit],
                            "schule_id": [schule_id],
                            "stufe": [stufe],
                            "adresse": [adresse],
                            "salter": [salter],
                            "gebdatum": [gebdatum],
                            "cre_userid": ["frontend-page2-userinpt"],
                            "cre_date": [datetime.date.today()],
                            "chg_userid": [None],
                            "chg_date": [None]
                        })


                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        if submitblock:
                            st.warning("Bitte alle benötigten Felder ausfüllen.")
                        
                        # give data to data_core
                        


            case "Arbeiten":
                
                # form for the 'arbeiten' input
                
                with st.form("Arbeiten",clear_on_submit=True):
                    if inpt_preference == "slider":
                        arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",leistungsnachweisformen)
                        kurs = st.selectbox("Kurs auswählen",kurs_display)
                        datum = st.date_input("Datum der Arbeit eingeben")
                        acount = st.slider("die wievielte Arbeit dieses Typs ist dies ?",min_value=1,max_value=20,step=1,value = 0)


                    elif inpt_preference == "Eingabefeld":
                        arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",leistungsnachweisformen)
                        kurs = st.selectbox("Kurs auswählen",kurs_display)
                        datum = st.date_input("Datum der Arbeit eingeben")
                        acount = st.number_input("die wievielte Arbeit dieses Typs ist dies ?",min_value=1,max_value=20,step=1,value = 0)

                    if not kurs_exists:
                        submitblock = True

                    else:
                        submitblock = False
                        kurs_id = kurs_datadict[kurs]


                        arbeiten = pd.DataFrame({
                            "arbeiten_id": ["ASIGN_FROM_CURRENT"],
                            "atype": [arbeit_type],
                            "kurs_id": [kurs_id],
                            "datum": [datum],
                            "acount": [acount],
                            "cre_userid": ["frontend-page2-userinpt"],
                            "cre_date": [datetime.date.today()],
                            "chg_userid": [None],
                            "chg_date": [None]
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
                        fach = st.selectbox("Fach auswählen",fach_display)
                        lehrer = st.selectbox("Lehrer auswählen",lehrer_display)


                    elif inpt_preference == "Eingabefeld":
                        stufe = st.number_input("Bitte Klassenstufe auswählen",min_value=1,max_value=13,step=1)
                        stundenzahl = st.number_input("Anzahl der Wochenstunden",min_value=1,max_value=8,step=1,value=2)
                        fach = st.selectbox("Fach auswählen",fach_display)
                        lehrer = st.selectbox("Lehrer auswählen",lehrer_display)


                    #getting the id from the fname_data
                    fach_id = fach_datadict[fach]

                    if not lehrer_exists:
                        submitblock = True

                    else:
                        submitblock = False
                        lehrer_id = lehrer_datadict[lehrer]

                        kurs = pd.DataFrame({
                            "kurs_id": ["ASIGN_FROM_CURRENT"],
                            "lehrer_id": [lehrer_id],
                            "fach_id": [fach_id],
                            "stundenzahl": [stundenzahl],
                            "stufe": [stufe],
                            "cre_userid": ["frontend-page2-userinpt"],
                            "cre_date": [datetime.date.today()],
                            "chg_userid": [None],
                            "chg_date": [None]
                        })

                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:

                        if submitblock:
                            st.warning("Bitte alle benötigten Felder ausfüllen.")
                        
                        # give data to data_core
                        


            case "Lehrer":
                
                # form for the 'lehrer' input
                
                with st.form("Lehrer",clear_on_submit=True):
                    if inpt_preference == "slider":
                        vorname = st.text_input("Bitte Vorname des Schülers / der Schülerin eingeben")
                        nachname = st.text_input("Bitte Nachname des Schülers / der Schülerin eingeben")
                        vorname2 = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")
                        kuerzel = st.text_input("Lehrer-Kürzel")
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen", schule_display)
                        origin = st.multiselect("Herkunftschule auswählen", schule_display)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        gebdatum = st.date_input("Geburtsdatum")



                    elif inpt_preference == "Eingabefeld":
                        vorname = st.text_input("Bitte Vorname des Schülers / der Schülerin eingeben")
                        nachname = st.text_input("Bitte Nachname des Schülers / der Schülerin eingeben")
                        vorname2 = st.text_input("Bitte zweiten Vornamen des Schülers / der Schülerin eingeben (falls vorhanden)")
                        email = st.text_input("Bitte Email-Adresse des Schülers eingeben (falls vorhanden)")
                        kuerzel = st.text_input("Lehrer-Kürzel")
                        an_schule_seit = st.date_input("Bitte Datum eingeben, seit welchem der Schüler / die Schülerin an der Schule ist")
                        schule = st.multiselect("Schule auswählen", schule_display)
                        origin = st.multiselect("Herkunftsschule auswählen", schule_display)
                        adresse= st.text_input("Wohnadresse des Schülers")
                        gebdatum = st.date_input("Geburtsdatum")


                    if not schule_exists:
                        submitblock = True

                    else:
                        submitblock = False
                        schule_id = schule_datadict[schule]


                        lehrer = pd.DataFrame({
                            "lehrer_id": ["ASIGN_FROM_CURRENT"],
                            "vorname": [vorname],
                            "nachname": [nachname],
                            "vorname2": [vorname2],
                            "email": [email],
                            "kuerzel": [kuerzel],
                            "an_schule_seit": [an_schule_seit],
                            "schule_id": [schule_id],
                            "origin": [schule_id],
                            "adresse": [adresse],
                            "gebdatum": [gebdatum],
                            "cre_userid": ["frontend-page2-userinpt"],
                            "cre_date": [datetime.date.today()],
                            "chg_userid": [None],
                            "chg_date": [None]
                        })

                    submitted = st.form_submit_button("Daten übernehmen")
                    if submitted:
                        if submitblock:
                            st.warning("Bitte alle benötigten Felder ausfüllen.")

                        # check if email is valid:
                        # TODO add better email check using module later on
                        if "@" not in email:
                            st.warning("Email ungültig.",icon="⚠️")

                        
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
                        "stunen_id": ["ASIGN_FROM_CURRENT"],
                        "sday": [sday],
                        "scount": [scount],
                        "cre_userid": ["frontend-page2-userinpt"],
                        "cre_date": [datetime.date.today()],
                        "chg_userid": [None],
                        "chg_date": [None]
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
                        "schulevents_id": ["ASIGN_FROM_CURRENT"],
                        "descript": [descript],
                        "datum": [datum],
                        "cre_userid": ["frontend-page2-userinpt"],
                        "cre_date": [datetime.date.today()],
                        "chg_userid": [None],
                        "chg_date": [None]
                    })

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:
                        
                        # give data to data_core
                        


            case "Schule":

                # form for the 'schule' input

                with st.form("Schule",clear_on_submit=True):
                    if inpt_preference == "slider":
                        name = st.text_input("Name der Schule")
                        stype = st.selectbox("Bitte Schultyp auswählen",schultypes)# ** make user aware he can change the presets
                        adresse = st.text_input("Adresse der Schule eingeben")


                    elif inpt_preference== "Eingabefeld":
                        name = st.text_input("Name der Schule")
                        stype = st.selectbox("Bitte Schultyp auswählen",schultypes)# ** make user aware he can change the presets
                        adresse = st.text_input("Adresse der Schule eingeben")



                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:

                        #give data to data_core


            case "Fächer":

                # form for the 'fächer' input

                with st.form("Fächer",clear_on_submit=True):
                    if inpt_preference == "slider":
                        name = st.text_input("Name des Fachs eingeben")

                    elif inpt_preference == "Eingabefeld":
                        name = st.text_input("Name des Fachs eingeben")

                    submitted = st.form_submit_button("Daten übernehmen")
                    #if submitted:

                        #give data to data_core






    elif st.session_state["notenrechner_data_config"] == 0:
        
        # code for adding a grade for config 1

        # NOTE: for this config there is only a single table

        # forms to build:
        # Noten -> noten_simplified.csv
        

        with st.form("Noten",clear_on_submit=True):
            # ! NOTE: this part is not functional due to the faecher variable not containing any data yet
            
            # form for the simplified Noten input
            
            arbeit_type = ["(Arbeit / Kursarbeit)","(Test / Hausaufgabenüberprüfung / Mitarbeit)"]

            if inpt_preference == "slider":# getting input for slider as prefered input
                score = st.slider("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                fach = st.select_slider("Bitte Fach auswählen",fach_display) # ** commented out to allow for easier testing
                arbeit_type = st.select_slider("Bitte Typ des Leistungsnachweises wählen",leistungsnachweisformen)
                count = st.slider("Die wievielte Note ist das ?",min_value=0,max_value = 20,step=1,value = 0)
                
            elif inpt_preference == "Eingabefeld":# getting input for other input as prefered input
                score = st.number_input("Note eingeben",min_value=0,max_value=15, value=10, step=1)
                fach = st.selectbox("Bitte Fach auswählen",fach_display) # ** commented out to allow for easier testing
                arbeit_type = st.selectbox("Bitte Typ des Leistungsnachweises wählen",leistungsnachweisformen)
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
            #if submitted:
                
                # give data to data_core
                

