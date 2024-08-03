import streamlit as st
#import os
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.0-pro-latest')

st.title("Welcome our chatbot:")
chat_avatar = "ai logo.jpg"
user_avtar = "user logo.png"
with st.chat_message("assistant", avatar=chat_avatar):
    st.write("How can I assist you?")

with st.chat_message("user",avatar=user_avtar):
    user_message = st.chat_input("Enter your query:")
response = ""
if user_message:
    response = model.generate_content(user_message)

    if response and response.candidates:
        response = response.candidates[0].content.parts[0].text

if user_message:
    st.write(response)


