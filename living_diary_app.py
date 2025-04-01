import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal

# ✅ Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Remove the sidebar completely to make navigation clearer
st.sidebar.empty()

# Main navigation - Using radio buttons for easy page switching
page = st.radio("Navigate", ["Home", "Gratitude Journal"])

# Display the content based on the radio button selection
if page == "Home":
    show_home_page()
elif page == "Gratitude Journal":
    show_gratitude_journal()
