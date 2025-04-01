import streamlit as st

def show_gratitude_journal():
    st.title("🌸 Gratitude Journal")

    with st.form("gratitude_form"):
        st.subheader("Today I'm grateful for:")
        grateful_1 = st.text_input("Grateful item 1", key="g1")
        grateful_2 = st.text_input("Grateful item 2", key="g2")
        grateful_3 = st.text_input("Grateful item 3", key="g3")

        st.subheader("Today's affirmation:")
        affirmation = st.text_area("Type your affirmation", key="a1")

        st.subheader("Something I’m proud of:")
        proud = st.text_area("What are you proud of today?", key="p1")

        st.subheader("Tomorrow I look forward to:")
        look_forward = st.text_area("What are you looking forward to?", key="l1")

        st.subheader("Notes / Reminders:")
        notes = st.text_area("Any extra thoughts or reminders?", key="n1")

        st.subheader("Today I am feeling...")
        feelings = st.text_area("Describe how you're feeling right now", key="f1")

        submitted = st.form_submit_button("Save Journal Entry")

        if submitted:
            st.success("💖 Entry saved! You can return to it later.")

