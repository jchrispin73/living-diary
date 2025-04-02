import streamlit as st
import pandas as pd
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal
from profile_page import show_profile_page  # Imported profile page
from resources_page import show_resources_page  # Imported resources page
from settings_page import show_settings_page  # Imported settings page

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Load the CSV file that contains the quotes and images
quotes_df = pd.read_csv('Enhanced_Quote_Images_Living_Diary new.csv')

# Function to get the quote and image for the selected mood
def get_mood_resource(mood):
    # Filter the CSV based on the selected mood
    filtered = quotes_df[quotes_df['mood'] == mood]

    if not filtered.empty:
        # Randomly select a quote and image based on the mood
        selected_resource = filtered.sample(1).iloc[0]
        quote = selected_resource['quote']
        image_path = selected_resource['image_path']
        return quote, image_path
    return None, None

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

# Default page set to "Home" if no other button is clicked
if not home_button and not gratitude_button and not profile_button and not resources_button and not settings_button and not talk_button:
    home_button = True  # Automatically show the Home page if no other button is pressed

# Display the content based on which button is pressed
if home_button:
    show_home_page()  # Show Home page
elif gratitude_button:
    show_gratitude_journal()  # Show Gratitude Journal page
    
    # After gratitude journal submission, show the matching resource
    mood = st.session_state.get('mood', None)
    if mood:
        quote, image_path = get_mood_resource(mood)
        if quote and image_path:
            # Show the quote and image right after journaling
            st.image(image_path, use_column_width=True)
            st.write(f"**Quote of the Day**: {quote}")
            
            # Save the entry to the Resources page
            st.session_state.resources = st.session_state.get('resources', [])
            st.session_state.resources.append({'quote': quote, 'image': image_path})
            show_resources_page()  # Navigate to Resources page
        else:
            st.write("No resource found for this mood.")
elif profile_button:
    show_profile_page()  # Show Profile page
elif resources_button:
    show_resources_page()  # Show Resources page
elif settings_button:
    show_settings_page()  # Show Settings page
