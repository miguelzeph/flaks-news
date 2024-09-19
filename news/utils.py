from mongo.mongo_settings import collection_news

def increment_news(slug:str) -> None:        
    """Increment the views field by 1"""
    
    collection_news.update_one(
        {"slug": slug},
        {"$inc": {"views": 1}}
    )
    
def clean_title(title:str) -> str:
    parts = title.split(' - ')
    
    return parts[0]