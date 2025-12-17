from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import load_prompt
import streamlit as st
from model import model
from Prompt.System_Message import System_Message


st.title("CyMent-AI")
st.text("""Cyment is an AI-powered cybersecurity assistant designed to provide practical guidance and support for individuals facing online security challenges. It offers advice on responding to potential threats, suggests security measures, and shares educational insights based on user requests. When a situation appears critical or risky, Cyment encourages contacting qualified professionals or authorities. Its goal is to assist users in understanding and improving their cybersecurity posture through clear and timely information.
""")
st.title("Chat")

if 'history' not in st.session_state:
    st.session_state.history = [
        SystemMessage(System_Message),
        ]


user = st.chat_input("You: ")

Prompt_load = load_prompt("Cyber-Buddy/Prompt/Prompt.json")

if user:
    chat_history_text = "\n".join([f"{type(msg).__name__}: {msg.content}" for msg in st.session_state.history])
    
    Prompt = Prompt_load.invoke({
        "User_Input": user,
        "Chat_History": chat_history_text
    })  
    
    st.session_state.history.append(HumanMessage(content=user))

    response = model.invoke(Prompt)

    st.session_state.history.append(AIMessage(content=response.content))

for message in st.session_state.history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
