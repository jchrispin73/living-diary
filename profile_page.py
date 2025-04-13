import streamlit as st

def show_profile_page():
    st.title("🌿 Your Living Diary Profile")
    st.markdown("Use this page to personalize your experience. Tara will remember your name during this session.")

    # Load saved name if available
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    # Form for user name
    with st.form("profile_form"):
        name_input = st.text_input("What should Tara call you?", value=st.session_state.user_name)
        submitted = st.form_submit_button("Save")

        if submitted:
            st.session_state.user_name = name_input
            st.success(f"Got it! Tara will call you **{name_input}** during this session.")

    # Show saved name if available
    if st.session_state.user_name:
        st.markdown(f"✅ **Tara will greet you as:** {st.session_state.user_name}")
