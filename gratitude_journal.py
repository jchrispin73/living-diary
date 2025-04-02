import streamlit as st

def show_gratitude_journal():
    st.title("Gratitude Journal")

    # Mood selection dropdown
    mood = st.selectbox("How are you feeling today?", [
        "😌 Calm", "💤 Tired", "🌧️ Sad", "🌀 Anxious", "🌪️ Overwhelmed",
        "🔥 Angry", "💔 Heartbroken", "💖 Loved", "🙃 Confused", 
        "🌈 Hopeful", "🌟 Inspired", "🧘 Grounded"
    ])

    # Input fields for journaling
    st.subheader("Today I'm grateful for:")
    grateful_1 = st.text_input("Grateful item 1")
    grateful_2 = st.text_input("Grateful item 2")
    grateful_3 = st.text_input("Grateful item 3")

    st.subheader("Today's affirmation:")
    affirmation = st.text_area("Type your affirmation")

    st.subheader("Looking forward to:")
    looking_forward = st.text_area("Something positive you're looking forward to")

    # Submit button (only on click will session_state be updated)
if st.button("Submit Journal Entry"):
    # Extract mood after emoji and store lowercase
    st.session_state["selected_mood"] = mood.split(" ", 1)[-1].strip().lower()
    st.success("Journal entry saved! Go back to the Home page to see your reflection.")


