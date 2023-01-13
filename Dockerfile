FROM python:3.8

RUN apt-get update && apt-get -y install python3-pip

COPY practica_creativa2 /home/

RUN pip3 install -r /home/bookinfo/src/productpage/requirements.txt

EXPOSE 9080

ENTRYPOINT python3 /home/bookinfo/src/productpage/productpage_monolith.py 9080