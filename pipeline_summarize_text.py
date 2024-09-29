from web_scraper.summarize_text import summarize_text
from mongo.mongo_settings import collection_news
from datetime import datetime


# Get all documents web scraped with no AI summary
match_format = {
    "$match":{
        "web_scrape.content":{"$exists":True},
        "AI.summary":{"$exists":False}
    }
}

# Get URLS
project_format = {
    "$project": {
        "web_scrape.content": 1,
        "slug":1
    }
}


documents = list(collection_news.aggregate(
        [
            # First find the documents and after format project
            match_format,
            project_format,
            # limit_stage
        ]
    )
)

print(f"number of documents to summarize:{len(documents)}")

for document in documents:
    
    text = " ".join(document["web_scrape"]["content"])
    
    
    try:
        # summary = summarize_text(text)
        summary = summarize_text(text)

        if summary:
            
            filter_doc = {"slug":document["slug"]}
            update_doc = {
                "$set":{
                    "AI":{
                        "summary":summary,
                        "updated_at": datetime.utcnow()
                    }
                }
            }
            
            collection_news.update_one(filter_doc,update_doc)
            
            print(f"Summary created for slug: {document['slug']}")
        
        else:
            
            print("nothing done...")
    
    except:
        print("error")
