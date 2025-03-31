import streamlit as st
from PIL import Image
import pandas as pd
import random

# 🔧 Page setup (must be first)
st.set_page_config(page_title="Living Diary", page_icon="🌿")

# 🌸 Display logo (centered and resized)
logo = Image.open("FullLogo_Transparent_NoBuffer.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=180)

# 🎨 Custom CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# 🧘 Title and intro
st.title("🌿 Living Diary")
st.markdown("_A soft place to land when you're feeling emotionally full or need support._")

# 🧠 Mood selector
st.markdown("#### How are you feeling right now?")
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

# ✍️ Journaling text box
st.markdown("You can type below if you'd like to reflect:")
user_entry = st.text_area(" ", height=200)

if user_entry:
    st.success("💖 Your words matter. Saved for this session — feel free to copy it into your journal.")
