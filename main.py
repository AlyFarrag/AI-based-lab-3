import argparse
from news_retriever import NewsRetriever
from embedding_engine import EmbeddingEngine
from summarizer import Summarizer
from user_manager import UserManager

def main():
    parser = argparse.ArgumentParser(description="News Summarization Application")
    parser.add_argument("--user", type=str, required=True, help="User ID")
    parser.add_argument("--topic", type=str, help="Search for news on a specific topic")
    parser.add_argument("--save-topic", type=str, help="Save a topic of interest")
    parser.add_argument("--summary-type", choices=["brief", "detailed"], help="Type of summary")
    args = parser.parse_args()

    user_manager = UserManager(args.user)
    news_retriever = NewsRetriever()
    embedding_engine = EmbeddingEngine()
    summarizer = Summarizer()

    if args.save_topic:
        user_manager.add_topic(args.save_topic)
        print(f"Topic '{args.save_topic}' saved.")

    if args.topic:
        articles = news_retriever.get_articles(args.topic)
        if articles:
            texts = [article["title"] + " " + article["description"] for article in articles]
            embedding_engine.create_embeddings(texts)

            for article in articles:
                print(f"\nTitle: {article['title']}")
                if args.summary_type == "brief":
                    print("Summary:", summarizer.brief_summary(article["content"]))
                elif args.summary_type == "detailed":
                    print("Summary:", summarizer.detailed_summary(article["content"]))

            user_manager.add_history(args.topic)
        else:
            print("No articles found.")

    if args.user:
        print(f"\nUser Topics: {user_manager.preferences['topics']}")
        print(f"Search History: {user_manager.history}")

if __name__ == "__main__":
    main()