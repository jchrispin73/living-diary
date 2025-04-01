import streamlit as st

def show_home_page():
    st.set_page_config(page_title="Living Diary", layout="centered", initial_sidebar_state="auto")

    # Center and resize logo
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://raw.githubusercontent.com/jchrispin73/living-diary/main/FullLogo_Transparent_NoBuffer.png" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🌈 Here's a gentle journaling prompt for you:")
    # ... rest of your Home UI ...
    prompt = st.selectbox("Pick a prompt", [
        "If my heart could speak, what would it say?",
        "Right now, I am feeling...",
        "What emotion keeps showing up lately?"
    ])

    mood = st.selectbox("Pick a mood to help match your reflection to a resource:", [
        "😌 Calm", "💔 Heartbroken", "🥰 Loved", "😵‍💫 Overwhelmed", "😴 Tired"
    ])

    reflection = st.text_area("You can type below if you'd like to reflect:")

    if st.button("💜 Save Entry"):
        st.success("💖 Entry saved. You can return to it later.")
