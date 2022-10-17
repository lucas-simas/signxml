FROM python:3.8

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

ADD api.py /app

RUN pip3 install -r requirements.txt

EXPOSE 5020

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5020", "api:app"]

