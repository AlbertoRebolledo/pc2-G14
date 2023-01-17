from subprocess import call
import time
import os
#------------------------comandos de instalación-------------------------------------------------------
call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
call(["sudo","apt","update"])
call(["sudo","apt","install","docker.io"])

call(["sudo","docker","build","-t","g14/product-page","."])
call(["sudo","docker","run", "-d", "--name","g14-productpage","-p9080:9080","g14/product-page"])
call(["rm", "-rf", "practica_creativa2"])

log = "INFO:root:start at port 9080"
cmd = "sudo docker logs g14-productpage"
i = 48
while i > 0:
	time.sleep(5)
	f = os.popen(cmd)
	logs = f.readlines()
	if log in logs[-3]:
		print("¡¡¡APLICACIÓN OPERATIVA!!!")
		exit()
	i = i-1
