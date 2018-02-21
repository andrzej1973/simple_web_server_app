FROM ubuntu:latest
MAINTAINER Andrzej Mazur "andrzej@mazur.info"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["simple_web_server_app.py", "-p", "5000", "--host", "127.0.0.1"]