FROM python:3.8-slim-buster AS dev

WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python","app.py"]
