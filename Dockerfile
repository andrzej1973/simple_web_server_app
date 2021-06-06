FROM arm32v7/python:3.9.5-buster
MAINTAINER andrzej@mazur.info
WORKDIR /usr/PyScripts/simple_web_server_app/src
COPY ./requirements.txt /usr/PyScripts/simple_web_server_app/
COPY ./src/* /usr/PyScripts/simple_web_server_app/src/
RUN pip3 install -r ../requirements.txt
CMD ["python3", "./simple_web_server.py"]

