import streamlit as st
import pandas as pd
import openai
import os

# ⬇️ Must be the first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ⬇️ Optional: background image with fallback color
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("background_home.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: #f7f4fb;
}
[data-testid="stHeader"] {
    background-color: rgba(255, 255, 255, 0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ⬇️ Import other pages
from gratitude_journal import show_gratitude_journal
from profile_page import show_profile_page
from resources_page import show_resources_page
from settings_page import show_settings_page
from talk_page import show_talk_page

# ⬇️ Navigation buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    home_button = st.button("Home", use_container_width=True)
with col2:
    gratitude_button = st.button("Gratitude Journal", use_container_width=True)
with col3:
    profile_button = st.button("Profile", use_container_width=True)

col4, col5, col6 = st.columns([1, 1, 1])
with col4:
    resources_button = st.button("Resources", use_container_width=True)
with col5:
    settings_button = st.button("Settings", use_container_width=True)
with col6:
    talk_button = st.button("Talk", use_container_width=True)

# ⬇️ Home page content
def show_home_page():
    col7, col8 = st.columns([1, 0.9])
    with col7:
        st.image("FullLogo_Transparent_NoBuffer.png", width=180)
    with col8:
        st.image("living diary soft place to land transparent.png", width=300)

    df = pd.read_csv("Enhanced_Quote_Images_Living_Diary_new.csv")
    df.columns = df.columns.str.strip().str.lower()
    df["mood"] = df["mood"].astype(str).str.strip().str.lower()
    df["hastext"] = df["hastext"].astype(str).str.lower() == "true"

    if "selected_mood" in st.session_state:
        mood = st.session_state["selected_mood"].strip().lower()
        filtered = df[df["mood"] == mood]

        if not filtered.empty:
            selected_row = filtered.sample(n=1).iloc[0]
            quote = selected_row["quote"]
            author = selected_row["author"]
            image_url = selected_row["image link"]
            has_text = selected_row["hastext"]

            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                st.image(image_url, caption="Image for reflection", use_container_width=False, width=400)

            if not has_text:
                st.markdown(f"### “{quote}”")
                st.markdown(f"**— {author}**")
        else:
            st.info("No matching quote found for your mood. Try journaling again.")
    else:
        st.info("Start by journaling to see your daily quote and reflection image.")

# ⬇️ Page navigation logic
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

if home_button:
    st.session_state["current_page"] = "Home"
elif gratitude_button:
    st.session_state["current_page"] = "Gratitude"
elif profile_button:
    st.session_state["current_page"] = "Profile"
elif resources_button:
    st.session_state["current_page"] = "Resources"
elif settings_button:
    st.session_state["current_page"] = "Settings"
elif talk_button:
    st.session_state["current_page"] = "Talk"

if st.session_state["current_page"] == "Home":
    show_home_page()
elif st.session_state["current_page"] == "Gratitude":
    show_gratitude_journal()
elif st.session_state["current_page"] == "Profile":
    show_profile_page()
elif st.session_state["current_page"] == "Resources":
    show_resources_page()
elif st.session_state["current_page"] == "Settings":
    show_settings_page()
elif st.session_state["current_page"] == "Talk":
    show_talk_page()
