import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

# Load environment variables
load_dotenv()

# Set environment variables for Langchain
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

# Initialize the Llama2 model
llm = Ollama(model="llama2")

# Streamlit application
st.title('Langchain Demo with Llama2 API')
input_text = st.text_input("Search the topic you want")

if input_text:
    # Format the prompt as a string
    formatted_prompt = prompt_template.format(question=input_text)
    
    # Generate a response using Llama2 model
    response = llm(formatted_prompt)
    
    # Display the response
    st.write("Response:", response)
