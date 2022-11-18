"""
this script starts the easy_debug streamlit app
"""


import streamlit as st
import os

def run():
    """
    running the easy-debug webapp (will launch in new windows)
    - makes it easy to debug in production and do things like resets and generating test data
    """
    os.system("streamlit run easy_debug.py")