import streamlit as st
import pandas as pd

def show_gratitude_journal():
    # Try loading the CSV for moods
    try:
        mood_image_df = pd.read_csv("Enhanced_Quote_Images_Living_Diary new.csv")
        st.write("CSV loaded successfully!")
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return

    # Ensure the CSV contains the 'Mood' column
    if 'Mood' not in mood_image_df.columns:
        st.error("The CSV file is missing 'Mood' column.")
        return
    
    # Create a list of moods from the CSV
    mood_options = mood_image_df['Mood'].tolist()

    st.title("🌸 Gratitude Journal")

    with st.form("gratitude_form"):
        # Add the mood dropdown at the top
        st.subheader("Today I am feeling...")
        selected_mood = st.selectbox("Select your mood", mood_options, key="mood")

        # Other sections for the gratitude journal
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

        submitted = st.form_submit_button("Save Journal Entry")

        if submitted:
            st.success("💖 Entry saved! You can return to it later.")  
            st.write(f"You are feeling: {selected_mood}")  # This will display the selected mood after submission

# Call the function to display the gratitude journal
show_gratitude_journal()
