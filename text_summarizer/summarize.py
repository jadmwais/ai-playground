from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("📝 Text Summarizer (Transformers)\n")
    user_input = input("Paste text to summarize:\n\n")
    print("\n🧠 Generating summary...\n")
    summary = summarize_text(user_input)
    print("📄 Summary:\n")
    print(summary)

