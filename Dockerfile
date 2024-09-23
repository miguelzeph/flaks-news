# Use uma imagem oficial do Python como base
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de configuração para o diretório de trabalho (verifique se ele é realmente necessário no seu caso Flask)
COPY config_example.yml /app/

# Copie o código fonte para o diretório de trabalho
COPY mongo /app/mongo
COPY news /app/news
COPY main.py /app/
COPY config.py /app/

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.deploy.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.deploy.txt

# Defina as variáveis de ambiente (certifique-se de que a configuração seja necessária)
ENV KLEIN_CONFIG=/app/config_example.yml

# Exponha a porta em que o Flask irá rodar com Gunicorn (flaks is 5000 but Gunicorn use 8000)
EXPOSE 8000

# Comando para rodar o aplicativo Flask usando Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
# CMD ["flask","--app","main.py","run"]