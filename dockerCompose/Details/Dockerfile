FROM ruby:2.7.1-slim

ENV SERVICE_VERSION v1

ENV ENABLE_EXTERNAL_BOOK_SERVICE true

RUN apt-get update

RUN mkdir /opt/microservices/

COPY details.rb /opt/microservices/

EXPOSE 9080

ENTRYPOINT ruby /opt/microservices/details.rb 9080