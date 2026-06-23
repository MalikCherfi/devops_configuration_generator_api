FROM python:3.14
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "app.py"]
EXPOSE 8000