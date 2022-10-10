import streamlit as st
import PIL
import pathlib


here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'

icon = resources_dir = resources_dir / 'page_icon.ico'



#initializing the page
icon_load = PIL.Image.open(icon)
st.set_page_config(page_title="Funktionen",page_icon=icon_load)




#sidebar
st.sidebar.success("Funktion / Modul wählen")


#content
st.title("einfache Funktionen")

#Zeugnisdurchschnittsrechner
st.markdown("### Zeugnisdurchschnittsrechner")
st.markdown("- Diese Funktion rechnet den Zeugnisnotendurchschnitt basierend auf eingegebenen Noten aus")

st.sidebar.markdown("## Notendurchschnitt")

@st.cache(allow_output_mutation=True)
def Nums():
    return []

#expander für Notendurchschnitt
with st.expander("Notendurchschnitt"):

    nums = Nums()
    num = st.sidebar.number_input("Note hinzufügen",min_value=0,max_value=15,step=1)
    if st.sidebar.button("Note hinzufügen"):
        nums.append(num)

    if st.sidebar.button("Letzte Note entfernen "):
        if len(nums) > 0:
            nums.pop(len(nums)-1)

    try:
        inputs = nums
        st.table(inputs)
        st.write("Durchschnitt: ", sum(inputs)/len(inputs)," in Notensystem 1-6:",round(((17-(sum(inputs)/len(inputs)))/3),2))
    except:
        st.write("Gib Noten links in der Seitenleiste ein !")





#Note für Zeugnis vorberechnen
st.markdown("### Note für Zeugnis vorberechnen [Oberstufe]")
st.markdown("- Diese Funktion rechnet aus Kursarbeitsnoten und der Mitarbeitsnote die Zeugnisnote aus.")

with st.expander("Note vorberechnen"):
    kursarbeit1 = st.number_input("1. Kursarbeit",min_value=0,max_value=15,step=1)
    kursarbeit2 = st.number_input("2. Kursarbeit",min_value=0,max_value=15,step=1)

    muendlich_1 = st.number_input("mündliche Mitarbeit 1",min_value=0,max_value=15,step=1)
    muendlich_2 = st.number_input("mündliche Mitarbeit 2 (optional) ",min_value=0,max_value=15,step=1)

    gewichtung = st.slider("Prozent pro Kursarbeit (optional)", min_value=0,max_value=100, value=40)

    if muendlich_2 == None:
        muendlich_2 = muendlich_1


    zeugnis_note = round((kursarbeit1+kursarbeit2)*(gewichtung/100) + ((100-gewichtung)/100)*((muendlich_1+muendlich_2)/2),2)

    st.write("Zeugnisnote:",zeugnis_note," in Notensystem 1-6:",round(((17-zeugnis_note)/3),2))



#Prozent in Arbeit ausrechnen
st.markdown("### Prozent in Arbeit ausrechnen")



#Punktezähler für Arbeit
st.markdown("### Punktezähler für Arbeit")

