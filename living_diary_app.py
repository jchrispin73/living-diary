import streamlit as st
import pandas as pd
import random
import datetime
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

# Path to your CSV file (adjust based on actual file location)
csv_file_path = 'Enhanced_Quote_Images_Living_Diary new.csv'
quotes_df = pd.read_csv(csv_file_path)

# Ensure the CSV has the expected columns (mood | quote | image)
# You can display the dataframe here to ensure it's loaded correctly
# st.write(quotes_df)

# Get the current date to display a new quote/image daily
today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")

# Check if the current date already exists in session state to ensure the quote is updated daily
if 'quote_date' not in st.session_state or st.session_state.quote_date != today_str:
    # Randomly pick a quote/image
    random_quote = quotes_df.sample(n=1).iloc[0]

    # Save the selected quote and image in session state
    st.session_state.selected_quote = random_quote['quote']
    st.session_state.selected_image = random_quote['image']
    st.session_state.quote_date = today_str
else:
    # Use the already saved quote and image from the session state
    random_quote = {
        'quote': st.session_state.selected_quote,
        'image': st.session_state.selected_image
    }

# Display the quote and image on the main page
st.image(random_quote['image'], width=300)  # Display image (adjust the width as needed)
st.write(f"**Quote of the Day:** {random_quote['quote']}")

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
elif profile_button:
    show_profile_page()  # Show Profile page
elif resources_button:
    show_resources_page()  # Show Resources page
elif settings_button:
    show_settings_page()  # Show Settings page
