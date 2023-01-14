from subprocess import call
import sys
import os

def cambiarCompose(version):
    with open("docker-compose.yml", "r") as f:
        lines = f.readlines()
        if version == "v1":
            lines_version = ['          - service_version=v1\n' if "service_version" in line else line for line in lines]
            lines_ratings = ['          - enable_ratings=false\n' if "enable_ratings" in line else line for line in lines_version]
            lines_color = ['          - star_color=black\n' if "star_color" in line else line for line in lines_ratings]
        elif version == "v2":
            lines_version = ['          - service_version=v2\n' if "service_version" in line else line for line in lines]
            lines_ratings = ['          - enable_ratings=true\n' if "enable_ratings" in line else line for line in lines_version]
            lines_color = ['          - star_color=black\n' if "star_color" in line else line for line in lines_ratings]
        elif version == "v3":
            lines_version = ['          - service_version=v3\n' if "service_version" in line else line for line in lines]
            lines_ratings = ['          - enable_ratings=true\n' if "enable_ratings" in line else line for line in lines_version]
            lines_color = ['          - star_color=red\n' if "star_color" in line else line for line in lines_ratings]
        else:
            print("Elige una versión valida[v1, v2, v3]")

    with open("docker-compose.yml", "w") as f:
        f.writelines(lines_color)

version = sys.argv[1]
print(version)
'''
#------------------------comandos de instalación-------------------------------------------------------
call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
call(["sudo","apt","update"])
call(["sudo","apt","install","docker.io"])

#-------------------------mover ficheros------------------------------------------
call(["cp","practica_creativa2/bookinfo/src/productpage","ProductPage/"])
call(["cp","practica_creativa2/bookinfo/src/details/details.rb","Details/"])
call(["cp","practica_creativa2/bookinfo/src/ratings/package.json","Ratings/"])
call(["cp","practica_creativa2/bookinfo/src/ratings/ratings.js","Ratings/"])

#------------------------cosas de reviews----------------------------------------
os.chdir(r'practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg')
pwd = os.getcwd()
call(["sudo", "docker", "run", "--rm", "-u", "root", "-v", str(pwd)+":/home/gradle/project", "-w", "/home/gradle/project", "gradle:4.8.1", "gradle", "clean", "build"])
'''
    #----------------------imagenes de reviews---------------------------------------------------------------------------------hay que mirar lo de los argumentos
cambiarCompose(version)
'''
if version == "v1":
    #call(["sudo","docker","build","-t","reviews","practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"])
elif version == "v2":
    #call(["sudo","docker","build","-t","reviews","practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"])
elif version == "v3":
    #call(["sudo","docker","build","-t","reviews","practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"])

#----------------------------docker-compose----------------------------------------------
#call(["sudo","docker","compose","up"])
'''