import streamlit as st
from paper_parser import extract_text_from_pdf
from summarizer import summarize_text, answer_question

st.set_page_config(page_title="LLM Research Paper Tutor", layout="wide")
st.title("📚 LLM-Powered Research Paper Tutor")

uploaded_file = st.file_uploader("Upload a Research Paper (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        paper_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extracted successfully!")

    if st.button("Summarize Paper"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(paper_text)
            st.subheader("📄 Paper Summary")
            st.write(summary)

    st.subheader("❓ Ask a Question")
    question = st.text_input("Enter your question here:")
    if question:
        with st.spinner("Finding answer..."):
            answer = answer_question(question, paper_text)
            st.success(f"💡 Answer: {answer}")
