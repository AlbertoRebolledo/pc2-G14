from subprocess import call
import sys
import os

def cambiarVersion(version):
    with open("docker-compose.yml", "r") as f:
        lines = f.readlines()
    if version == "v1":
        lines_version = ['      - SERVICE_VERSION=v1\n' if "SERVICE_VERSION" in line else line for line in lines]
        lines_ratings = ['      - ENABLE_RATINGS=false\n' if "ENABLE_RATINGS" in line else line for line in lines_version]
        lines_color = ['      - STAR_COLOR=black\n' if "STAR_COLOR" in line else line for line in lines_ratings]
    elif version == "v2":
        lines_version = ['      - SERVICE_VERSION=v2\n' if "SERVICE_VERSION" in line else line for line in lines]
        lines_ratings = ['      - ENABLE_RATINGS=true\n' if "ENABLE_RATINGS" in line else line for line in lines_version]
        lines_color = ['      - STAR_COLOR=black\n' if "STAR_COLOR" in line else line for line in lines_ratings]
    elif version == "v3":
        lines_version = ['      - SERVICE_VERSION=v3\n' if "SERVICE_VERSION" in line else line for line in lines]
        lines_ratings = ['      - ENABLE_RATINGS=true\n' if "ENABLE_RATINGS" in line else line for line in lines_version]
        lines_color = ['      - STAR_COLOR=red\n' if "STAR_COLOR" in line else line for line in lines_ratings]
    else:
        print("Elige una versión valida[v1, v2, v3]")
        exit()

    with open("docker-compose.yml", "w") as f:
        f.writelines(lines_color)

version = sys.argv[1]

#-----------------------------cambiar versión en fichero compose-----------------------------------------
#cambiarVersion(version)

#------------------------comandos de instalación-------------------------------------------------------
call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
call(["sudo","apt","update"])

#-------------------------mover ficheros------------------------------------------
call(["cp","-r","practica_creativa2/bookinfo/src/productpage/","ProductPage/"])
call(["cp","practica_creativa2/bookinfo/src/details/details.rb","Details/"])
call(["cp","practica_creativa2/bookinfo/src/ratings/package.json","Ratings/"])
call(["cp","practica_creativa2/bookinfo/src/ratings/ratings.js","Ratings/"])

#------------------------cosas de reviews----------------------------------------
os.chdir(r'practica_creativa2/bookinfo/src/reviews')
pwd = os.getcwd()
call(["sudo", "docker", "run", "--rm", "-u", "root", "-v", str(pwd)+":/home/gradle/project", "-w", "/home/gradle/project", "gradle:4.8.1", "gradle", "clean", "build"])
os.chdir(r"../../../../")

#--------------------------------creación de las imagenes del resto de microservicios-------------------------
if version == "v1":
    call(["sudo","docker","build","-t","g14/reviews-v1","practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"])
elif version == "v2":
    call(["sudo","docker","build","-t","g14/reviews-v2","practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"])
elif version == "v3":
    call(["sudo","docker","build","-t","g14/reviews-v3","practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"])

call(["sudo","docker","build","-t","g14/productpage","ProductPage/"])
call(["sudo","docker","build","-t","g14/details","Details/"])
call(["sudo","docker","build","-t","g14/ratings","Ratings/"])

#----------------------------------lanzamineto de kubernetes--------------------------------------------------
call(["kubectl","apply","-f","practica_creativa2/bookinfo/platform/kube/reviews-svc.yaml"])
call(["kubectl","apply","-f","Productpage/productPage.yaml"])
call(["kubectl","apply","-f","Details/details.yaml"])
call(["kubectl","apply","-f","Ratings/ratings.yaml"])

if version == "v1":
    call(["kubectl","apply","-f","Reviews/reviews-v1-deployment.yaml"])
elif version == "v2":
    call(["kubectl","apply","-f","Reviews/reviews-v2-deployment.yaml"])
elif version == "v3":
    call(["kubectl","apply","-f","Reviews/reviews-v3-deployment.yaml"])

#--------------------------------exponer puerto--------------------------------------------------------
call(["kubectl","expose","deployment","productpage-v1","--type=LoadBalancer","--","port=9080"])