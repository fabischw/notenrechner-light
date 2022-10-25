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
kurs_columns = []
kurs_datatypes = []
kurs_required = []

stunden_columns = []
stunden_datatypes = []
stunden_required = []

fach_columns = []
fach_datatypes = []
fach_required = []

schulevents_columns = []
schulevents_datatypes = []
schulevents_required = []

arbeiten_columns = []
arbeiten_datatypes = []
arbeiten_required = []

kalender_columns = []
kalender_datatypes = []
kalender_required = []

schueler_columns = []
schueler_datatypes = []
schueler_required = []

noten_columns = []
noten_datatypes = []
noten_required = []

lehrer_columns = []
lehrer_datatypes = []
lehrer_required = []

fach_columns = []
fach_datatypes = []
fach_required = []

kursschuleventsref_columns = []
kursschuleventsref_datatypes = []
kursschuleventsref_required = []

kursstundenref_columns = []
kursstundenref_datatypes = []
kursstundenref_required = []

kursschuelerref_columns = []
kursschuelerref_datatypes = []
kursschuelerref_required = []

lehrerfachref_columns = []
lehrerfachref_datatypes = []
lehrerfachref_required = []

notenschuelerref_columns = []
notenschuelerref_datatypes = []
notenschuelerref_required = []





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




