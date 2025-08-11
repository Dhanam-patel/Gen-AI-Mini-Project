from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
# import pyttsx3

load_dotenv()

# engine = pyttsx3.init()

llm = HuggingFaceEndpoint(
    repo_id="baidu/ERNIE-4.5-300B-A47B-Base-PT",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm,temprature=2)
text = {str(st.text_area("Enter the text to be summarized", height=300))}
tone = st.selectbox("Select the desired tone for the summary",["Professional", "Fun", "Explanatory", "Detailed", "Creative", "Technical", "Code-Oriented"])
length = st.selectbox("Select the desired length for the summary(The length of summary will also depend on the length of text)",["short(50 to 60 words)", "Medium (100 to 120 words)", "Large (more than 150 words)"])
Format = st.selectbox("Select the desired Format for the summary",["Paragraph", "Numbered Steps", "Bullet Points"])
language = st.selectbox("Select the desired language for the summary",["English", "Hindi", "Gujarati"])
template = load_prompt("template.json")
prompt = template.invoke({
    "text": text,
    "tone": tone,
    "length": length,
    "Format": Format,
    "language": language
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
    # engine.say(result.content)
    # engine.runAndWait()