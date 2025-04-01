import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal

# Set up the page configuration without the sidebar
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Center content
    initial_sidebar_state="collapsed"
)

# Using columns to manage the button layout in a responsive way
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # Equal width for desktop

with col1:
    home_button = st.button("Home")

with col2:
    gratitude_button = st.button("Gratitude Journal")

with col3:
    profile_button = st.button("Profile")

with col4:
    resources_button = st.button("Resources")

# Creating a new row for 'Settings' and 'Talk' buttons, ensuring responsiveness
col5, col6 = st.columns([1, 1])  # Adjusting for smaller screens

with col5:
    settings_button = st.button("Settings")

with col6:
    talk_button = st.button("Talk")

# Default page set to "Home" if no button is pressed
if not home_button and not gratitude_button:
    home_button = True  # Set "Home" as default if no button is pressed yet

# Display the content based on which button is pressed
if home_button:
    show_home_page()
elif gratitude_button:
    show_gratitude_journal()
