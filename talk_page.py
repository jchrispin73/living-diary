import streamlit as st
import openai import OpenAI
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

    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0);
    }

    [data-testid="stChatInput"] {
        background-color: rgba(255, 255, 255, 0) !important;
        border: none !important;
        box-shadow: none !important;
    }

    footer {
        background-color: rgba(255, 255, 255, 0) !important;
    }

    .css-1vq4p4l {
        background-color: rgba(255, 255, 255, 0) !important;
        box-shadow: none !important;
        border: none !important;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Tara's soft welcome box
    st.markdown(
        f"""
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

    # Add initial system message
    if "messages" not in st.session_state:
        user_name = st.session_state.get("user_name", "")
        name_line = f"The user's name is {user_name}. Greet them warmly and refer to them by name when helpful.\n" if user_name else ""
        st.session_state.messages = [
            {
                "role": "system",
                "content": (
                    "You are Living Diary — a calm, emotionally intuitive, and deeply compassionate companion. "
                    "You are not a therapist, but you support people like a trusted friend — grounded, soulful, and gentle.\n\n"
                    f"{name_line}"
                    "Always speak with warmth and kindness, like a close friend who really listens."
                )
            }
        ]

    # Show previous messages
    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
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
