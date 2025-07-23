# 📚 LLM-Powered Research Paper Tutor

An intelligent tool to help users understand, summarize, and interact with research papers using Large Language Models (LLMs). Upload a PDF or text file, get a concise summary, generate Q&A flashcards, extract glossary terms, and even auto-generate presentation slides – all within a simple Streamlit interface.

---

## 🚀 Features

- 🔍 **Upload Support**: Accepts PDF or plain text input.
- ✨ **Summarization**: Automatically generates a concise summary of the uploaded paper using Hugging Face Transformers.
- 🧠 **Flashcard Generator**: Extracts Q&A pairs for easy revision and learning.
- 📘 **Glossary Extractor**: Identifies and explains key terms from the paper.
- 🖼️ **Slide Generator**: Converts summarized content into a PowerPoint presentation (optional).
- 🖥️ **Streamlit UI**: Clean, user-friendly interface for seamless interaction.

---

## 🛠️ Project Structure

```

llm-paper-tutor/
│
├── app.py                 # Streamlit frontend
├── paper\_parser.py        # PDF/text file processing
├── summarizer.py          # Summarization + Q\&A using Hugging Face
├── flashcards.py          # Generate flashcards (Q\&A pairs)
├── glossary.py            # Extract glossary terms with explanations
├── slide\_generator.py     # PowerPoint slide creation (optional)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-paper-tutor.git
cd llm-paper-tutor

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

---

## ▶️ Usage

```bash
streamlit run app.py
```

1. Upload a research paper (`.pdf` or `.txt`)
2. Click "Summarize Paper"
3. Explore:

   * Summary
   * Ask Questions (Q\&A)
   * Generate Flashcards
   * Extract Glossary Terms
   * Create Slide Deck (optional)

---

## 🧪 Tech Stack

* Python 3.10+
* Streamlit
* Hugging Face Transformers (e.g., `facebook/bart-large-cnn`, `t5-base`)
* PyPDF2, spaCy, NLTK
* python-pptx (for slides)
* scikit-learn

---

## 💡 Example Use Cases

* 🎓 Students summarizing academic material
* 🔬 Researchers extracting insights quickly
* 👩‍🏫 Teachers generating teaching material
* 🧑‍💻 Developers experimenting with LLM-based document tools

---

## 👤 Author

**Krishna Venugopal**
AI & Software Developer
🔗 [LinkedIn](https://www.linkedin.com/in/krishna-venugopal-9b073b267) • 🐱 [GitHub](https://github.com/krishnavenu12)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Show Your Support

If you like this project, consider giving it a ⭐️ and sharing it with others!

```

---

Let me know if you want deployment instructions for Hugging Face Spaces, Streamlit Cloud, or PDF screenshots to include!
```
