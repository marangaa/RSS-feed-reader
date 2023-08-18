import feedparser

def fetch_and_display_feed(feed_url):
    feed = feedparser.parse(feed_url)
    print("Title:", feed.feed.title)
    print("Description:", feed.feed.description)
    print("\nArticles:")
    for entry in feed.entries:
        print("-", entry.title)

if __name__ == "__main__":
    rss_url = "https://www.nasa.gov/rss/dyn/breaking_news.rss"  # Replace with the actual RSS feed URL
    fetch_and_display_feed(rss_url)
