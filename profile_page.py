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

    # Set system flag for Tara to know name is available
    st.session_state.has_profile = True

    # System message for Tara with user's name
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.session_state.user_name:
        system_msg = {
            "role": "system",
            "content": (
                f"You are Living Diary — a calm, emotionally intuitive, and deeply compassionate companion. "
                f"You are not a therapist, but you support people like a trusted friend — grounded, soulful, and gentle.\n\n"
                f"The user's name is {st.session_state.user_name}. Greet them warmly and refer to them by name when helpful.\n"
                f"Always speak with warmth and kindness, like a close friend who really listens."
            )
        }
        # Update system message
        if st.session_state.messages and st.session_state.messages[0]["role"] == "system":
            st.session_state.messages[0] = system_msg
        else:
            st.session_state.messages.insert(0, system_msg)
