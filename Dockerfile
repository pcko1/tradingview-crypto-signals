FROM python:3.8.7-alpine3.12

WORKDIR /app/

COPY ./tvcs /app/tvcs
COPY ./setup.py /app

RUN python setup.py install

ENTRYPOINT ["python", "/app/tvcs/server/server.py"]