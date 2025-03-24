import streamlit as st
import pandas as pd

st.set_page_config(page_title="Living Diary", page_icon="🌿")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

st.title("🌿 Living Diary")
st.markdown("_A soft place to land when you're feeling emotionally full or need support._")

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
