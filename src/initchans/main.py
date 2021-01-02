import csv
import logging
import psycopg2

import myutil
from myutil import env

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting Channel List Initializer")

csv_file_name = './channels.csv'

csv_file = open(csv_file_name, 'r')
logging.debug('Opening %s', csv_file_name)

csv_reader = csv.reader(csv_file_name)
logging.debug('Reading %s', csv_file_name)

user = myutil.env.get_db_user()
host = myutil.env.get_db_host()
port = myutil.env.get_db_port()
db = myutil.env.get_db_name()
table = myutil.env.get_db_table()

sql_insert = f'INSERT INTO {table} (serial) VALUES (%s);'
conn = psycopg2.connect(user=user, host=host, port=port, database=db)
cursor = conn.cursor()

for row in csv_reader:
    serial = row[0]
    logging.debug('Inserting value %s into table %s', serial, table)
    cursor.exec(sql_insert, [serial])

cursor.close()
conn.close()

