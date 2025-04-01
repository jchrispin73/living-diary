import streamlit as st

# ✅ Must be at the top, before any Streamlit commands
st.set_page_config(
    page_title="Living Diary",
    layout="centered",
    initial_sidebar_state="auto"
)

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
        # Your gratitude journal form code here (keep as is)
        show_gratitude_journal()

def show_gratitude_journal():
    st.title("🌸 Gratitude Journal")

    with st.form("gratitude_form"):
        st.subheader("Today I'm grateful for:")
        grateful_1 = st.text_input("Grateful item 1", key="g1")
        grateful_2 = st.text_input("Grateful item 2", key="g2")
        grateful_3 = st.text_input("Grateful item 3", key="g3")

        st.subheader("Today's affirmation:")
        affirmation = st.text_area("Type your affirmation", key="a1")

        st.subheader("Something I'm proud of:")
        proud = st.text_area("What are you proud of today?", key="p1")

        st.subheader("Tomorrow I look forward to:")
        look_forward = st.text_area("What are you looking forward to?", key="l1")

        st.subheader("Notes / Reminders:")
        notes = st.text_area("Any extra thoughts or reminders?", key="n1")

        st.subheader("Today I am feeling...")
        feelings = st.text_area("Describe how you're feeling right now", key="f1")

        submitted = st.form_submit_button("Save Journal Entry")

    if submitted:
        st.success("💜 Entry saved! You can return to it later.")
