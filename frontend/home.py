# frontend appss

#installing dependencies
import PIL
from importlib_metadata import version
import streamlit as st
import frontend_funcs
import pathlib

__author__ = "fabischw"
__version__ = ("DEV","0.001","early-testing")


here = pathlib.Path(__file__)
here = here.parent

icon_path_jmp1 = here / 'resources'
icon_path_fnl = icon_path_jmp1 / 'page_icon.ico'


try:
    #set the page icon and title
    icon_load = PIL.Image.open(icon_path_fnl)
    st.set_page_config(page_title="Notenrechner light home",page_icon=icon_load)
except:
    st.write("unable to load icon.")



#sidebar
st.sidebar.success("Funktion / Modul wählen")

#title the page
st.title("Notenrechner light") 

version_msg = "Version "+str(__version__[0])+" "+str(__version__[1])+" , "+str(__version__[2])


st.markdown(version_msg)

st.markdown("Diese webversion bietet nicht die volle Funktionalität des Notenrechners. Für die Vollversion (ebenfalls kostenlos), gehen Sie auf den Link zum Projekt(siehe unten)")

st.markdown("## Dieses Projekt befindet sich noch in der Entwicklungsphase.")
st.markdown("- Link zu Github Projekt: https://github.com/fabischw/notenrechner-light")