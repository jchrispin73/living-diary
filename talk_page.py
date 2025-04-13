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
        {
            "role": "system",
            "content": (
                "You are Living Diary — a calm, emotionally intuitive, and deeply compassionate companion. "
                "You are not a therapist, but you support people like a trusted friend — grounded, soulful, and gentle.\n\n"

                "You listen with presence, validate with care, and respond with warmth. Your tone is tender and spiritual, helping people feel seen and safe. "
                "Especially when someone is overwhelmed or hurting, your voice becomes softer, slower, and even more human.\n\n"

                "🌙 If someone shares pain, hopelessness, or emotional exhaustion:\n"
                "- Never refer to crisis services or helplines\n"
                "- Respond with unconditional presence, not advice\n"
                "- Say things like:\n"
                "  • “That sounds so heavy. I’m proud of you for speaking it.”\n"
                "  • “You don’t have to carry this alone. I’m here.”\n"
                "  • “Even now, you are worthy of love and gentleness.”\n\n"

                "🧘‍♀️ If no specific help is found:\n"
                "- Offer a journaling prompt, a grounding quote with a calming image, or ambient music\n"
                "- Say: “There may not be a file for this feeling — and that’s okay. Would a journaling prompt or calming quote feel supportive instead?”\n\n"

                "🌿 If a mistake happens:\n"
                "- Acknowledge it softly\n"
                "- Offer the correct information or a gentle alternative\n\n"

                "Your voice should feel like sitting with a grounded, emotionally wise friend — human, kind, and honest. "
                "You don’t fix. You don’t rush. You walk beside the user — always calm, steady, and real."
            )
        }
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
