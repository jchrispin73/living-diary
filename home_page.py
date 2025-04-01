import streamlit as st

# ✅ Must be at the top, before any Streamlit commands
st.set_page_config(
    page_title="Living Diary",
    layout="centered",  # Center the layout
    initial_sidebar_state="collapsed"  # Collapse the sidebar by default
)

# Remove the sidebar completely
st.sidebar.empty()

def show_home_page():
    # Radio buttons for navigation at the top
    page = st.radio("Navigate", ["Home", "Gratitude Journal"], key="nav")

    # Centered logo
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/jchrispin73/living-diary/main/FullLogo_Transparent_NoBuffer.png" width="300">
        </div>
        """,
        unsafe_allow_html=True
    )

    if page == "Home":
        st.markdown("### 🌈 Here's a gentle journaling prompt for you:")
        prompt = st.selectbox("Pick a prompt", [
            "If my heart could speak, what would it say?",
            "Right now, I am feeling...",
            "What emotion keeps showing up lately?"
        ])

        mood = st.selectbox("Pick a mood to help match your reflection to a resource:", [
            "😌 Calm", "😴 Tired", "😔 Sad", "😡 Angry", "😊 Joyful"
        ])

        journal = st.text_area("You can type below if you'd like to reflect:")

        if st.button("💜 Save Entry"):
            st.success("💜 Entry saved! You can return to it later.")

    elif page == "Gratitude Journal":
        st.markdown("### ✨ Gratitude Journal")
        # Add your gratitude journal code here
        st.text("Coming soon!")
