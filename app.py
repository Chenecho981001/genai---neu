from dotenv import load_dotenv
from typing import Any, Dict, List, Set
import streamlit as st
from streamlit_chat import message
from run_llm import run_llm

# Load environment variables
load_dotenv()

def create_sources_string(source_urls: Set[str]) -> str:
    """Generate a string of formatted source links from a set of URLs."""
    if not source_urls:
        return ""
    sources_list = list(source_urls)[:3]  # Fetch the top K (K <= 3) data entries
    sources_list.sort()
    sources_string = "".join(f"- [Source {i+1}]({source})\n" for i, source in enumerate(sources_list))
    return sources_string

def initialize_session_state():
    """Initialize session state variables."""
    if "chat_answers_history" not in st.session_state:
        st.session_state["chat_answers_history"] = []
    if "user_prompt_history" not in st.session_state:
        st.session_state["user_prompt_history"] = []
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

def handle_prompt(prompt: str):
    """Handle the user prompt and generate a response."""
    try:
        with st.spinner("Generating response..."):
            generated_response = run_llm(query=prompt, chat_history=st.session_state["chat_history"])
            sources = {doc.metadata["source"] for doc in generated_response["context"]}
            formatted_response = f"{generated_response['answer']} \n {create_sources_string(sources)}"

            # Update session state
            st.session_state["user_prompt_history"].append(prompt)
            st.session_state["chat_answers_history"].append(formatted_response)
            st.session_state["chat_history"].append(("human", prompt))
            st.session_state["chat_history"].append(("ai", generated_response["answer"]))
    except Exception as e:
        st.error(f"An error occurred: {e}")

def display_chat_history():
    """Display the chat history."""
    for user_query, generated_response in zip(st.session_state["user_prompt_history"], st.session_state["chat_answers_history"]):
        message(user_query, is_user=True)
        message(generated_response)

# App Header
st.header("Ask me anything about MongoDB!")

# Initialize session state
initialize_session_state()

# User Prompt Input
prompt = st.text_input("Prompt", placeholder="Enter your question here...") or st.button("Submit")

if prompt:
    handle_prompt(prompt)

# Display Chat History
display_chat_history()
