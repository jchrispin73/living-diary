import streamlit as st
import pandas as pd

# Import other pages
from gratitude_journal import show_gratitude_journal
from profile_page import show_profile_page
from resources_page import show_resources_page
from settings_page import show_settings_page

# Must be the very first Streamlit command
st.set_page_config(
    page_title="Living Diary",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Navigation buttons - TOP OF PAGE (unchanged)
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

# Function to display Home Page
def show_home_page():
    # Header with buttons (keeping this part the same as before)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.button("Home", use_container_width=True)
    with col2:
        st.button("Gratitude Journal", use_container_width=True)
    with col3:
        st.button("Profile", use_container_width=True)

    col4, col5, col6 = st.columns([1, 1, 1])
    with col4:
        st.button("Resources", use_container_width=True)
    with col5:
        st.button("Settings", use_container_width=True)
    with col6:
        st.button("Talk", use_container_width=True)

    # Display logos below the buttons
    col7, col8 = st.columns([1, 0.9])
    with col7:
        st.image("FullLogo_Transparent_NoBuffer.png", width=180)
    with col8:
        st.image("living diary soft place to land transparent.png", width=400)

    # Load and clean the CSV
    df = pd.read_csv("Enhanced_Quote_Images_Living_Diary_new.csv")
    df.columns = df.columns.str.strip().str.lower()
    df["mood"] = df["mood"].astype(str).str.strip().str.lower()
    df["hastext"] = df["hastext"].astype(str).str.lower() == "true"

    # Check for mood in session
    if "selected_mood" in st.session_state:
        mood = st.session_state["selected_mood"].strip().lower()
        filtered = df[df["mood"] == mood]

        if not filtered.empty:
            selected_row = filtered.sample(n=1).iloc[0]
            quote = selected_row["quote"]
            author = selected_row["author"]
            image_url = selected_row["image link"]
            has_text = selected_row["hastext"]

            # Show image under the header (image comes below logo section)
            st.image(image_url, caption="Image for reflection", use_container_width=True, width=500)

            # Only show quote and author if the image does NOT already have text on it
            if not has_text:
                st.markdown(f"### “{quote}”")
                st.markdown(f"**— {author}**")
        else:
            st.info("No matching quote found for your mood. Try journaling again.")
    else:
        st.info("Start by journaling to see your daily quote and reflection image.")

# Track current page across reruns
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Update page when buttons are clicked
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

# Show the correct page based on state
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
    st.markdown("**Talk feature coming soon.**")
