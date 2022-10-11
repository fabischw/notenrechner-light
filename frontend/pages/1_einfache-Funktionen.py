import streamlit as st
import PIL
import pathlib


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
        st.write("Durchschnitt: ", sum(inputs)/len(inputs)," in Notensystem 1-6:",round(((17-(sum(inputs)/len(inputs)))/3),2))
    except:
        st.write("Gib Noten links in der Seitenleiste ein !")#output info if no data to calculate average yet





#Note für Zeugnis vorberechnen
st.markdown("### Note für Zeugnis vorberechnen [Oberstufe]")
st.markdown("- Diese Funktion rechnet aus Kursarbeitsnoten und der Mitarbeitsnote die Zeugnisnote aus.")

with st.expander("Note vorberechnen"):#streamlit expander for content

    #number inputs
    kursarbeit1 = st.number_input("1. Kursarbeit",min_value=0,max_value=15,step=1)
    kursarbeit2 = st.number_input("2. Kursarbeit",min_value=0,max_value=15,step=1)

    muendlich_1 = st.number_input("mündliche Mitarbeit 1",min_value=0,max_value=15,step=1)
    muendlich_2 = st.number_input("mündliche Mitarbeit 2 (optional) ",min_value=0,max_value=15,step=1)

    gewichtung = st.slider("Prozent pro Kursarbeit (optional)", min_value=0,max_value=100, value=40)#iput slider

    if muendlich_2 == None:#check if there was a 2nd 'mündliche Note' given, if no, set to same as first (for average calculation)
        muendlich_2 = muendlich_1


    zeugnis_note = round((kursarbeit1+kursarbeit2)*(gewichtung/100) + ((100-gewichtung)/100)*((muendlich_1+muendlich_2)/2),2)#calculation

    st.write("Zeugnisnote:",zeugnis_note," in Notensystem 1-6:",round(((17-zeugnis_note)/3),2))#output results



#Prozent in Arbeit ausrechnen
st.markdown("### Prozent in Arbeit ausrechnen")
st.makrdown("- Dise Funktion erleichtert das Rechnen mit Prozenten und Punkten im Zusammenhang einer Kursarbeit")




#Punktezähler für Arbeit
st.markdown("### Punktezähler für Arbeit")

