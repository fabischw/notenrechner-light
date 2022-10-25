import streamlit as st

st.set_page_config(page_title="app home page")


st.title("This is the app's home page")

if "inpt_prefered" not in st.session_state:
    st.session_state["inpt_prefered"] = "slider"


msg = "current inpt choice is",str(st.session_state["inpt_prefered"])
st.markdown(msg)