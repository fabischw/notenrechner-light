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
st.markdown(" -Diese Funktion rechnet den Zeugnisnotendurchschnitt basierend auf eingegebenen Noten aus")


@st.cache(allow_output_mutation=True)
def Nums():
    return []

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
    st.write("Durchschnitt: ", sum(inputs)/len(inputs))
except:
    st.write("Gib Noten ein !")



#Note für Zeugnis vorberechnen
st.markdown("### Note für Zeugnis vorberechnen")


#Prozent in Arbeit ausrechnen
st.markdown("### Prozent in Arbeit ausrechnen")



#Punktezähler für Arbeit
st.markdown("### Punktezähler für Arbeit")

