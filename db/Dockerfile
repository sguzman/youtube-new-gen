FROM postgres:latest

COPY schema/01-init.sql /docker-entrypoint-initdb.d/
COPY schema/02-channel.sql /docker-entrypoint-initdb.d/
COPY schema/03-channel-ts.sql /docker-entrypoint-initdb.d/