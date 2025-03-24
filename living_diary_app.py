import streamlit as st
import pandas as pd

st.set_page_config(page_title="Living Diary", page_icon="🌿")

st.title("🌿 Living Diary")
st.markdown("_A soft place to land when you're feeling emotionally full or need support._")

@st.cache_data
def load_data():
    return pd.read_csv("Living_Diary_Manual_Link_FINAL.csv")

df = load_data()

user_input = st.text_area("What's on your mind today?")

if st.button("Reflect with me") and user_input:
    user_input_lower = user_input.lower()

    # Try to find the best matching resource
    match = None
    for index, row in df.iterrows():
        themes = row['Themes'].lower()
        if any(word in themes for word in user_input_lower.split()):
            match = row
            break

    if match is not None:
        st.markdown("**Here you go — you can view or download _{}_:**".format(match["Title"]))
        st.markdown(f"[{match['Title']}]({match['Link']})")
        st.info("Even just one page can be enough today. You’re already doing something kind for yourself.")
    else:
        st.warning("I didn’t find a resource that matches those exact feelings… and that’s okay.")
        st.markdown("Would you like a journaling prompt instead?")
        st.markdown("**Prompt:** What part of me is asking to be seen right now?")


