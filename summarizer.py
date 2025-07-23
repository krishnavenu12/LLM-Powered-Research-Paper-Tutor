import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return " ".join(summaries)

def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']
