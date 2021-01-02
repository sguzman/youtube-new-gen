import csv
import logging
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

user = myutil.env.get_db_user()
host = myutil.env.get_db_host()
port = myutil.env.get_db_port()
db = myutil.env.get_db_name()

conn = psycopg2.connect(user=user, host=host, port=port, database=db)
cursor = conn.cursor()

for row in csv_reader:
    serial = row[0]
    print(serial)

cursor.close()
conn.close()

