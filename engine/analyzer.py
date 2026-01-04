from transformers import pipeline

# Load the "Linguistic Wizard" - a pre-trained sentiment analyzer
# This model is specifically trained for English text classification
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_headlines(headlines):
    print(f"\n🧠 AI: Analyzing {len(headlines)} headlines...")
    results = []
    
    for text in headlines:
        # The AI "reads" the text and gives a Label (POSITIVE/NEGATIVE) and a Score
        prediction = analyzer(text)[0]
        results.append({
            "text": text,
            "sentiment": prediction['label'],
            "confidence": round(prediction['score'], 4)
        })
    return results

if __name__ == "__main__":
    test_news = ["Nasdaq 100 Futures Rally", "Stock market losing streak"]
    analysis = analyze_headlines(test_news)
    for res in analysis:
        print(f"[{res['sentiment']}] {res['text']} (Conf: {res['confidence']})")