import streamlit as st
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Adjust the spacing for the buttons (placed next to each other)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # Equal width for each column

with col1:
    home_button = st.button("Home")

with col2:
    gratitude_button = st.button("Gratitude Journal")

with col3:
    profile_button = st.button("Profile")

with col4:
    resources_button = st.button("Resources")

# Add the "Talk" button
col5, col6 = st.columns([1, 1])  # This ensures the new buttons are placed in a separate line if needed
with col5:
    settings_button = st.button("Settings")

with col6:
    talk_button = st.button("Talk")

# Ensure buttons stack in mobile view
st.markdown(
    """
    <style>
    @media screen and (max-width: 800px) {
        .stButton > button {
            display: block;
            width: 100%;
            margin: 10px 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Default page set to "Home"
if not home_button and not gratitude_button:
    home_button = True  # Set "Home" as default if no button is pressed yet

# Display the content based on which button is pressed
if home_button:
    show_home_page()
elif gratitude_button:
    show_gratitude_journal()
