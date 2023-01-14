FROM python:3.8

RUN apt-get update && apt-get -y install python3-pip

ENV GROUP_NUMBER 14

RUN mkdir /home/app/

COPY productpage /home/app/

COPY internal.py /home/app/

EXPOSE 9080

ENTRYPOINT python3 /home/app/internal.py