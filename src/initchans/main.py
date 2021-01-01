import csv
import logging
import os
import psycopg2

import myutil
from myutil import env

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting Channel List Initializer")

csv_file_name = './channels.csv'

csv_file = open(csv_file_name, 'r')
logging.debug(f'Opening {csv_file_name}')

csv_reader = csv.reader(csv_file_name)
logging.debug(f'Reading {csv_file_name}')

user_env = 'POSTGRES_USER'
user = os.environ['POSTGRES_USER']

password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
db = os.environ['POSTGRES_DB']

conn = psycopg2.connect(user=user, password=password, host=host, port=port, database=db)

cursor = conn.cursor()

for row in csv_reader:
    serial = row[0]
    print(serial)

cursor.close()
conn.close()

