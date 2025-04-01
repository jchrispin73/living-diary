import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal

# Force sidebar open
st.set_page_config(page_title="Living Diary", layout="wide", initial_sidebar_state="expanded")

# Sidebar navigation
st.sidebar.title("🌿 Living Diary")
page = st.sidebar.radio("Navigate", ["Home", "Gratitude Journal"])

# Page router
if page == "Home":
    show_home_page()
elif page == "Gratitude Journal":
    show_gratitude_journal()
