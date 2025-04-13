# talk_page.py
import streamlit as st
import openai

# --- Securely load the API key ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Page layout settings ---
st.title("Talk to Tara 💬")
st.markdown("""
Welcome to your gentle space for reflection. Tara is here to listen with empathy and offer soft, supportive insight. 
Just share what you're feeling or thinking — there are no wrong words here.
""")

# --- Text input box ---
user_input = st.text_area("What's on your mind?", placeholder="Type your thoughts here...", height=150)

# --- Handle submission ---
if st.button("Send to Tara") and user_input:
    with st.spinner("Tara is thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # You can change this to "gpt-3.5-turbo" if needed
                messages=[
                    {"role": "system", "content": "You are Tara, a calm, emotionally intuitive companion. Always respond with warmth, compassion, and deep understanding. Speak gently and offer reflective encouragement."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=300,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.markdown("---")
            st.markdown("**Tara says:**")
            st.success(reply)
        except Exception as e:
            st.error("Something went wrong. Please try again later.")
            st.exception(e)

# Optional: subtle footer
st.markdown("<br><sub>Living Diary – A soft place to land.</sub>", unsafe_allow_html=True)
