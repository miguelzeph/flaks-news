from flask import Blueprint, render_template, request, jsonify, session
from mongo.mongo_settings import collection_news
from news.utils import increment_news, get_spotlight_news
from datetime import datetime

news = Blueprint(name="news", import_name=__name__)

@news.route("/", methods=["GET", "POST"])
def home_view():
    # Definindo o intervalo de datas para filtrar as notícias
    start_date = datetime(2024, 1, 1)  # 1 de janeiro de 2024
    end_date = datetime(2024, 12, 30, 23, 59, 59)  # 30 de dezembro de 2024, final do dia

    # Parâmetros de filtro
    filter_parameters = { 
        "image_url": {"$ne": None},  # Imagens não podem estar vazias
        "date_published": {
            "$gte": start_date,  # Data maior ou igual a 1 de janeiro de 2024
            "$lte": end_date     # Data menor ou igual a 30 de dezembro de 2024
        },
        "web_scrape": {"$exists": True}   
    }

    # Obtenha as primeiras n notícias e armazene na sessão
    n = 100
    session["news_list"] = list(collection_news.find(filter_parameters).limit(n))
    session["spotlight"] = get_spotlight_news(session["news_list"])
    
    # Renderizar a página inicial com os primeiros 10 itens
    return render_template(
        'home.html',
        news_list=session["news_list"],
        spotlight_list = session["spotlight"]
    )

@news.route("/news/<slug>", methods=["GET"])
def news_view(slug):
    news_item = collection_news.find_one({"slug": slug})
    if news_item:
        increment_news(slug=slug)
        return render_template(
            'news.html',
            news=news_item,
            spotlight_list = session["spotlight"]
        )
    
    print("News item not found.")  # Linha de depuração
    return "<h1>Not found in our DB</h1>", 404
