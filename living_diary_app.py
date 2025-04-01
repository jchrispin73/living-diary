import streamlit as st
from PIL import Image
import pandas as pd
import random
import re

# 🌸 Display logo
logo = Image.open("FullLogo_Transparent_NoBuffer.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=180)

# 🎨 Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# 🧘 Title and intro
st.title("🌿 Living Diary")
st.markdown("_A soft place to land when you're feeling emotionally full or need support._")

# 🧠 Mood selector
st.markdown("### How are you feeling right now?")
mood = st.selectbox(
    "Choose your mood:",
    ["🌤️ Calm", "🌧️ Sad", "⛅ Overwhelmed", "🌪️ Anxious", "☀️ Hopeful", "🌙 Tired", "🪷 Grounded"]
)

# ✨ Journaling prompt
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
st.markdown("You can type below if you'd like to reflect:")

# ✍️ Journal input
entry = st.text_area(" ", height=200)
save = st.button("💜 Save Entry")

if "entries" not in st.session_state:
    st.session_state.entries = []

if save and entry:
    st.session_state.entries.append({"mood": mood, "text": entry})
    st.success("💖 Entry saved. You can return to it in 'Previous Entries' later.")

# 📂 Load resource CSV
df = pd.read_csv("Living_Diary_Complete_Index_with_Images (1).csv")

# 🔍 Match mood to resource
clean_mood = re.sub(r"[^\w\s]", "", mood).strip().lower()
st.write(f"🔎 Debug: Matching mood as `{clean_mood}`")  # ← Debug line

matched_resource = df[df["Folder"].str.lower().str.strip() == clean_mood]

if not matched_resource.empty:
    resource = matched_resource.sample(1).iloc[0]
    st.markdown("### Based on how you're feeling, this might help:")
    st.image(resource["Image_Link"], width=300)
    st.markdown(f"**{resource['Quote']}**")
    st.markdown(f"[Download Resource PDF]({resource['PDF_Link']})", unsafe_allow_html=True)
else:
    st.info("No matching resource found — but more are coming soon!")

# 🕰️ Previous entries
if st.session_state.entries:
    st.markdown("### Previous Entries")
    for i, e in enumerate(reversed(st.session_state.entries)):
        st.markdown(f"**Mood:** {e['mood']}  \n🟪 *{e['text']}*")
        st.markdown("---")
