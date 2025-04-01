import streamlit as st
from PIL import Image
import pandas as pd
import random
import re

# Load logo
logo = Image.open("FullLogo_Transparent_NoBuffer.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=180)

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# App title and intro
st.title("🌿 Living Diary")
st.markdown("_A soft place to land when you're feeling emotionally full or need support._")

# Mood selection
st.markdown("#### How are you feeling right now?")
mood = st.selectbox(
    "Choose your mood:",
    ["🌤️ Calm", "🌧️ Sad", "⛅ Overwhelmed", "🌪️ Anxious", "☀️ Hopeful", "🌙 Tired", "🪷 Grounded"]
)

# Gentle journaling prompt
prompts = [
    "What part of me is asking to be seen today?",
    "How can I offer myself more kindness in this moment?",
    "What emotions have been sitting with me lately?",
    "If my heart could speak, what would it say?",
    "Where in my body am I holding tension or softness?",
    "What would it feel like to fully accept myself today?",
    "What am I ready to let go of right now?"
]
selected_prompt = random.choice(prompts)

st.markdown("### Here's a gentle journaling prompt for you:")
st.markdown(f"🌈 *{selected_prompt}*")

# Journal input box
st.markdown("You can type below if you'd like to reflect:")
user_entry = st.text_area(" ", height=200)

# Save journal entry
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
        st.image(resource['Image_Link'], width=300)
        st.markdown(f"**{resource['Quote']}**")
        st.markdown(f"[Download Resource PDF]({resource['PDF_Link']})", unsafe_allow_html=True)
    else:
        st.info("No matching resource found — but more are coming soon!")

# Display previous entries
if st.session_state.entries:
    st.markdown("### Previous Entries")
    for i, e in enumerate(reversed(st.session_state.entries)):
        st.markdown(f"**Mood:** {e['mood']}\n📖 _{e['text']}_")
        st.markdown("---")
