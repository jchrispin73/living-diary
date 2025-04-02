import streamlit as st
import pandas as pd
import re

# Set page config
st.set_page_config(page_title="Living Diary", layout="centered")

# Apply custom CSS (keep the layout and style as per requirements)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Set up the logo (adjusted size to be smaller and centered)
logo = "FullLogo_Transparent_NoBuffer.png"
st.image(logo, width=180)  # Logo size is set to 180px and centered by default

# Create columns for the buttons (these are positioned at the top)
col1, col2, col3 = st.columns([1, 1, 1])  # Equal-width columns for buttons

with col1:
    home_button = st.button("Home", use_container_width=True)

with col2:
    gratitude_button = st.button("Gratitude Journal", use_container_width=True)

with col3:
    profile_button = st.button("Profile", use_container_width=True)

# Add second row for additional buttons (Settings, Talk, Resources)
col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    resources_button = st.button("Resources", use_container_width=True)

with col5:
    settings_button = st.button("Settings", use_container_width=True)

with col6:
    talk_button = st.button("Talk", use_container_width=True)

# Ensure that home page is displayed if no other button is clicked
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

# Journaling Prompt Section: User selects prompt, mood, and writes reflection
prompts = [
    "If my heart could speak, what would it say?",
    "Right now, I am feeling...",
    "What’s one small step I could take to be kind to myself today?",
    "What emotion keeps showing up lately?",
    "How does my inner child feel today?"
]

selected_prompt = st.selectbox("🌈 Here's a gentle journaling prompt for you:", prompts)

mood = st.selectbox("Pick a mood to help match your reflection to a resource:", [
    "💤 Tired", "🌧️ Sad", "🌪️ Overwhelmed", "😌 Calm", "💖 Loved", "💔 Heartbroken",
    "🔥 Angry", "🧘 Grounded", "🌀 Anxious", "🌟 Inspired", "🙃 Confused", "🌈 Hopeful"
])

user_entry = st.text_area("You can type below if you'd like to reflect:", placeholder="Start writing here...")

# Save entries using session state
if "entries" not in st.session_state:
    st.session_state.entries = []

if st.button("💜 Save Entry"):
    st.session_state.entries.append({"mood": mood, "text": user_entry})
    st.success("💖 Entry saved. You can return to it in 'Previous Entries' later.")

# Resource matching from keywords
if user_entry:
    try:
        df = pd.read_csv("Enhanced_Living_Diary_Index_UPDATED.csv")
    except FileNotFoundError:
        st.error("🚫 The file 'Enhanced_Living_Diary_Index_UPDATED.csv' was not found. Make sure it's uploaded and named correctly.")
        st.stop()

    user_words = set(re.findall(r'\w+', user_entry.lower()))

    def score_row(row):
        keywords = str(row['Keywords']).lower().split(',')
        return len(set(map(str.strip, keywords)) & user_words)

    df['score'] = df.apply(score_row, axis=1)
    top_match = df[df['score'] > 0].sort_values(by='score', ascending=False).head(1)

    if not top_match.empty:
        resource = top_match.iloc[0]
        st.markdown("### Based on how you're feeling, this might help:")
        st.markdown(f"**{resource.get('Quote', 'Here’s something gentle to explore.')}**")
        st.markdown(f"📝 Here's a journal you might find supportive: [*{resource['File Name']}*]({resource['Drive Link']})", unsafe_allow_html=True)
    else:
        st.info("No matching resource found — but more are coming soon!")
