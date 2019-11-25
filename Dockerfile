FROM ubuntu:18.04
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev
RUN pip3 install Flask
ADD app /app
WORKDIR /app
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD ["env","FLASK_APP=app.py","flask","run","--host=0.0.0.0","--port=80"]
EXPOSE 80
