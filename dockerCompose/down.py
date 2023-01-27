import os
from subprocess import call

call(["sudo", "docker-compose", "down"])
call(["sudo","docker", "rmi", "g14/ratings", "g14/reviews", "g14/productpage", "g14/details", "python:3.8", "ruby:2.7.1-slim", "node:12.18.1-slim", "gradle:4.8.1", "websphere-liberty:20.0.0.6-full-java8-ibmjava"])
print("\nClúster apagado correctamente.")
