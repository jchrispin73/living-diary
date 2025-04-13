import streamlit as st
import openai
import os

def show_talk_page():
    st.title("🌸 Talk to Tara")
    st.markdown("Tara is here to listen gently and offer wisdom, just like a supportive friend. Share whatever’s on your mind.")

    # Securely load your OpenAI API key from Streamlit secrets
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": (
                "You are Tara, a warm, compassionate and emotionally intuitive companion. "
                "You respond with kindness, non-judgment, and gentle wisdom. "
                "You help people reflect, express themselves, and feel supported. "
                "Avoid giving clinical or medical advice. Focus on empathy and encouragement."
            )}
        ]

    # Show chat history
    for msg in st.session_state.messages[1:]:  # skip system prompt
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    if user_input := st.chat_input("What's on your mind today?"):
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Tara is thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Change to "gpt-4" if you like
                messages=st.session_state.messages,
                temperature=0.7
            )
            reply = response.choices[0].message["content"]
            st.chat_message("assistant").markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
