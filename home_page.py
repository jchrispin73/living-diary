import streamlit as st

def show_home_page():
    # Add top navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness
    with col1:
        home_button = st.button("Home", use_container_width=True)
    with col2:
        gratitude_button = st.button("Gratitude Journal", use_container_width=True)
    with col3:
        profile_button = st.button("Profile", use_container_width=True)

    # Second row for other buttons (Resources, Settings, Talk)
    col4, col5, col6 = st.columns([1, 1, 1])  # Adjust proportions for responsiveness
    with col4:
        resources_button = st.button("Resources", use_container_width=True)
    with col5:
        settings_button = st.button("Settings", use_container_width=True)
    with col6:
        talk_button = st.button("Talk", use_container_width=True)

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
                <img src="https://raw.githubusercontent.com/jchrispin73/living-diary/main/leaf_image.png" width="50">
            </div>
            """, unsafe_allow_html=True
        )

    # Add the quote section below the logo
    st.markdown("### Living Diary")
    st.markdown("A soft place to land when you're feeling emotionally full or need support.")
    st.markdown("**daily quote here**")

    # Add the reflective image placeholder below the quote
    st.markdown("### Reflective Image")
    st.image("https://via.placeholder.com/150", caption="reflective image", use_column_width=True)

    # Optionally handle other logic for when buttons are clicked
    if home_button:
        # Show Home content or redirect here
        pass
    if gratitude_button:
        # Show Gratitude Journal content
        pass
    if profile_button:
        # Show Profile content
        pass
    if resources_button:
        # Show Resources content
        pass
    if settings_button:
        # Show Settings content
        pass
    if talk_button:
        # Show Talk content
        pass
