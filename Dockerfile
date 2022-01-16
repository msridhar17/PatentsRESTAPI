FROM python:3.7

RUN mkdir /

WORKDIR /

ADD . /

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 7890

CMD ["python3", "app.py"]