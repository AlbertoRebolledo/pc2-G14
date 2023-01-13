from subprocess import call
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logger")

if len(sys.argv) >= 2:
	orden = sys.argv[1]
	if len(sys.argv) = 3:
		comp = sys.argv[2]
else:
	logging.info("Debes introducir una orden.")
	exit()

if orden == "1":
	if len(sys.argv) == 3:
		comp = None
	call["python3", "mvpesada.py"]
elif orden == "2":
	if comp == "start":
		call["python3", "docker.py"]
	elif comp == "stop":
		call["python3", "stopDocker.py"]
	else:
		logging.info("Error: el tercer parámetro solo puede ser \"start\" o \"stop\"")
		exit()
