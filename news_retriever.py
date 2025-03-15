import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

class NewsRetriever:
    def __init__(self):
        self.newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_API_KEY"))

    def get_articles(self, query, language="en", page_size=10):
        try:
            response = self.newsapi.get_everything(
                q=query, language=language, page_size=page_size
            )
            return response["articles"]
        except Exception as e:
            print(f"Error fetching articles: {e}")
            return []