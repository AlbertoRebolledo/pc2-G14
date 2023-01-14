FROM node:12.18.1-slim

ENV SERVICE_VERSION v1

RUN apt-get update

RUN mkdir /opt/microservices/

COPY ../practica_creativa2/bookinfo/src/ratings/package.json /opt/microservices/

COPY ../practica_creativa2/bookinfo/src/ratings/ratings.js /opt/microservices/

WORKDIR /opt/microservices/

RUN npm install

EXPOSE 9080

ENTRYPOINT node ratings.js 9080