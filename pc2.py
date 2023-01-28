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
	if comp == "v1":
		call(["python3", "compose.py", "v1"])
	elif comp == "v2":
		call(["python3", "compose.py", "v2"])
	elif comp == "v3":
		call(["python3", "compose.py", "v3"])
	elif comp == "down":
		call(["python3", "down.py"])
elif orden == "help":
	print("\nFuncionamiento de la Práctica 2 de CDPS:")
	print("Modo de uso: python3 pc2.py <ORDEN> <ACCION>\n")
	print("Ordenes:")
	print(" - monolith: despliega la aplicación en la máquina actual de forma monolítica")
	print("\n - docker: despliega la aplicación en un contenedor Docker de forma monolítica")
	print("   Acciones:")
	print("    - start: arranca la aplicación")
	print("    - stop: para la aplicación y elimina todas las dependencias")
	print("\n - compose: ejecuta la aplicación con microservicios en distintos contenedores conectados entre sí")
	print("   Acciones:")
	print("    - v1: versión 1 del servicio (ratings desactivado")
	print("    - v2: versión 2 del servicio (ratings activado con estrellas negras)")
	print("    - v3: versión 3 del servicio (ratings activado con estrellas rojas)")
	print("    - down: para los contenedores y los elimina, así como las imágenes de las que dependen")

else:
	logging.error("El primer parámetro solo puede ser: \"monolith\", \"docker\", \"compose\" o \"kubernetes\"")
