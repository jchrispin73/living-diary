import pandas as pd
import streamlit as st

def show_home_page():
    # Add top navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness
    with col1:
        home_button = st.button("Home", use_container_width=True, key="home_button")
    with col2:
        gratitude_button = st.button("Gratitude Journal", use_container_width=True, key="gratitude_button")
    with col3:
        profile_button = st.button("Profile", use_container_width=True, key="profile_button")

    # Second row for other buttons (Resources, Settings, Talk)
    col4, col5, col6 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness
    with col4:
        resources_button = st.button("Resources", use_container_width=True, key="resources_button")
    with col5:
        settings_button = st.button("Settings", use_container_width=True, key="settings_button")
    with col6:
        talk_button = st.button("Talk", use_container_width=True, key="talk_button")

    # Add logo and leaf side by side with a small gap
    col7, col8 = st.columns([1, 0.2, 1])  # Adjust for logo and leaf alignment
    with col7:
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://raw.githubusercontent.com/jchrispin73/living-diary/main/FullLogo_Transparent_NoBuffer.png" width="100">
            </div>
            """, unsafe_allow_html=True
        )
    with col8:
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://raw.githubusercontent.com/jchrispin73/living-diary/main/living%20diary%20soft%20place%20to%20land%20transparent.png" width="50">
            </div>
            """, unsafe_allow_html=True
        )

    # Add the quote section below the logo
    st.markdown("### Living Diary")
    st.markdown("A soft place to land when you're feeling emotionally full or need support.")
    st.markdown("**daily quote here**")  # Placeholder for daily quote

    # Add the reflective image placeholder below the quote
    st.markdown("### Reflective Image")
    st.image("https://via.placeholder.com/150", caption="reflective image", use_column_width=True)

    # Optionally handle other logic for when buttons are clicked
    if home_button:
        pass  # Logic for home page
    if gratitude_button:
        pass  # Logic for gratitude journal
    if profile_button:
        pass  # Logic for profile page
    if resources_button:
        pass  # Logic for resources
    if settings_button:
        pass  # Logic for settings page
    if talk_button:
        pass  # Logic for talk feature
