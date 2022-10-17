FROM python:3.8

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

ADD api.py /app

RUN apt-get update
RUN yes | apt-get install --no-install-recommends python3-pip python3-wheel python3-setuptools python3-openssl

RUN pip3 install -r requirements.txt

EXPOSE 5020

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:6025", "api:app"]

