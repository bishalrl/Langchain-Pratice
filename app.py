from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv
import time
import openai  # Import openai package

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# Debugging: Print out loaded variables
st.write(f"OPENAI_API_KEY: {openai.api_key}")
st.write(f"LANGCHAIN_API_KEY: {langchain_api_key}")

if openai.api_key is None:
    st.error("OPENAI_API_KEY not found in .env file")
    st.stop()

if langchain_api_key is None:
    st.error("LANGCHAIN_API_KEY not found in .env file")
    st.stop()

# Enable Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo with OpenAI API')
input_text = st.text_input("Search the topic you want")

# OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

def get_response(question):
    # Create the prompt
    formatted_prompt = prompt.format_messages(question=question)
    
    # Try to generate a response with retry logic
    for _ in range(3):  # Retry up to 3 times
        try:
            response = llm.predict(formatted_prompt)
            return response
        except openai.OpenAIError as e:
            st.warning(f"OpenAI API error: {e}. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None
    return "Error occurred. Please try again later."

if input_text:
    response = get_response(input_text)
    st.write(response)
