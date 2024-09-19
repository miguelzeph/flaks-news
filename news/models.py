from datetime import datetime
from mongo.mongo_settings import collection_news
from news.utils import clean_title
from slugify import slugify


class News:
    
    def __init__(
        self,
        title:str,
        summary:str,
        description:str,
        content:list,
        image_storage_path:str,
        image_url:str,
        date_published:datetime,
        author:str,
        tags:list,
        category:str,
        country:str,
        news_source:str,
        url:str,
        doc_source:str,
        views:int
        ):
        
        self.title = title
        self.summary = summary
        self.description = description
        self.content = content
        self.image_storage_path= image_storage_path
        self.image_url = image_url
        self.date_published = date_published
        self.author = author
        self.tags = tags
        self.category = category
        self.country = country
        self.news_source = news_source
        self.url = url
        self.doc_source = doc_source
        self.views = views
        
    def processing_news(self):
        
        self.news_document = {
            "raw_title": self.title,
            "title": clean_title(self.title), # remove " - " source... 
            "summary":self.summary,
            "description": self.description,
            "content": self.content,
            "slug": slugify(self.title), # Use the "raw title"
            "image_storage_path": self.image_storage_path,
            "image_url": self.image_url,
            "date_published": datetime.strptime(self.date_published, "%Y-%m-%dT%H:%M:%SZ"),
            "author": self.author,
            "tags": self.tags,
            "category": self.category,
            "country": self.country,
            "news_source": self.news_source,
            "url": self.url,
            "doc_source": self.doc_source,
            "views":self.views,
            # language (AI can define)
        }
    
    def check_document_in_db(self) -> None:
        
        if collection_news.find_one(
                {"slug": self.news_document["slug"]} #slugify(self.title)
            ):
            return True
            
    def save_to_db(self) -> None:
        
        # Save    
        collection_news.insert_one(self.news_document)
    
