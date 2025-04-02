import streamlit as st
import pandas as pd
import re
from home_page import show_home_page
from gratitude_journal import show_gratitude_journal
from profile_page import show_profile_page
from resources_page import show_resources_page
from settings_page import show_settings_page

# Set page config
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Ensure content is centered
    initial_sidebar_state="collapsed"  # Collapse sidebar by default
)

# Function to recommend resource based on user entry and mood
def recommend_resource(user_entry, mood):
    # Load your resource CSV
    df = pd.read_csv("Enhanced_Living_Diary_Index_UPDATED.csv")

    # Extract keywords from user entry
    user_words = set(re.findall(r'\w+', user_entry.lower()))

    def score_row(row):
        # Match keywords in user entry to the resource keywords
        keywords = str(row['Keywords']).lower().split(',')
        return len(set(map(str.strip, keywords)) & user_words)

    df['score'] = df.apply(score_row, axis=1)
    top_match = df[df['score'] > 0].sort_values(by='score', ascending=False).head(1)

    if not top_match.empty:
        resource = top_match.iloc[0]
        # Show the recommended resource (quote and download link)
        st.image(resource['Image'], width=300)
        st.markdown(f"**{resource['Quote']}**")
        st.markdown(f"[Download Resource PDF]({resource['Drive Link']})", unsafe_allow_html=True)

        # Save the recommended resource in session state
        if "recommended_resources" not in st.session_state:
            st.session_state.recommended_resources = []
        st.session_state.recommended_resources.append(resource)
    else:
        st.info("No matching resource found — but more are coming soon!")

# Function to display Home Page
def show_home_page():
    st.markdown("### 🌈 Here's a gentle journaling prompt for you:")
    
    # Mood selector
    mood = st.selectbox("Pick a mood to help match your reflection to a resource:", [
        "💤 Tired", "🌧️ Sad", "🌪️ Overwhelmed", "😌 Calm", "💖 Loved", "💔 Heartbroken",
        "🔥 Angry", "🧘 Grounded", "🌀 Anxious", "🌟 Inspired", "🙃 Confused", "🌈 Hopeful"
    ])
    
    # User entry text area
    user_entry = st.text_area("You can type below if you'd like to reflect:", placeholder="Start writing here...")
    
    # After submitting, display the recommended resource
    if st.button("💜 Save Entry"):
        if user_entry:
            recommend_resource(user_entry, mood)  # Recommend resource based on entry
            st.success("💜 Entry saved! You can return to it later.")

# Function to display Resources Page
def show_resources_page():
    if "recommended_resources" in st.session_state and st.session_state.recommended_resources:
        st.markdown("### Your Recommended Resources")
        for resource in st.session_state.recommended_resources:
            st.image(resource['Image'], width=300)
            st.markdown(f"**{resource['Quote']}**")
            st.markdown(f"[Download Resource PDF]({resource['Drive Link']})", unsafe_allow_html=True)
    else:
        st.info("No resources yet! Try journaling to get a recommendation.")

# Main layout setup with radio buttons for navigation
col1, col2, col3 = st.columns([1, 1, 1])  # Adjust columns for buttons

with col1:
    home_button = st.button("Home")

with col2:
    gratitude_button = st.button("Gratitude Journal")

with col3:
    profile_button = st.button("Profile")

# Second row for additional buttons
col4, col5, col6 = st.columns([1, 1, 1]) 

with col4:
    resources_button = st.button("Resources")

with col5:
    settings_button = st.button("Settings")

with col6:
    talk_button = st.button("Talk")

# Default page set to "Home"
if not home_button and not gratitude_button and not profile_button and not resources_button and not settings_button and not talk_button:
    home_button = True  # Set "Home" as default if no other button is pressed

# Display content based on which button is pressed
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
