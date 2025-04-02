import streamlit as st
import pandas as pd
import random

# Import other pages
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

# Function to display home page content
def show_home_page():
    # Display the logo and leaf images here
    col7, col8 = st.columns([1, 0.9])  # Adjust for logo and leaf alignment
    with col7:
        st.image("FullLogo_Transparent_NoBuffer.png", width=180)  # Logo
    with col8:
        st.image("living diary soft place to land transparent.png", width=400)  # Leaf Design

    # Load the CSV for images and quotes
    df = pd.read_csv("Enhanced_Quote_Images_Living_Diary new.csv")

    # Choose a random row for the quote and image
    random_quote = df.sample(n=1).iloc[0]
    quote_text = random_quote['Quote']
    image_url = random_quote['Image Link']

    # Display the quote and image
    st.markdown(f"**{quote_text}**")  # Display the quote
    st.image(image_url, caption="Image for reflection", width=300)  # Display the image

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

# Default to home page if no button is clicked
if not home_button and not gratitude_button and not profile_button and not resources_button and not settings_button and not talk_button:
    home_button = True  # Automatically show the Home page if no other button is pressed
    show_home_page()  # Show Home page
