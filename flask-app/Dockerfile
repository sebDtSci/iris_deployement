FROM python:latest

WORKDIR /app
COPY requirements.txt .
COPY app.py .
COPY templates/template.html /templates/
COPY iris_classifier.pkl .
RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]