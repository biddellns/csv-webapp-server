From python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY [".", "./"]
RUN pip install -r requirements.txt
ENTRYPOINT ["./entrypoint.sh"]
