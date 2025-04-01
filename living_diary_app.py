import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)
# Create the buttons in a responsive layout
# For smaller screens, they will stack; for larger screens, they will be in a row.
button_columns = st.columns(4)

# Use the first row for the main buttons
with button_columns[0]:
    home_button = st.button("Home")
    
with button_columns[1]:
    gratitude_button = st.button("Gratitude Journal")

with button_columns[2]:
    profile_button = st.button("Profile")

with button_columns[3]:
    resources_button = st.button("Resources")

# Use the second row for the "Settings" and "Talk" buttons
button_columns_2 = st.columns(2)

with button_columns_2[0]:
    settings_button = st.button("Settings")

with button_columns_2[1]:
    talk_button = st.button("Talk")

# Default page set to "Home"
if not home_button and not gratitude_button:
    home_button = True  # Set "Home" as default if no button is pressed yet

# Display the content based on which button is pressed
if home_button:
    show_home_page()
elif gratitude_button:
    show_gratitude_journal()
