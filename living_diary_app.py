import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Main navigation buttons (displayed next to each other)
col1, col2, col3, col4 = st.columns(4)

with col1:
    home_button = st.button("Home")

with col2:
    gratitude_button = st.button("Gratitude Journal")

with col3:
    profile_button = st.button("Profile")

with col4:
    resources_button = st.button("Resources")

# Additional button for Settings and Talk functionality
settings_button = st.button("Settings")
talk_button = st.button("Talk")

# Default page set to "Home"
if not home_button and not gratitude_button:
    home_button = True  # Set "Home" as default if no button is pressed yet

# Display the content based on which button is pressed
if home_button:
    show_home_page()
elif gratitude_button:
    show_gratitude_journal()

# Future functions for new buttons
if profile_button:
    st.write("Profile content goes here")

if resources_button:
    st.write("Resources content goes here")

if settings_button:
    st.write("Settings content goes here")

if talk_button:
    # Logic to trigger the GPT conversation
    st.write("Starting conversation with GPT...")
    # (You would link your GPT functionality here)
