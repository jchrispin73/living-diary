import streamlit as st
import pandas as pd

def show_gratitude_journal():
    # Try loading the CSV and check if it works
    try:
        mood_image_df = pd.read_csv("Enhanced_Quote_Images_Living_Diary new.csv")
        st.write("CSV loaded successfully!")
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return

    # Check the content of the CSV
    st.write("Mood and image data from CSV:")
    st.write(mood_image_df.head())  # Show the first few rows of the dataframe for debugging

    # Create a dictionary to map moods to images
    if 'Mood' not in mood_image_df.columns or 'Image URL' not in mood_image_df.columns:
        st.error("The CSV file is missing 'Mood' or 'Image URL' columns.")
        return

    mood_to_image = {mood: image for mood, image in zip(mood_image_df['Mood'], mood_image_df['Image URL'])}

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
        # Mood selection dropdown
        mood_options = list(mood_to_image.keys())
        selected_mood = st.selectbox("Select your mood", mood_options, key="mood")

        st.subheader("How are you feeling today?")
        feelings = st.text_area("Describe how you're feeling right now", key="f1")

        submitted = st.form_submit_button("Save Journal Entry")

        if submitted:
            st.success("💖 Entry saved! You can return to it later.")
            
            # Display mood-based image
            st.image(mood_to_image[selected_mood], caption=f"Image for mood: {selected_mood}", width=300)

# Call the function to display the gratitude journal
show_gratitude_journal()
