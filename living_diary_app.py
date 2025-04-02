import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal
from profile_page import show_profile_page
from resources_page import show_resources_page
from settings_page import show_settings_page

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Use st.columns to manage layout
col1, col2, col3 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness

with col1:
    home_button = st.button("Home", use_container_width=True, key="home")

with col2:
    gratitude_button = st.button("Gratitude Journal", use_container_width=True, key="gratitude")

with col3:
    profile_button = st.button("Profile", use_container_width=True, key="profile")

# Add second row for the next set of buttons (Settings, Talk, Resources)
col4, col5, col6 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness

with col4:
    resources_button = st.button("Resources", use_container_width=True, key="resources")

with col5:
    settings_button = st.button("Settings", use_container_width=True, key="settings")

with col6:
    talk_button = st.button("Talk", use_container_width=True, key="talk")

# Handle button presses and display respective content
if home_button:
    show_home_page()  # Show Home page
elif gratitude_button:
    show_gratitude_journal()  # Show Gratitude Journal page
elif profile_button:
    show_profile_page()  # Show Profile page
elif resources_button:
    show_resources_page()  # Show Resources page
elif settings_button:
    show_settings_page()  # Show Settings page
elif talk_button:
    # Show the talk page if needed
    pass
