
From python:latest

WORKDIR /app

RUN pip3 install Flask-SQLAlchemy && \
    pip3 install flask-marshmallow && \
    pip3 install marshmallow-sqlalchemy

COPY create_db.py /app
COPY webapp.py /app
COPY startup.sh /app

EXPOSE 5000

#entrypoint command
CMD ["/app/startup.sh"]