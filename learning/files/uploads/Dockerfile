FROM python:3.8-slim

RUN python3 -m venv venv

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install PyMuPDF

EXPOSE 8080

CMD [ "python3", "main.py"]