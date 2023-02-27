"""
This file provides the functionality to use the custom-built hashing function
which can later be used to compare datasets and pfrorm checks on the data
"""



def hash_data(tablename,inpt_data, **kwargs):
    """
    custom-built hashing function for the data to later compare and find errors
    

    tablename(str): name of the table the data is from
    inpt_data(dict): the data being hashed

    **kwargs:

    include_index(bool): sets whether an index based on the previous data (automaticly checked)
    will be added to the final hash

    recognizable(bool): sets whether an hash can be traced back to a specific table
    or not

    """


    match tablename:
        case "noten":
        case "schueler":
        case "kurs":
        case "lehrer":
        case "stunden":
        case "fach":
        case "schule":
        case "schulevents":
        case "arbeiten":
        case "kalender":
        case "kursschuleventsref":
        case "kursstundenref":
        case "kursschuelerref":
        case "lehrerfachref":
        case "notenschuelerref":
        case "noten_simplified":

