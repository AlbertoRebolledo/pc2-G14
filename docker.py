from subprocess import call

#------------------------comandos de instalación-------------------------------------------------------
call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
call(["sudo","apt","update"])
call(["sudo","apt","install","docker.io"])

call(["sudo","docker","build","-t","g14/product-page","."])
call(["sudo","docker","run","--name","g14-productpage","-p9080:9080","g14/product-page"])
