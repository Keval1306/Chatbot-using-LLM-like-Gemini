import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.sidebar.title("K.E.V.A.L.AI")
st.sidebar.write("Knowledge, Empathy, Versatility, Adaptability, Learning and AI")
contact_us = st.sidebar.selectbox (
    "How would you like to be contacted?",  
    ("Email","Phone no")
)

if contact_us == "Email":
    st.sidebar.write("kevaljamnapara@gmail.com")
else:
    st.sidebar.write("+91 ******4948")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("Welcome to  K.E.V.A.L.AI :")


response = ""
if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
    st.write("How can I assist you?")

user_message = st.chat_input("Enter your query:", key="input")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})
    st.success('wait atleast 4 seconds for your answer', icon="👍")

    with st.chat_message("user"):
        st.markdown(user_message)

    with st.spinner("Generating..."):
        try:
            response = model.generate_content(user_message)
            if response and response.candidates:
                response_text = response.candidates[0].content.parts[0].text

            st.session_state.messages.append({"role": "assistant", "content": response_text})

            with st.chat_message("assistant"):
                st.markdown(response_text)

        except Exception as e:
            st.error(f"An error occurred: {e}")



#print(os.environ.get("GEMINI_API_KEY"))
