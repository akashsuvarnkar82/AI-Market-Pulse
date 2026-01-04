import requests
from bs4 import BeautifulSoup

def fetch_market_news():
    # NETWORKING: Sending an HTTP request across the web
    url = "https://news.google.com/rss/search?q=stock+market"
    response = requests.get(url)
    
    # Check if the connection was successful (Status 200)
    if response.status_code == 200:
        print("✅ Networking: Successfully connected to News Feed")
        soup = BeautifulSoup(response.content, 'xml')
        headlines = [item.title.text for item in soup.find_all('item')[:5]]
        return headlines
    else:
        print(f"❌ Networking Error: Status {response.status_code}")
        return []

if __name__ == "__main__":
    news = fetch_market_news()
    for i, title in enumerate(news, 1):
        print(f"{i}. {title}")