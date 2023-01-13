from subprocess import call
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logger")

if len(sys.argv) >= 2:
	orden = sys.argv[1]
	if len(sys.argv) == 3:
		comp = sys.argv[2]
	else:
		comp = ""
else:
	logging.error("Debes introducir una orden.")
	exit()

if orden == "monolith":
	call(["python3", "MVPesada/mvpesada.py"])
elif orden == "docker":
	if comp == "start":
		call(["python3", "dockerVirtualizacionL/docker.py"])
	elif comp == "stop":
		call(["python3", "dockerVirtualizacionL/stopDocker.py"])
	else:
		logging.error("Error: el tercer parámetro solo puede ser \"start\" o \"stop\"")
		exit()
else:
	logging.error("El primer parámetro solo puede ser: \"monolith\", \"docker\", \"compose\" o \"kubernetes\"")
