from subprocess import call
import sys
import os

#------------------------variable de entorno con el valor de nuestro grupo-----------------------------
os.environ['GROUP_NUMBER'] = '14'

#------------------------comandos de instalación-------------------------------------------------------
call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
call(["sudo","apt","update"])
call(["sudo","apt","install","docker.io"])

#------------------modificar requirements.txt-------------------------------------------------------
with open("practica_creativa2/bookinfo/src/productpage/requirements.txt","r") as file: 
    r = file.read()

with open("practica_creativa2/bookinfo/src/productpage/requirements.txt","w") as file:
    r = r.replace("urllib3==1.26.5", "urllib3<1.25")
    file.write(r)

#------------------modificar el productpage.html-------------------------------------------------------
with open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html","r") as file: 
    x = file.read()

with open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html","w") as file:
    x = x.replace("{% block title %}Simple Bookstore App{% endblock %}", "{% block title %}G"+os.environ['GROUP_NUMBER']+"{% endblock %}")
    file.write(x)

call(["sudo","docker","build","-t","pc2:3.8","."])
call(["sudo","docker","run","--name","pc2","-p9080:9080","pc2:3.8"])