import streamlit as st
import pandas as pd

st.set_page_config(page_title="Living Diary", page_icon="🌿")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

st.title("🌿 Living Diary")
st.markdown("_A soft place to land when you're feeling emotionally full or need support._")
import random

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

st.markdown(f"💭 _Today's gentle reflection:_ **{selected_prompt}**")
st.markdown("---")
mood = st.selectbox("How are you feeling today?", [
    "🌤 Calm",
    "🌧 Anxious",
    "🔥 Overwhelmed",
    "🌙 Reflective",
    "🌸 Grateful",
    "💤 Tired",
    "🎢 Mixed Emotions",
    "🌊 Heavy-hearted"
])

mood_messages = {
    "🌤 Calm": "May this calm stay with you gently through the day.",
    "🌧 Anxious": "You’re safe right now. One breath at a time.",
    "🔥 Overwhelmed": "It’s okay to pause. Everything doesn’t need to be solved at once.",
    "🌙 Reflective": "You’re allowed to explore your thoughts slowly, softly.",
    "🌸 Grateful": "That warmth you’re feeling is beautiful—let it grow.",
    "💤 Tired": "Rest is not a reward. It’s a right. You’ve earned softness today.",
    "🎢 Mixed Emotions": "It’s okay to hold more than one feeling at once. Be kind to them all.",
    "🌊 Heavy-hearted": "You’re not alone. Let your heart be held here for a moment."
}

st.info(mood_messages.get(mood, "You are allowed to feel exactly as you do."))

@st.cache_data
def load_data():
    return pd.read_csv("Living_Diary_Manual_Link_FINAL.csv")

df = load_data()

user_input = st.text_area("What's on your mind today?")

if st.button("Reflect with me") and user_input:
    user_input_lower = user_input.lower().split()

    best_match = None
    best_match_count = 0

    # Check all rows and count keyword matches
    for _, row in df.iterrows():
        themes = row['Themes'].lower().split(',')
        themes = [theme.strip() for theme in themes]
        match_count = sum(1 for word in user_input_lower if word in ' '.join(themes))

        if match_count > best_match_count:
            best_match = row
            best_match_count = match_count

    if best_match_count > 0:
        st.markdown(f"**Here you go — you can view or download _{best_match['Title']}_:**")
        st.markdown(f"[{best_match['Title']}]({best_match['Link']})")
        st.info("Even just one page can be enough today. You’re already doing something kind for yourself.")
    else:
        st.warning("I didn’t find a resource that matches those exact feelings… and that’s okay.")
        st.markdown("Would you like a journaling prompt instead?")
        st.markdown("**Prompt:** What part of me is asking to be seen right now?") 
