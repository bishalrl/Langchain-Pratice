import requests
import streamlit as st

def get_openai_response(input_text):
    try:
        response = requests.post("http://localhost:8000/essay/invoke",
                                 json={'input': {'topic': input_text}})
        response.raise_for_status()
        return response.json()['output']['content']
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def get_ollama_response(input_text):
    try:
        response = requests.post("http://localhost:8000/poem/invoke",
                                 json={'input': {'topic': input_text}})
        response.raise_for_status()
        response_json = response.json()
        st.write("Ollama Response JSON:", response_json)  # Print the response content
        return response_json['output']
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Streamlit framework

st.title('Langchain Demo With LLama2 Api')
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
