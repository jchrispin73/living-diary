import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal
from profile_page import show_profile_page  # Placeholder for Profile page logic
from resources_page import show_resources_page  # Placeholder for Resources page logic
from settings_page import show_settings_page  # Placeholder for Settings page logic
from talk_page import show_talk_page  # Placeholder for Talk page logic

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Use st.columns to manage layout
col1, col2, col3 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness

# Main navigation buttons (displayed next to each other)
with col1:
    home_button = st.button("Home", use_container_width=True)

with col2:
    gratitude_button = st.button("Gratitude Journal", use_container_width=True)

with col3:
    profile_button = st.button("Profile", use_container_width=True)

# Add second row for the next set of buttons (Settings, Talk, Resources)
col4, col5, col6 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness

with col4:
    resources_button = st.button("Resources", use_container_width=True)

with col5:
    settings_button = st.button("Settings", use_container_width=True)

with col6:
    talk_button = st.button("Talk", use_container_width=True)

# Default page set to "Home"
if not home_button and not gratitude_button and not profile_button and not resources_button and not settings_button and not talk_button:
    home_button = True  # Set "Home" as default if no button is pressed yet

# Display the content based on which button is pressed
if home_button:
    show_home_page()
elif gratitude_button:
    show_gratitude_journal()
elif profile_button:
    show_profile_page()  # Call the Profile page function
elif resources_button:
    show_resources_page()  # Call the Resources page function
elif settings_button:
    show_settings_page()  # Call the Settings page function
elif talk_button:
    show_talk_page()  # Call the Talk page function
