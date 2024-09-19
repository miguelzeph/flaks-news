# Flaks News

![MinuteNews](./minutenews.png)


Welcome to Django News! This project demonstrates how to use Django to build a news website efficiently. It automates the process of updating news content and allows you to manage everything from your local machine by simply deploying the Django site and updating the database.

## Dependencies

To get started, install the required dependencies using the following command:


```bash
pip install -r requeriments.txt
```

## Configuration

Before running the application, set up the configuration file:


```bash
export KLEIN_CONFIG=./path/your-config.yml
```

## Key Components

- NewsAPI: For populating the database with news data.
- Requests & BeautifulSoup: For web scraping.
- Selenium: For summarizing news content. (This free option avoids using memory-intensive transformers or paid services like ChatGPT.)


## Database Management

The database should be hosted in the cloud for optimal performance and accessibility. By having your database in the cloud, you ensure that updates and changes are seamless and can be managed directly from your local machine. This setup eliminates the need for long deployment times and allows for quicker updates and maintenance.

### Advantages of Cloud Database:
- Direct Updates: You can update the database directly from your local machine without needing to redeploy the entire application.
- Efficiency: Reduces deployment times and ensures that changes are reflected immediately.
- Accessibility: Provides easy access to the database from anywhere, facilitating remote management and updates.

## Running MongoDB with Docker Compose

To test the database locally, use Docker Compose to create a MongoDB container:

```bash
docker-compose up --build
```
**Note**: Use config_example.yml as a template to create your own config.yml. The information in config.yml might not be included in the repository.

## Starting

- 1-) Creating project:
```bash
django-admin startproject django_news
cd django_news
```
- 2-) Creating application of news:
```bash
django-admin startapp noticias
```

## Populating the Database with News

Populating the Database with News

```bash
python pipeline_populate_db.py
```

## Scraping News

To scrape news data from the web, execute:

```bash
python pipeline_web_scraper.py
```

## Summarizing News Text

To summarize news content, use:

```bash
python pipeline_summarize_text.py
```

## Populating DB with News 

This part can be an web scraper generating information with OpenAI API.

```bash
python pipeline_populate_db.py
```

## Scrape News

```bash
python pipeline_web_scraper.py
```

## Pipeline Summarize Text

```bash
python pipeline_summarize_text.py
```

## Author

- Miguel Angelo do Amaral