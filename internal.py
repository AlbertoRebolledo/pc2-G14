from subprocess import call
import sys
import os

#------------------modificar requirements.txt-------------------------------------------------------
with open("/home/app/bookinfo/src/productpage/requirements.txt","r") as file: 
    r = file.read()

with open("/home/app/bookinfo/src/productpage/requirements.txt","w") as file:
    r = r.replace("urllib3==1.26.5", "urllib3<1.25")
    file.write(r)

#------------------modificar el productpage.html-------------------------------------------------------
with open("/home/app/bookinfo/src/productpage/templates/productpage.html","r") as file: 
    x = file.read()

with open("/home/app/bookinfo/src/productpage/templates/productpage.html","w") as file:
    x = x.replace("{% block title %}Simple Bookstore App{% endblock %}", "{% block title %}G"+os.environ['GROUP_NUMBER']+"{% endblock %}")
    file.write(x)

#--------------------------instalación de dependencias----------------------------------------------
call(["pip3","install","-r","/home/app/bookinfo/src/productpage/requirements.txt"])

call(["python3","/home/app/bookinfo/src/productpage/productpage_monolith.py","9080"])
