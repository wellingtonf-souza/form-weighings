FROM python:3.8-slim-buster AS dev

WORKDIR /app

RUN apt-get update && apt-get install tk --yes
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python","app.py"]
