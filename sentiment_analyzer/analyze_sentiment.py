from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "😊 Positive"
    elif polarity < -0.2:
        return "😠 Negative"
    else:
        return "😐 Neutral"

if __name__ == "__main__":
    print("🧠 Sentiment Analyzer\n")
    text = input("Enter text to analyze: ")
    sentiment = get_sentiment(text)

    print("\n📝 Sentiment Result:")
    print(f"{sentiment}")

