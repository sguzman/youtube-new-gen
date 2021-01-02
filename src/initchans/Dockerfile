FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
COPY channels.csv /app/channels.csv
COPY ./myutil /app/myutil

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
