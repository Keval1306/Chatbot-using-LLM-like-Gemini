import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("Welcome our chatbot:")
chat_avatar = "ai logo.jpg"
user_avtar = "user logo.png"

response = ""
if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant", avatar=chat_avatar):
    st.write("How can I assist you?")

user_message = st.chat_input("Enter your query:", key="input")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.chat_message("user", avatar=user_avtar):
        st.markdown(user_message)

    with st.spinner("Generating..."):
        try:
            response = model.generate_content(user_message)
            if response and response.candidates:
                response_text = response.candidates[0].content.parts[0].text

            st.session_state.messages.append({"role": "assistant", "content": response_text})

            with st.chat_message("assistant", avatar=chat_avatar):
                st.markdown(response_text)

        except Exception as e:
            st.error(f"An error occurred: {e}")



#print(os.environ.get("GEMINI_API_KEY"))
