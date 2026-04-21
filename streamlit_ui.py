import streamlit as st 
import requests

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_icon="none",
    page_title="Stock market Multi-Agent Chatbot",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("Stock Market Agentic Chatbot")

with st.sidebar:
    st.header("Please upload Document")
    st.markdown("Upload your stock market releted pdf or Docx files to prepare knowledge base.")
    uploaded_files = st.file_uploader("choose files", type=["pdf","docx"], accept_multiple_files=True )

    if st.button("Upload and Ingest"):
        if not uploaded_files:
            st.warning("Please upload file first")
        else:
            files = [("files", (f.name, f.read(), f.type)) for f in uploaded_files]
            with st.spinner("uploading and processing files..."):
                response = requests.post(f"{BASE_URL}/upload", files=files)
                if response.status_code == 200:
                    st.success("files upload and processed sucessfully")
                else:
                    st.error("Upload failed" + response.text)

st.header("Ask Question")

st.markdown("Enter your stock market-releted question. The chatbot will search the document and response intelligently")

question=st.text_input("Your question" , placeholder="e.g. what are the financials of apple Inc?")
     
if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter the question")
    else: 
        with st.spinner("Thinking..."):
            payload = {"question":question}
            response = requests.post(f"{BASE_URL}/query", json=payload)
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer returned.")
                st.markdown("### Answer")
                st.write(answer)
            else:
                st.error("Failed to get answer:"+ response.txt)
