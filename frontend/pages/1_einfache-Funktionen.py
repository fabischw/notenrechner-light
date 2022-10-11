import streamlit as st
import PIL
import pathlib
import pandas as pd

#functions
# TODO export functions to different file

#Funktion um Prozentzahl zu gegebener Note zu erhalten
def getpercentage_for_note(note):
    if note == 15:
        return(95)
    elif note == 14:
        return(90)
    elif note == 13:
        return(85)
    elif note == 12:
        return(80)
    elif note == 11:
        return(75)
    elif note == 10:
        return(70)
    elif note == 9:
        return(65)
    elif note == 8:
        return(60)
    elif note == 7:
        return(55)
    elif note == 6:
        return(50)
    elif note == 5:
        return(45)
    elif note == 4:
        return(40)
    elif note == 3:
        return(33)
    elif note == 2:
        return(27)
    elif note == 1:
        return(20)



#Funktion um Note füt gegebene Prozent zu erhalten		
def getnotefrompercentage(percentage):
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

#Zeugnisdurchschnittsrechner
st.markdown("### Zeugnisdurchschnittsrechner")
st.markdown("- Diese Funktion rechnet den Zeugnisnotendurchschnitt basierend auf eingegebenen Noten aus")

st.sidebar.markdown("## Notendurchschnitt")

@st.cache(allow_output_mutation=True)
#get empty array
def Nums():
    return []

with st.expander("Notendurchschnitt"):#streamlit expander for content

    nums = Nums()
    num = st.sidebar.number_input("Note hinzufügen",min_value=0,max_value=15,step=1)#sidebar input für Note
    if st.sidebar.button("Note hinzufügen"):
        nums.append(num)

    if st.sidebar.button("Letzte Note entfernen "):
        if len(nums) > 0:#check if theres already elements befroe attempting to delete the last element
            nums.pop(len(nums)-1)

    try:
        inputs = nums
        st.table(inputs)#create the table containing the data
        st.write("Durchschnitt: ", round(sum(inputs)/len(inputs),2)," in Notensystem 1-6:",round(((17-(sum(inputs)/len(inputs)))/3),2))
    except:
        st.write("Gib Noten links in der Seitenleiste ein !")#output info if no data to calculate average yet





#Note für Zeugnis vorberechnen
st.markdown("### Note für Zeugnis vorberechnen [Oberstufe]")
st.markdown("- Diese Funktion rechnet aus Kursarbeitsnoten und der Mitarbeitsnote die Zeugnisnote aus.")

# TODO add comments
with st.expander("Note vorberechnen"):#streamlit expander for content

    #number inputs
    kursarbeit1 = st.number_input("1. Kursarbeit",min_value=0,max_value=15,step=1)
    kursarbeit2 = st.number_input("2. Kursarbeit",min_value=0,max_value=15,step=1)

    muendlich_1 = st.number_input("mündliche Mitarbeit 1",min_value=0,max_value=15,step=1)
    muendlich_2 = st.number_input("mündliche Mitarbeit 2 (optional) ",min_value=0,max_value=15,step=1)

    gewichtung = st.slider("Prozent pro Kursarbeit (optional)", min_value=0,max_value=50, value=40)#iput slider

    if muendlich_2 == None:#check if there was a 2nd 'mündliche Note' given, if no, set to same as first (for average calculation)
        muendlich_2 = muendlich_1


    zeugnis_note = round((kursarbeit1+kursarbeit2)*(gewichtung/100) + ((100-gewichtung)/100)*((muendlich_1+muendlich_2)/2),2)#calculation

    st.write("Zeugnisnote:",zeugnis_note," in Notensystem 1-6:",round(((17-zeugnis_note)/3),2))#output results



#Prozent in Arbeit ausrechnen
st.markdown("### Prozent in Arbeit ausrechnen")
st.markdown("- Dise Funktion erleichtert das Rechnen mit Prozenten und Punkten im Zusammenhang einer Kursarbeit")

with st.expander("Prozentrechnung Kursarbeit"):
    st.markdown("Prozentwerte für Abitur / GOS")

    data_dict = {
        "Note: ": [],
        "benötigte Punkte: ": []
    }


    def prozentrechnung_arbeit(gesamt):
        noten = []
        punkte = []
        if gesamt != None or gesamt != 0.0:
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


        st.table(pd.DataFrame.from_dict(data_dict))

    max_punktzahl = st.number_input("Maximalpunktzahl",min_value=1.00)


    erreicht_punktzahl = st.slider("erreichte Punktzahl",min_value=0.0,max_value=max_punktzahl,step=0.25)


    if st.button("Eingaben anwenden"):
        prozentrechnung_arbeit(max_punktzahl)
        st.write("Erreichte Note: ",int(getnotefrompercentage((erreicht_punktzahl/max_punktzahl)*100)),"Erreichte Prozentzahl: ",round(erreicht_punktzahl/max_punktzahl*100,2))



# TODO add comments

#Punktezähler für Arbeit
st.markdown("### Punktezähler für Arbeit")
st.markdown("- Punkte links eingeben und einfach summieren lassen !")

@st.cache(allow_output_mutation=True)
def punkte_arr():
    return []


st.sidebar.markdown("# Punktezähler für Arbeit")


pkt_arr = punkte_arr()
pkt = st.sidebar.number_input("Punkte hinzufügen",min_value=0.0,max_value=100.0,step=0.25)#sidebar input für Note
if st.sidebar.button("Punkte hinzufügen"):
    pkt_arr.append(pkt)

if st.sidebar.button("Letzte Punkte entfernen "):
    if len(pkt_arr) > 0:#check if theres already elements befroe attempting to delete the last element
        pkt_arr.pop(len(pkt_arr)-1)

try:
    inputs = pkt_arr
    st.sidebar.write("Punkte gesamt: ",sum(pkt_arr))
except:
    st.sidebar.write("Gib Noten oben ein!")#output info if no data to calculate average yet



