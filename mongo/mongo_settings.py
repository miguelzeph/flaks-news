from klein_mongo import get_client
from config import config


# Constants
MONGO_HOST = config.get("mongo.host")
MONGO_PORT = config.get("mongo.port")
MONGO_USERNAME = config.get("mongo.username")
MONGO_PASSWORD = config.get("mongo.password")

MONGO_DATABASE = config.get("mongo.database")
MONGO_COLLECTION_NEWS = config.get("mongo.collection.news")
MONGO_COLLECTION_COMMENTS= config.get("mongo.collection.comments")
MONGO_COLLECTION_AUTHENTICATION = config.get("mongo.collection.authentication")


# Mongo Client
client = get_client(config)

# Database
db = client[MONGO_DATABASE]

# Collection
collection_news = db[MONGO_COLLECTION_NEWS]
collection_comments = db[MONGO_COLLECTION_COMMENTS]
collection_authentication = db[MONGO_COLLECTION_AUTHENTICATION]
