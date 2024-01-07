FROM postgres:latest

ENV POSTGRES_DB=iris
ENV POSTGRES_USER=alex
ENV POSTGRES_PASSWORD=notsure

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
