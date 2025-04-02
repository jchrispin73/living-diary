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

    if st.button("💜 Save Entry"):
    st.session_state.entries.append({"mood": mood, "text": user_entry})
    st.success("💖 Entry saved. You can return to it in 'Previous Entries' later.")

# Resource matching from keywords
if user_entry:
    try:
        df = pd.read_csv("Enhanced_Living_Diary_Index_UPDATED.csv")
    except FileNotFoundError:
        st.error("🚫 The file 'Enhanced_Living_Diary_Index_UPDATED.csv' was not found. Make sure it's uploaded and named correctly.")
        st.stop()

    user_words = set(re.findall(r'\w+', user_entry.lower()))

    def score_row(row):
        keywords = str(row['Keywords']).lower().split(',')
        return len(set(map(str.strip, keywords)) & user_words)

    df['score'] = df.apply(score_row, axis=1)
    top_match = df[df['score'] > 0].sort_values(by='score', ascending=False).head(1)

    if not top_match.empty:
        resource = top_match.iloc[0]
        st.markdown("### Based on how you're feeling, this might help:")
        st.markdown(f"**{resource.get('Quote', 'Here’s something gentle to explore.')}**")
        st.markdown(f"📝 Here's a journal you might find supportive: [*{resource['File Name']}*]({resource['Drive Link']})", unsafe_allow_html=True)
    else:
        st.info("No matching resource found — but more are coming soon!")
 
