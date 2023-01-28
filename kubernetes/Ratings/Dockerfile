FROM node:12.18.1-slim

ENV SERVICE_VERSION v1

RUN apt-get update

RUN mkdir /opt/microservices/

COPY package.json /opt/microservices/

COPY ratings.js /opt/microservices/

WORKDIR /opt/microservices/

RUN npm install

EXPOSE 9080

ENTRYPOINT node ratings.js 9080