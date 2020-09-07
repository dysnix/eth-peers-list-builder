FROM python:3-alpine

ADD requirements.txt /usr/src/app/requirements.txt

RUN pip install -r /usr/src/app/requirements.txt

ADD . /usr/src/app

CMD ["python", "/usr/src/app/main.py"]