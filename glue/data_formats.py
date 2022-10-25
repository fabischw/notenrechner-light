"""
This file includes the formats for each dataframe
This includes column names, data types etc.
"""



#importing modules
import pandas as pd
import os
import pathlib
import importlib.util
import sys
import json
import os.path
import streamlit as st
import copy


#paths
here = pathlib.Path(__file__)
glue_layer = here.parent

# ** columns / datatpyes for the tables / csv's
"""
EXAMPLE LAYOUT:

EXAMPLE_columns = ["name","score","date","day"]
EXAMPLE_datatypes = ["VARCHAR(20)","NUMBER(2)","DATE","DATE"] -> ORACLE datatypes
EXAMPLE_required = ["name","score"] -> required keys
"""


kurs_columns = ["kurs_id","lehrer_id","fach_id","stundenzahl","stufe","cre_userid","cre_date","chg_userid","chg_date"]
kurs_datatypes = ["NUMBER(10)","NUMBER(10)","NUMBER(10)","NUMBER(2)","NUMBER(2)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
kurs_required = ["kurs_id","lehrer_id","fach_id","stundenzahl","stufe","cre_userid","cre_date"]

stunden_columns = ["stunden_id","sday","scount","cre_userid","cre_date","chg_userid","chg_date"]
stunden_datatypes = ["NUMBER(10)","VARCHAR(20)","NUMBER(2)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
stunden_required = ["stunden_id","sday","scount","cre_userid","cre_date"]

fach_columns = ["fach_id","fname","cre_userid","cre_date","chg_userid","chg_date"]
fach_datatypes = ["NUMBER(10)","VARCHAR(40)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
fach_required = ["fach_id","fname","cre_userid","cre_date"]

schulevents_columns = ["schulevents_id","descript","datum","cre_userid","cre_date","chg_userid","chg_date"]
schulevents_datatypes = ["NUMBER(10)","VARCHAR(200)","DATE","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
schulevents_required = ["schulevents_id","descript","datum","cre_userid","cre_date"]

arbeiten_columns = ["arbeiten_id","atype","kurs_id","datum","acount","cre_userid","cre_date","chg_userid","chg_date"]
arbeiten_datatypes = ["NUMBER(10)","VARCHAR(3)","NUMBER(10)","DATE","NUMBER(10)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
arbeiten_required = ["arbeiten_id","atype","kurs_id","datum","cre_userid","cre_date"]

kalender_columns = ["kalender_id","events_descript","events_date","cre_userid","cre_date","chg_userid","chg_date"]
kalender_datatypes = ["NUMBER(10)","VARCHAR(200)","DATE","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
kalender_required = ["kalender_id","events_descript","events_date","cre_userid","cre_date"]

schueler_columns = ["schueler_id","vorname","nachname","vorname2","email","an_schule_seit","schule","stufe","adresse","salter","gebdatum","cre_userid","cre_date","chg_userid","chg_date"]
schueler_datatypes = ["NUMBER(10)","VARCHAR(30)","VARCHAR(30)","VARCHAR2(30)","VARCHAR(30)","DATE",""]
schueler_required = ["schueler_id","vorname","nachname","email","schule","stufe","salter","cre_userid","cre_date"]

noten_columns = ["noten_id","score","ntype","kommentar","doclink","ndate","anz_year","kurs_id","cre_userid","cre_date","chg_userid","chg_date"]
noten_datatypes = ["NUMBER(10)","NUMBER(2)","VARCHAR(10)","VARCHAR2(100)","VARCHAR2(200)","DATE","VARCHAR2(100)","NUMBER(10)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
noten_required = ["noten_id","score","ntype","kurs_id","cre_userid","cre_date"]

lehrer_columns = ["lehrer_id","vorname","nachname","vorname2","email","kuerzel","an_schule_seit","schule","origin","adresse","gebdatum","cre_userid","cre_date","chg_userid","chg_date"]
lehrer_datatypes = ["NUMBER(10)","VARCHAR(30)","VARCHAR(30)","VARCHAR2(30)","VARCHAR(30)","VARCHAR(5)","DATE","VARCHAR(2)","VARCHAR(1)","VARCHAR2(300)","VARCHAR(30)","DATE","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
lehrer_required = ["lehrer_id","vorname","nachname","email","kuerzel","schule","origin","adresse","cre_userid","cre_date"]

fach_columns = ["fach_id","fname","cre_userid","cre_date","chg_userid","chg_date"]
fach_datatypes = ["NUMBER(10)","VARCHAR(40)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
fach_required = ["fach_id","fname","cre_userid","cre_date"]

kursschuleventsref_columns = ["kursschuleventsref_id","kurs_id","schulevents_id","cre_userid","cre_date","chg_userid","chg_date"]
kursschuleventsref_datatypes = ["NUMBER(10)","NUMBER(10)","NUMBER(10)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
kursschuleventsref_required = ["kursschuleventsref_id","kurs_id","schulevents_id","cre_userid","cre_date"]

kursstundenref_columns = ["kursschuleventsref_id","kurs_id","schulevents_id","cre_userid","cre_date","chg_userid","chg_date"]
kursstundenref_datatypes = ["NUMBER(10)","NUMBER(10)","NUMBER(10)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
kursstundenref_required = ["kursschuleventsref_id","kurs_id","schulevents_id","cre_userid","cre_date"]

kursschuelerref_columns = ["kursschuelerref_id","kurs_id","schueler_id","cre_userid","cre_date","chg_userid","chg_date"]
kursschuelerref_datatypes = ["NUMBER(10)","NUMBER(10)","NUMBER(10)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
kursschuelerref_required = ["kursschuelerref_id","kurs_id","schueler_id","cre_userid","cre_date"]

lehrerfachref_columns = ["lehrerfachref_id","lehrer_id","fach_id","cre_userid","cre_date","chg_userid","chg_date"]
lehrerfachref_datatypes = ["NUMBER(10)","NUMBER(10)","NUMBER(10)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
lehrerfachref_required = ["lehrerfachref_id","lehrer_id","fach_id","cre_userid","cre_date"]

notenschuelerref_columns = ["notenschuelerref_id","noten_id","schueler_id","cre_userid","cre_date","chg_userid","chg_date"]
notenschuelerref_datatypes = ["NUMBER(10)","NUMBER(10)","NUMBER(10)","VARCHAR(30)","DATE","VARCHAR2(30)","DATE"]
notenschuelerref_required = ["notenschuelerref_id","noten_id","schueler_id","cre_userid","cre_date"]





def get_data_format(table_name):
    """
    This function return a array with three arrays containing:
        - column names
        - data types for column
        - required fields
    """
    match table_name:
        case "kurs":
            result = []
            result.append(kurs_columns)
            result.append(kurs_datatypes)
            result.append(kurs_required)
            return(result)
        case "stunden":
            result = []
            result.append(stunden_columns)
            result.append(stunden_datatypes)
            result.append(stunden_required)
            return(result)
        case "fach":
            result = []
            result.append(fach_columns)
            result.append(fach_datatypes)
            result.append(fach_required)
            return(result)
        case "schulevents":
            result = []
            result.append(schulevents_columns)
            result.append(schulevents_datatypes)
            result.append(schulevents_required)
            return(result)
        case "arbeiten":
            result = []
            result.append(arbeiten_columns)
            result.append(arbeiten_datatypes)
            result.append(arbeiten_required)
            return(result)
        case "kalender":
            result = []
            result.append(kalender_columns)
            result.append(kalender_datatypes)
            result.append(kalender_required)
            return(result)
        case "schueler":
            result = []
            result.append(schueler_columns)
            result.append(schueler_datatypes)
            result.append(schueler_required)
            return(result)
        case "noten":
            result = []
            result.append(noten_columns)
            result.append(noten_datatypes)
            result.append(noten_required)
            return(result)
        case "lehrer":
            result = []
            result.append(lehrer_columns)
            result.append(lehrer_datatypes)
            result.append(lehrer_required)
            return(result)
        case "fach":
            result = []
            result.append(fach_columns)
            result.append(fach_datatypes)
            result.append(fach_required)
            return(result)
        case "kursschuleventsref":
            result = []
            result.append(kursschuleventsref_columns)
            result.append(kursschuleventsref_datatypes)
            result.append(kursschuleventsref_required)
            return(result)
        case "kursstundenref":
            result = []
            result.append(kursstundenref_columns)
            result.append(kursstundenref_datatypes)
            result.append(kursstundenref_required)
            return(result)
        case "kursschuelerref":
            result = []
            result.append(kursschuelerref_columns)
            result.append(kursschuelerref_datatypes)
            result.append(kursschuelerref_required)
            return(result)
        case "lehrerfachref":
            result = []
            result.append(lehrerfachref_columns)
            result.append(lehrerfachref_datatypes)
            result.append(lehrerfachref_required)
            return(result)
        case "notenschuelerref":
            result = []
            result.append(notenschuelerref_columns)
            result.append(notenschuelerref_datatypes)
            result.append(notenschuelerref_required)
            return(result)




