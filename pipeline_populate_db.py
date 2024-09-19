from news.models import News
from config import config
import requests

# NewsAPI Config
api_key = config.get("newsapi.key")
url = config.get("newsapi.url")

# Search Parameters
params = {
    'country': 'us',
    'category': 'technology',
    'apiKey': api_key
}

# GET
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    articles = data['articles']
    
    for article in articles:
        
        news_instance = News(
        title=article["title"],
        summary = None,
        description = article["description"],
        # List of paragraphs (use single quotes, as some paragraphs have double quotes to repeat what was said)
        content= article["content"], # Web scraper this part
        image_storage_path = None ,# "img/image_test.png"
        image_url= article["urlToImage"],
        date_published= article["publishedAt"], #datetime.now(timezone.utc),
        author=article["author"],
        tags=[], # generate tags with ML
        category= params["category"], # API info
        country = params["country"], # API info
        news_source=article.get("source",{}).get("name"),
        url = article["url"],
        doc_source = "NewsAPI",
        views = 0
        )
        
        # 1-) Generate document
        news_instance.processing_news()
        
        # 2-) check if the news already is in the db
        if not news_instance.check_document_in_db():
            
            # 3-) Save if isn't in the Db
            news_instance.save_to_db()
            print(f"News item saved successfully!: {article['title']}")
        
        else:
            print("It's already in the db")

else:
    print(f"Erro to find the news: {response.status_code}")
