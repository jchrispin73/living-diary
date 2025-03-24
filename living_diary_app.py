
import streamlit as st
import pandas as pd
import openai

# Load your CSV file
@st.cache_data
def load_data():
    return pd.read_csv("Living_Diary_Tool_Ready.csv")

df = load_data()

# Streamlit UI
st.set_page_config(page_title="Living Diary", page_icon="🌿")
st.title("🌿 Living Diary")
st.markdown("A soft place to land when you're feeling emotionally full or need support.")

user_input = st.text_area("What's on your mind today?", height=150)

if st.button("Reflect with me"):
    if user_input.strip() == "":
        st.warning("You can just say a few words or a feeling — there's no pressure.")
    else:
        # Match user input to themes
        def score_row(themes, user_text):
            if pd.isna(themes): return 0
            user_words = set(user_text.lower().split())
            theme_words = set(themes.lower().split(","))
            return len(user_words & theme_words)

        df["score"] = df["Themes"].apply(lambda x: score_row(x, user_input))
        match = df[df["score"] > 0].sort_values(by="score", ascending=False)

        if not match.empty:
            top = match.iloc[0]
            st.markdown(f"**Here you go — you can view or download _{top['Title']}_ using this link:**")
            st.markdown(f"[{top['Title']}]({top['Link']})", unsafe_allow_html=True)
            st.info("Even just one page can be enough today. You’re already doing something kind for yourself.")
        else:
            st.markdown("I didn’t find a resource that matches those exact feelings… and that’s okay.")
            st.markdown("Would you like a journaling prompt instead?")
            st.write("**Prompt:** What part of me is asking to be seen right now?")
