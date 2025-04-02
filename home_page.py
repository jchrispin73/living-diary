import streamlit as st

# Centered layout
st.set_page_config(
    layout="centered",  # Center the layout
    initial_sidebar_state="collapsed"  # Collapse the sidebar by default
)

# Remove the sidebar completely
st.sidebar.empty()

def show_home_page():
    # Centered logo
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/jchrispin73/living-diary/main/FullLogo_Transparent_NoBuffer.png" width="180">
    </div>
    """, unsafe_allow_html=True)

    # Main content for the "Home" page
    st.markdown("### Here's a gentle journaling prompt for you:")

    prompt = st.selectbox("Pick a prompt", [
        "If my heart could speak, what would it say?",
        "Right now, I am feeling...",
        "What emotion keeps showing up lately?"
    ])

    # Mood selector
    mood = st.selectbox("Pick a mood to help match your reflection to a resource:", [
        "😴 Tired", "😞 Sad", "😟 Overwhelmed", "😊 Calm", "❤️ Loved", "💔 Heartbroken",
        "😠 Angry", "🌱 Grounded", "😓 Anxious", "💡 Inspired", "🤔 Confused", "🌈 Hopeful"
    ])

    # Text input for reflection
    journal = st.text_area("You can type below if you'd like to reflect:")

    # Save entry button
    save_button = st.button("Save Entry", use_container_width=True)

    # Action when the save button is clicked
    if save_button:
        # Logic to save the journal entry
        st.success("Entry saved! You can return to it later.")

