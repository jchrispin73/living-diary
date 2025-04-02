import streamlit as st
from gratitude_journal import show_gratitude_journal
from profile_page import show_profile_page
from resources_page import show_resources_page
from settings_page import show_settings_page

# Define the layout and buttons
st.set_page_config(page_title="Living Diary", layout="centered")

# Button layout for top navigation
col1, col2, col3 = st.columns([1, 1, 1]) 
with col1:
    home_button = st.button("Home", use_container_width=True)
with col2:
    gratitude_button = st.button("Gratitude Journal", use_container_width=True)
with col3:
    profile_button = st.button("Profile", use_container_width=True)

# Add second row for next set of buttons
col4, col5, col6 = st.columns([1, 1, 1]) 
with col4:
    resources_button = st.button("Resources", use_container_width=True)
with col5:
    settings_button = st.button("Settings", use_container_width=True)
with col6:
    talk_button = st.button("Talk", use_container_width=True)

# Page flow based on the button clicked
if home_button:
    show_home_page()  # Show the home page content
elif gratitude_button:
    show_gratitude_journal()  # Show Gratitude Journal page
elif profile_button:
    show_profile_page()  # Show Profile page
elif resources_button:
    show_resources_page()  # Show Resources page
elif settings_button:
    show_settings_page()  # Show Settings page

# Show a placeholder content for home page if no button is pressed
if not home_button and not gratitude_button and not profile_button and not resources_button and not settings_button and not talk_button:
    show_home_page()  # Default to home page if no other button is clicked
