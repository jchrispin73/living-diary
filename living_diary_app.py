import streamlit as st
import pandas as pd
import re

# Set page config
st.set_page_config(page_title="Living Diary", layout="centered")

# Apply custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Load logo
logo = "FullLogo_Transparent_NoBuffer.png"
st.image(logo, width=250)

# Prompts for journaling
prompts = [
    "If my heart could speak, what would it say?",
    "Right now, I am feeling...",
    "What’s one small step I could take to be kind to myself today?",
    "What emotion keeps showing up lately?",
    "How does my inner child feel today?"
]

selected_prompt = st.selectbox("🌈 Here's a gentle journaling prompt for you:", prompts)

# Mood selector
mood = st.selectbox("Pick a mood to help match your reflection to a resource:", [
    "💤 Tired", "🌧️ Sad", "🌪️ Overwhelmed", "😌 Calm", "💖 Loved", "💔 Heartbroken",
    "🔥 Angry", "🧘 Grounded", "🌀 Anxious", "🌟 Inspired", "🙃 Confused", "🌈 Hopeful"
])

# User entry text area
user_entry = st.text_area("You can type below if you'd like to reflect:", placeholder="Start writing here...")

# Save entries using session state
if "entries" not in st.session_state:
    st.session_state.entries = []

if st.button("💜 Save Entry"):
    st.session_state.entries.append({"mood": mood, "text": user_entry})
    st.success("💖 Entry saved. You can return to it in 'Previous Entries' later.")

# Resource matching from keywords
if user_entry:
    df = pd.read_csv("Enhanced_Living_Diary_Index.csv")

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
        st.markdown(f"[Download Resource PDF]({resource['Drive Link']})", unsafe_allow_html=True)
    else:
        st.info("No matching resource found — but more are coming soon!")
