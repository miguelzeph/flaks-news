from flask import Blueprint, render_template, request, jsonify
from mongo.mongo_settings import collection_news
from news.utils import increment_news
from datetime import datetime

news = Blueprint(name="news", import_name=__name__)

@news.route("/", methods=["GET", "POST"])
def home_view():
    # Filter List News
    start_date = datetime(2024, 1, 1)  # 1st January 2024
    end_date = datetime(2024, 12, 30, 23, 59, 59)  # 30th December 2024, end of the day
    
    filter_parameters = { 
        # images not empty
        "image_url": {"$ne": None},
        # Filter List News
        "date_published": {
            "$gte": start_date,  # Date greater than or equal to 1st January 2024
            "$lte": end_date     # Date less than or equal to 30th December 2024
        },
        # Filter Content
        "web_scrape": {"$exists": True}   
    }
    
    # Get first n News
    n = 100
    news_list = list(collection_news.find(filter_parameters).limit(n))
    
    return render_template('home.html', news_list=news_list)

@news.route("/news/<slug>", methods=["GET"])
def news_view(slug):
    
    news_item = collection_news.find_one({"slug": slug})
    if news_item:
        increment_news(slug=slug)
        return render_template('news.html', news=news_item)
    
    print("News item not found.")  # Debugging line
    return "<h1>Not found in our DB</h1>", 404

