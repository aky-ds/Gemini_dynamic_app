from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=os.getenv("GOOGLE_KEY"))

model=genai.GenerativeModel('gemini-pro')

def get_response(question):
    response=model.generate_content(question)
    return response.text

st.header('Gemini Pro Assistant App')

input=st.text_input("Input",key='input')

submit=st.button("Ask The Question")

if submit:
    response=get_response(input)
    st.subheader("Your Answer is")
    st.write(response)
