import streamlit as st
from PIL import Image
import pandas as pd
import random

# 🌿 Set page config first
st.set_page_config(page_title="Living Diary", page_icon="🌿", layout="centered")

# 🌸 Load and center logo
logo = Image.open("FullLogo_Transparent_NoBuffer.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=180)

# 🎨 Load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# 💜 Title and subtitle
st.title("🌿 Living Diary")
st.markdown("_A soft place to land when you're feeling emotionally full or need support._")

# 💬 Mood selector
st.markdown("#### How are you feeling right now?")
mood = st.selectbox(
    "Choose your mood:",
    ["Calm", "Sad", "Overwhelmed", "Anxious", "Hopeful", "Tired", "Grounded"]
)

# 📚 Load updated CSV with mood-based tags
df = pd.read_csv("Living_Diary_Complete_Index_with_Images (1).csv")

# 🔍 Filter based on mood tag match
matched_rows = df[df['Moods'].str.contains(mood, case=False, na=False)]

# 🎲 Pick a random matching entry
if not matched_rows.empty:
    selected = matched_rows.sample(1).iloc[0]
    quote = selected['Quote']
    image_url = selected['Image Link']
    download_link = selected['Download Link']
else:
    quote = "No matching quote found for this mood."
    image_url = ""
    download_link = ""

# 🌈 Display journaling prompt
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

# 📸 Show quote image + daily quote
if image_url:
    st.image(image_url, use_column_width=True)

st.markdown(f"**💭 Daily Quote:** _{quote}_")

# ✍️ Prompt + journal input
st.markdown("### Here's a gentle journaling prompt for you:")
st.markdown(f"🌈 *{selected_prompt}*")
st.markdown("You can type below if you'd like to reflect:")

user_entry = st.text_area(" ", height=200)

if user_entry:
    st.success("💖 Your words matter. Entry saved locally for this session.")
    if "entries" not in st.session_state:
        st.session_state.entries = []
    st.session_state.entries.append(user_entry)

# 📎 Resource download link
if download_link:
    st.markdown(f"[📥 Download a matching resource PDF]({download_link})")

# 🔁 Try another resource
if st.button("🔄 Try a new one"):
    st.experimental_rerun()

