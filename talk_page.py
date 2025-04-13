import streamlit as st
import openai
import os

def show_talk_page():
    # Inject custom page styles
        page_bg_img = """
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/jchrispin73/living-diary/main/background_talk_v2.png");
        background-size: 90%;
        background-position: right center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Match Home page max-width for nav buttons */
    [data-testid="stHorizontalBlock"] {
        max-width: 900px;
        margin: 2rem auto;
    }

    /* Remove background from main content container */
    .block-container {
        background-color: rgba(255, 255, 255, 0);
        padding: 2rem;
        border-radius: 0;
        max-width: 100%;
        margin: 2rem 2rem 1rem 2rem;
        box-shadow: none;
    }


    .stButton > button {
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    /* Transparent top nav bar */
    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0);
    }

    /* Transparent chat input box */
    [data-testid="stChatInput"] {
        background-color: rgba(255, 255, 255, 0) !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Transparent bar container for chat input */
    footer {
        background-color: rgba(255, 255, 255, 0) !important;
    }

    /* Transparent outer wrapper of the chat input row (Streamlit-specific class) */
    .css-1vq4p4l {
        background-color: rgba(255, 255, 255, 0) !important;
        box-shadow: none !important;
        border: none !important;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

        # Tara's soft welcome box (styled like Home page)
    st.markdown(
        """
        <div class='block-container'>
            <div style="text-align: center;">
                <h1 style='margin-top: 0;'>🌸 Talk to Tara</h1>
                <p style="font-size: 1.1rem;">
                    Tara is here to listen gently and offer wisdom, just like a supportive friend. <br>
                    Share whatever’s on your mind.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load OpenAI key
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Initial system prompt
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

    # Display chat history
    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle new user input
    if user_input := st.chat_input("What's on your mind today?"):
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Tara is thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages,
                temperature=0.7
            )
            reply = response.choices[0].message["content"]
            st.chat_message("assistant").markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
