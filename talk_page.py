import streamlit as st
import openai


def show_talk_page():
    st.title("✨ Talk to Tara")
    st.markdown("Tara is here to listen gently and offer wisdom, just like a supportive friend. Share whatever’s on your mind.")

    # Load your OpenAI API key securely
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": (
                "You are Tara, a calm, compassionate, emotionally intuitive companion. "
                "You help people feel heard and supported with empathy, encouragement, and reflection. "
                "Avoid clinical advice. Focus on gentle, soulful conversation."
            )}
        ]

    # Show chat history
    for msg in st.session_state.messages[1:]:  # Skip system message in display
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input box
    if prompt := st.chat_input("What would you like to talk about today?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("Tara is thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages,
                temperature=0.7,
            )
            reply = response.choices[0].message.content
            st.chat_message("assistant").markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
