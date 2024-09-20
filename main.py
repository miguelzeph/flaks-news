from flask import Flask
from flask_session import Session
from flask_sitemap import Sitemap
from news.views import news
from mongo.mongo_settings import collection_news

from news.config_flask import config_flask

app = Flask(
    __name__,
    template_folder="./news/templates",
    static_folder="./news/static"
)

# Inicializando Sitemap
sitemap = Sitemap(app=app)

# Registrando Blueprint
app.register_blueprint(news)

# Registrando gerador de URLs para o sitemap
@sitemap.register_generator
def news_generator():
    news_items = collection_news.find({})
    for news_item in news_items:
        slug = news_item.get('slug')
        if slug:  # Adicione apenas se o slug existir
            yield 'news.news_view', {'slug': slug}

@app.route('/sitemap.xml', methods=['GET'])
def sitemap_view():
    sitemap.add_url('/', changefreq='daily', priority=1.0)
    return sitemap.generate_sitemap()

config_flask(app)  # Nossa configuração pessoal
Session(app)  # Usado para adicionar sessão no lado do servidor
