import streamlit as st

# Set page config FIRST before any other Streamlit command
st.set_page_config(page_title="Living Diary", layout="centered")

def show_home_page():
    # Show your logo (adjust path or width if needed)
    st.image("FullLogo_Transparent_NoBuffer.png", width=250)

    st.markdown("🌈 Here's a gentle journaling prompt for you:")
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
