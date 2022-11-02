
# ! This file aims to reporduce which I experienced using st.radio's on_change paramater
import streamlit as st


st.set_page_config(page_title="different page of the app")


st.title("This is a different app page")



number_inpt_choice = None

# function to update the settings
def update_settings(type):
    # st.session_state.number_inpt_choice
    st.markdown("this should only run on change!!")# ! debug statement -> this should only be outputted when the value is actually changed !
    if type == "number_input":#updating the number input
        st.markdown("another debug statement") # ! debug statement
        if st.session_state.number_inpt_choice != st.session_state["inpt_prefered"] and number_inpt_choice != None:
            st.markdown("value changed") # ! debug statement
            st.session_state["inpt_prefered"] = st.session_state.number_inpt_choice






current_choice = None
choose_prefered_inpt_setting = True

if st.session_state.get("inpt_prefered") == "slider":
    current_choice = 1
elif st.session_state.get("inpt_prefered") == "input_box":
    current_choice = 0
else:
    choose_prefered_inpt_setting = False
    st.markdown("an error occured")


# user choosing input settings
if choose_prefered_inpt_setting:
    number_inpt_choice = st.radio("Choose an input method",("input_box","slider"),index=current_choice,on_change=update_settings, args=("number_input",),key="number_inpt_choice")