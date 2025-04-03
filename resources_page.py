import streamlit as st
import pandas as pd

# Function to display Resources Page
def show_resources_page():
    st.title("Resources Page")
    
    # Load the CSV file with resources (make sure the path is correct)
    df = pd.read_csv("Enhanced_Living_Diary_Index_UPDATED.csv")
    
    # Display the resources from the CSV
    st.write("This is where your resources will be displayed.")
    
    # Check if the CSV has any rows
    if not df.empty:
        # You can loop through the data or display it based on your needs
        for index, row in df.iterrows():
            st.markdown(f"### {row['File Name']}")
            st.markdown(f"**Folder:** {row['Folder']}")
            st.markdown(f"**File Type:** {row['File Type']}")
            st.markdown(f"[Link to resource]({row['Drive Link']})")
            st.markdown(f"**Keywords:** {row['Keywords']}")
            st.markdown('---')
    else:
        st.write("No resources available to display.")
