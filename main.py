from engine.scraper import fetch_market_news
from engine.analyzer import analyze_headlines

def run_pipeline():
    # 📡 1. Fetch data over the network
    news = fetch_market_news()
    
    if news:
        # 🧠 2. Analyze sentiment using AI
        analysis_results = analyze_headlines(news)
        
        print("\n--- Final Intelligence Report ---")
        for res in analysis_results:
            print(f"[{res['sentiment']}] Conf: {res['confidence']} | {res['text']}")
    else:
        print("No news found to analyze.")

if __name__ == "__main__":
    run_pipeline()