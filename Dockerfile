FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev
RUN pip3 install Flask
ADD app /app
WORKDIR /app
CMD ['env','FLASK_APP=app.py','flask','run']
