from subprocess import call
import sys
import os
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
	logger.error("Debes introducir una orden.")
	exit()

if orden == "monolith":
	os.chdir(r"./MVPesada")
	logger.info(os.getcwd())
	call(["python3", "mvpesada.py"])
elif orden == "docker":
	os.chdir(r"./dockerVirtualizacionL")
	logger.info(os.getcwd())
	if comp == "start":
		call(["python3", "docker.py"])
	elif comp == "stop":
		call(["python3", "stopDocker.py"])
	else:
		logger.error("Error: el tercer parámetro solo puede ser \"start\" o \"stop\"")
		exit()
elif orden == "compose":
	os.chdir(r"./dockerCompose")
	logger.info(os.getcwd())
else:
	logging.error("El primer parámetro solo puede ser: \"monolith\", \"docker\", \"compose\" o \"kubernetes\"")
