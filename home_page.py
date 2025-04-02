import streamlit as st

def show_home_page():
    # Page layout
    st.set_page_config(page_title="Living Diary", layout="centered", initial_sidebar_state="collapsed")
    
    # Create columns for the page structure
    col1, col2 = st.columns([1, 1])

    with col1:
        # Logo and Leaf Image side by side
        st.image("images/Living_Diary_logo.png", width=180)  # Replace with actual path to the logo
    with col2:
        # Leaf image (adjust the path and size)
        st.image("images/living_diary_soft_place_to_land_transparent.png", width=250)  # Adjust as needed

    # Title and description
    st.markdown("### Living Diary")
    st.markdown("A soft place to land when you're feeling emotionally full or need support.")
    
    # Daily quote and image section (static placeholder for now)
    st.markdown("**daily quote here**")  # You will replace this with dynamic content later
    st.image("images/reflective_image_placeholder.png", caption="reflective image", width=400)  # Placeholder image

    # Buttons for navigation (as per the design)
    col3, col4, col5 = st.columns([1, 1, 1])
    
    with col3:
        if st.button("Gratitude Journal"):
            # Functionality for Gratitude Journal
            st.write("Gratitude Journal clicked!")  # Replace with actual function or navigation
    
    with col4:
        if st.button("Talk"):
            # Functionality for Talk
            st.write("Talk clicked!")  # Replace with actual function or navigation
    
    with col5:
        if st.button("Resources"):
            # Functionality for Resources
            st.write("Resources clicked!")  # Replace with actual function or navigation
