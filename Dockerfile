FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

COPY entrypoint.sh /app/entrypoint.sh

# Set entrypoint to the script
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
