import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Remove the sidebar completely
st.sidebar.empty()

# Use st.columns to manage layout
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # Adjust proportions for responsiveness

with col1:
    home_button = st.button("Home")

with col2:
    gratitude_button = st.button("Gratitude Journal")

with col3:
    profile_button = st.button("Profile")

with col4:
    resources_button = st.button("Resources")

# Place 'Settings' and 'Talk' buttons beneath the first row on smaller screens
col5, col6 = st.columns([1, 1])

with col5:
    settings_button = st.button("Settings")

with col6:
    talk_button = st.button("Talk")

# Default page set to "Home"
if not home_button and not gratitude_button:
    home_button = True  # Set "Home" as default if no button is pressed yet

# Display the content based on which button is pressed
if home_button:
    show_home_page()
elif gratitude_button:
    show_gratitude_journal()
