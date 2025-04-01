import streamlit as st
import datetime

# Page setup
st.set_page_config(page_title="Gratitude Journal", layout="centered")
st.title("🌸 Daily Gratitude Journal")
st.markdown("_A gentle space to reflect, affirm, and grow._")

# Default date
today = datetime.date.today()
st.markdown(f"### 📅 {today.strftime('%A, %B %d, %Y')}")

# Journal form
with st.form("journal_form"):
    st.markdown("#### 💖 Today I'm grateful for...")
    gratitude = st.text_area("Gratitude", placeholder="List one or more things you’re grateful for today.")

    st.markdown("#### 🌞 Today's affirmation")
    affirmation = st.text_input("Affirmation", placeholder="Write an uplifting or grounding thought.")

    st.markdown("#### 🌱 Something I'm proud of")
    proud = st.text_area("Proud Moment", placeholder="Reflect on something you're proud of—even if it's small.")

    st.markdown("#### 🌈 Tomorrow I look forward to...")
    forward = st.text_area("Looking Forward", placeholder="Set a gentle intention for tomorrow.")

    st.markdown("#### 🧠 Notes or reminders")
    notes = st.text_area("Notes", placeholder="Anything else you'd like to remember or let go of.")

    st.markdown("#### 🌤️ Today I feel...")
    feeling = st.selectbox("Mood", ["😌 Calm", "🌧️ Sad", "🌟 Inspired", "🔥 Frustrated", "💤 Tired", "💖 Loved", "🌪️ Overwhelmed"])

    submitted = st.form_submit_button("💾 Save My Entry")

    if submitted:
        st.success("💜 Your journal entry was saved for today.")
        st.write("---")
        st.markdown("### 📘 Your Reflection Summary")
        st.markdown(f"**Grateful for:** {gratitude}")
        st.markdown(f"**Affirmation:** {affirmation}")
        st.markdown(f"**Proud moment:** {proud}")
        st.markdown(f"**Looking forward to:** {forward}")
        st.markdown(f"**Notes:** {notes}")
        st.markdown(f"**Feeling:** {feeling}")
