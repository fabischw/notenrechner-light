# this page is meant to act as a content library, link to external resources etc.

import streamlit as st
import PIL
import pathlib

#set the page icon
here = pathlib.Path(__file__)
resources_dir = here.parent.parent / 'resources'
icon = resources_dir = resources_dir / 'page_icon.ico'
icon_load = PIL.Image.open(icon)
#set the page title
st.set_page_config(page_title="Bibliothek",page_icon=icon_load)


#sidebar
st.sidebar.success("Funktion / Modul wählen")


st.title("Bibliothek")
st.markdown("## Diese Seite dient als Bibliothek für externe Resourcen, Quellen etc.")

with st.expander("Lehrpläne"):
    st.markdown("#### [Baden-Württemberg](http://www.bildungsplaene-bw.de/,Lde/LS/BP2016BW/ALLG#FaecherGS)")
    st.markdown("#### [Bayern](http://www.isb.bayern.de/schulartspezifisches/lehrplan/)")
    st.markdown("#### [Berlin](https://bildungsserver.berlin-brandenburg.de/unterricht/rahmenlehrplaene/)")
    st.markdown("#### [Brandenburg](https://bildungsserver.berlin-brandenburg.de/unterricht/rahmenlehrplaene/)")
    st.markdown("#### [Hamburg](https://www.hamburg.de/bildungsplaene)")
    st.markdown("#### [Hessen](https://kultusministerium.hessen.de/Unterricht/Kerncurricula-und-Lehrplaene/Kerncurricula)")
    st.markdown("#### [Mecklenburg-Vorpommern](https://www.bildung-mv.de/lehrer/schule-und-unterricht/faecher-und-rahmenplaene/)")
    st.markdown("#### [Niedersachsen](https://cuvo.nibis.de/cuvo.php)")
    st.markdown("#### [Nordrhein-Westfalen](https://www.schulentwicklung.nrw.de/lehrplaene/)")
    st.markdown("#### [Rheinland-Pfalz](https://lehrplaene.bildung-rp.de)")
    st.markdown("#### [Saarland](https://www.saarland.de/mbk/DE/portale/bildungsserver/themen/unterricht-und-bildungsthemen/lehrplaenehandreichungen/lehrplaenehandreichungen_node.html)")
    st.markdown("#### [Sachsen](v)")
    st.markdown("#### [Sachsen-Anhalt](https://lisa.sachsen-anhalt.de/unterricht/lehrplaenerahmenrichtlinien/)")
    st.markdown("#### [Schleswig-Holstein](https://fachportal.lernnetz.de/sh/fachanforderungen.html)")
    st.markdown("#### [Thüringen](https://www.schulportal-thueringen.de/web/guest/lehrplaene)")

