# 🤖 AI Playground

This is a personal lab of AI tools, experiments, and learning projects built in **Python** and **JavaScript**.  
It’s where I explore the power of language models, NLP, computer vision, and prompt engineering — one tool at a time.

---

## 🧠 What You'll Find Here

| Tool / Folder            | Language     | Description                                                         |
|--------------------------|--------------|---------------------------------------------------------------------|
| `sentiment_analyzer/`    | Python       | Detects emotional tone of input text using `TextBlob`               |
| `image_to_text/`         | Python       | OCR tool that extracts text from images using `pytesseract`         |
| `text_summarizer/`       | Python       | Summarizes long text using Hugging Face's `facebook/bart-large-cnn`|
| `prompt_playground/`     | JavaScript   | A web UI to test prompts using the OpenAI API                       |
| `ai_notes/`              | Markdown     | Personal notes on AI concepts, fine-tuning, APIs, and more          |

---

## 🚀 How to Run (Per Tool)

Each tool has its own folder with a `README.md` and setup instructions.  
Here’s the general setup:

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install necessary packages
pip install -r requirements.txt  # or see individual READMEs
