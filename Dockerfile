FROM python:3.7

RUN mkdir /patentsapp

WORKDIR /patentsapp

ADD . /patentsapp

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 7890

CMD ["python3", "patentsapp/app.py"]
