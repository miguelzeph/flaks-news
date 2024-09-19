# Use uma imagem oficial do Python como base
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de configuração para o diretório de trabalho
COPY config_django_news_mongo_atlas.yml /app/

# Copie o código fonte para o diretório de trabalho
COPY django_news /app/django_news
COPY mongo /app/mongo
COPY news /app/news
COPY manage.py /app/
COPY global_config.py /app/
# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.deploy.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.deploy.txt

# Defina as variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=django_news.settings
ENV KLEIN_CONFIG=/app/config_django_news_mongo_atlas.yml

# Coletar arquivos estáticos
# RUN python manage.py collectstatic --noinput

# Exponha a porta em que o Django irá rodar
EXPOSE 8000

# Comando para rodar o aplicativo Django usando Gunicorn
CMD ["python", "manage.py", "runserver"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_news.wsgi:application"]