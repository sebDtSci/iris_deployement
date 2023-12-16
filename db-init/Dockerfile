FROM postgres:latest

# RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# RUN python3 -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# RUN pip install psycopg2-binary scikit-learn

ENV POSTGRES_DB=iris
ENV POSTGRES_USER=alex
ENV POSTGRES_PASSWORD=notsure

COPY init.sql /docker-entrypoint-initdb.d/
# COPY init.sh /docker-entrypoint-initdb.d/
# COPY init.py /docker-entrypoint-initdb.d/

# RUN chmod +x /docker-entrypoint-initdb.d/init.sh

EXPOSE 5432
