FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pip install boto3

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app