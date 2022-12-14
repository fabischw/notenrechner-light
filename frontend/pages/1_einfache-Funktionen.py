"""
This file includes super simple frontend-only functions that provide mostly QOL (quality of life) features

the functions for the user:
- calculate the average for a given amount of grades
- calculate the final grade someone is supposed to get basedon prevous exam results
- calculate the achieved percent in an exam
- function to help counting points in an exam
"""



import streamlit as st
import PIL
import pathlib
import pandas as pd
import pathlib
import importlib.util
import sys



# file paths
here = pathlib.Path(__file__).parent


project = here.parent.parent#project folder
glue_layer = project / "glue"# /glue
frontend_layer = project / "frontend"
resources_dir = project / "frontend" / "resources"# /frontend/resources
appdata = project / "appdata"

settings_path = appdata / "user_data" / "notenrechnersettings.json"



# import local modules


#importing main
main_spec=importlib.util.spec_from_file_location("main",frontend_layer / "main.py")
main = importlib.util.module_from_spec(main_spec)
main_spec.loader.exec_module(main)
sys.modules["main"] = main







#importing frontend funcs
frontend_funcs_spec = importlib.util.spec_from_file_location("frontend_funcs",frontend_layer / "frontend_funcs.py")
frontend_funcs = importlib.util.module_from_spec(frontend_funcs_spec)
frontend_funcs_spec.loader.exec_module(frontend_funcs)
sys.modules["frontend_funcs"] = frontend_funcs


# logic to check if the page was being reload, if yes, initialize the app again
if "DATA" not in st.session_state:
    frontend_funcs.init_phase()#initializing the app, if page is reload







#set the page icon
here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
st.set_page_config(page_title="Funktionen",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


#page title
st.title("einfache Funktionen")
st.markdown("- Es wird keine Garantie für die errechneten Werte übernommen")




# functions
# function to calculate the percentage required for a specific grade
def getpercentage_for_note(note):
    match note:
        case 15: return(95)
        case 14: return(90)
        case 13: return(85)
        case 12: return(80)
        case 11: return(75)
        case 10: return(70)
        case 9: return(65)
        case 8: return(60)
        case 7: return(55)
        case 6: return(50)
        case 5: return(45)
        case 4: return(40)
        case 3: return(33)
        case 2: return(27)
        case 1: return(20)



# ! Change to a switch statement - Also, the name should be get_note_from_percentage(percentage).
# function to get the grade based on the percentage a student got		
def get_note_from_percentage(percentage):
    if percentage < 20:
        return("00")
    elif percentage >= 20 and percentage <27:
        return("01")
    elif percentage >= 27 and percentage <33:
        return("02")
    elif percentage >= 33 and percentage <40:
            return("03")
    elif percentage >= 40 and percentage <45:
            return("04")
    elif percentage >= 45 and percentage < 50:
        return("05")
    elif percentage >= 50 and percentage < 55:
        return("06")
    elif percentage >= 55 and percentage < 60:
        return("07")
    elif percentage >= 60 and percentage < 65:
        return("08")
    elif percentage >= 65 and percentage < 70:
        return("09")
    elif percentage >= 70 and percentage < 75:
        return("10")
    elif percentage >= 75 and percentage < 80:
        return("11")
    elif percentage >= 80 and percentage < 85:
        return("12")
    elif percentage >= 85 and percentage < 90:
        return("13")
    elif percentage >= 90 and percentage  < 95:
        return("14")
    elif percentage >= 95:
        return("15")













#Zeugnisdurchschnittsrechner
st.markdown("### Zeugnisdurchschnittsrechner")
st.markdown("- Diese Funktion rechnet den Zeugnisnotendurchschnitt basierend auf eingegebenen Noten aus")

st.sidebar.markdown("## Notendurchschnitt")

@st.cache(allow_output_mutation=True)
# ** this function has to be here for the cache loading to work
def Nums():
    return []

with st.expander("Notendurchschnitt"):#streamlit expander for content

    nums = Nums() # ** should be fine I hope, check commit for extra details
    #slider / number inout depending on the current state
    if st.session_state["inpt_prefered"] == "slider":
        num = st.sidebar.slider("Note hinzufügen",min_value=0,max_value=15,step=1)
    elif st.session_state["inpt_prefered"] == "Eingabefeld":
        num = st.sidebar.number_input("Note hinzufügen",min_value=0,max_value=15,step=1)
    if st.sidebar.button("Note hinzufügen"):
        nums.append(num)

    if st.sidebar.button("Letzte Note entfernen "):
        if len(nums) > 0:#check if theres already elements befroe attempting to delete the last element
            nums.pop(len(nums)-1)

    if st.sidebar.button("Alle Noten entfernen"):
        nums = []

    try:
        inputs = nums
        st.table(inputs)#create the table containing the data
        st.write("Durchschnitt: ", round(sum(inputs)/len(inputs),2)," in Notensystem 1-6:",round(((17-(sum(inputs)/len(inputs)))/3),2))
    except:# ** render the Info to input data in case no data is present yet
        st.write("Gib Noten links in der Seitenleiste ein !")#output info if no data to calculate average yet





#Note für Zeugnis vorberechnen
st.markdown("### Note für Zeugnis vorberechnen [Oberstufe]")
st.markdown("- Diese Funktion rechnet aus Kursarbeitsnoten und der Mitarbeitsnote die Zeugnisnote aus.")


with st.expander("Note vorberechnen"):#streamlit expander for content

    #data input

    if st.session_state["inpt_prefered"] == "Eingabefeld":
        kursarbeit1 = st.number_input("1. Kursarbeit",min_value=0,max_value=15,step=1)
        kursarbeit2 = st.number_input("2. Kursarbeit",min_value=0,max_value=15,step=1)

        muendlich_1 = st.number_input("mündliche Mitarbeit 1",min_value=0,max_value=15,step=1)
        muendlich_2 = st.number_input("mündliche Mitarbeit 2 (optional) ",min_value=0,max_value=15,step=1)

        gewichtung = st.number_input("Prozent pro Kursarbeit (optional)", min_value=0,max_value=50,value=40,step=1)

    elif st.session_state["inpt_prefered"] == "slider":

        kursarbeit1 = st.slider("1. Kursarbeit",min_value=0,max_value=15,step=1)
        kursarbeit2 = st.slider("2. Kursarbeit",min_value=0,max_value=15,step=1)

        muendlich_1 = st.slider("mündliche Mitarbeit 1",min_value=0,max_value=15,step=1)
        muendlich_2 = st.slider("mündliche Mitarbeit 2 (optional) ",min_value=0,max_value=15,step=1)

        gewichtung = st.slider("Prozent pro Kursarbeit (optional)", min_value=0,max_value=50, value=40, step=1)

    if muendlich_2 == None:#check if there was a 2nd 'mündliche Note' given, if no, set to same as first (for average calculation)
        muendlich_2 = muendlich_1


    zeugnis_note = round((kursarbeit1+kursarbeit2)*((gewichtung/100)) + ((100-gewichtung*2)/100)*((muendlich_1+muendlich_2)/2),2)#calculation

    st.write("Zeugnisnote:",zeugnis_note," in Notensystem 1-6:",round(((17-zeugnis_note)/3),2))#output results



# calculation for percent achieved in exam 
# ! fix bug related to this
st.markdown("### Prozent in Arbeit ausrechnen")
st.markdown("- Dise Funktion erleichtert das Rechnen mit Prozenten und Punkten im Zusammenhang einer Kursarbeit")

with st.expander("Prozentrechnung Kursarbeit"):#expander for the  Prozentrechnung functionality
    st.markdown("Prozentwerte für Abitur / GOS")

    #Dictionairy for the grades / required score
    data_dict = {
        "Note: ": [],
        "benötigte Punkte: ": []
    }

    #calculate the required score for each possible grade based on the maximum score possible
    def prozentrechnung_arbeit(gesamt):
        noten = []
        punkte = []
        if gesamt:#double checking if the inserted data makes sense
            for i in range(1,16):
                x = round(((gesamt * getpercentage_for_note(i)) / 100),2)
                if len(str(i)) == 1:
                    i = str("0"+str(i))
                noten.append(i)
                punkte.append(x)
            data_dict["Note: "] = noten
            data_dict["benötigte Punkte: "] = punkte



        else:
            st.table()
            st.write("Gib die Maximalpunktzahl ein !")


        st.table(pd.DataFrame.from_dict(data_dict))#displaying the calculated data in a streamlit table componenet

    if st.session_state["inpt_prefered"] == "Eingabefeld":
        max_punktzahl = st.number_input("Maximalpunktzahl",min_value=1.00)# input for the maximum score possible in an exam
        erreicht_punktzahl = st.number_input("erreichte Punktzahl",min_value=0.0,max_value=max_punktzahl,step=0.25)# number_input for the reached score
    elif st.session_state["inpt_prefered"] == "slider":
        max_punktzahl = st.slider("Maximalpunktzahl",min_value=1.00,max_value=100.00,step=0.25)# input for the maximum score possible in an exam
        erreicht_punktzahl = st.slider("erreichte Punktzahl",min_value=0.0,max_value=max_punktzahl,step=0.25)#slider for the reached score

    


    if st.button("Eingaben anwenden"):#button for applying the input 
        prozentrechnung_arbeit(max_punktzahl)
        #displaying the grade the student gets with the points given
        st.write("Erreichte Note: ",int(get_note_from_percentage((erreicht_punktzahl/max_punktzahl)*100)),"Erreichte Prozentzahl: ",round(erreicht_punktzahl/max_punktzahl*100,2))





#Punktezähler für Arbeit
st.markdown("### Punktezähler für Arbeit")
st.markdown("- Punkte links in Seitenleiste eingeben und einfach summieren lassen !")


#moving this function to the sidebar to make things easier
# **the code below is required because of the way streamlit works with caching
@st.cache(allow_output_mutation=True)
def punkte_arr():
    return []


st.sidebar.markdown("# Punktezähler für Arbeit")


pkt_arr = punkte_arr()
if st.session_state["inpt_prefered"] == "Eingabefeld":
    pkt = st.sidebar.number_input("Punkte hinzufügen",min_value=0.0,max_value=100.0,step=0.25)#sidebar input für Note
elif st.session_state["inpt_prefered"] == "slider":
    pkt = st.sidebar.slider("Punkte hinzufügen",min_value=0.0,max_value=100.0,step=0.25)#sidebar input für Note
if st.sidebar.button("Punkte hinzufügen"):#adding points to the array
    pkt_arr.append(pkt)

if st.sidebar.button("Letzte Punkte entfernen "):#removing the last added element in the array
    if len(pkt_arr) > 0:#check if theres already elements befroe attempting to delete the last element
        pkt_arr.pop(len(pkt_arr)-1)

try:
    inputs = pkt_arr
    st.sidebar.write("Punkte gesamt: ",sum(pkt_arr))
except:# ** render the Info to input data in case no data is present yet
    st.sidebar.write("Gib Noten oben ein!")#output info if no data to calculate average yet



