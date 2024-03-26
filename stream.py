from langserve import RemoteRunnable
from langchain_core.output_parsers import StrOutputParser


import streamlit as st

llm = RemoteRunnable("http://localhost:8001/basic_chat/") | StrOutputParser()

# Streamlit app
st.title("NVDIA CHAT")
st.write("Talk to the LLM!")

def chat():
    """Chat interface with the LLM"""
    history = st.session_state.get("history", []) 

    message = st.text_input("Enter your message:")

    if st.button("Send"):
        response = llm.invoke(message)
        history.append((message.split("\n", 1)[0], response))  
        st.session_state["history"] = history  


    st.sidebar.title("Chat History")
    for title, _ in history:
        st.sidebar.markdown(f"- {title}")

    for _, output in history:
        st.write(output)

chat()