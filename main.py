from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
import os

import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate text using Google Generative AI
model = genai.GenerativeModel("gemini-v1")


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app
st.set_page_config(page_title="Manja 2.0", page_icon=":robot_face:", layout="wide")

st.header("Manja 2.0 powered by Google Generative AI")
st.write("Ask me anything!")  

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Submit")

# Display the response from the model
if submit_button:
    response = get_gemini_response(input_text)  # Corrected input reference
    st.subheader("Response:")
    st.write(response)
