From python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ["requirements.txt", "./"]
RUN pip install -r requirements.txt

COPY [".", "./"]
ENTRYPOINT ["./entrypoint.sh"]
