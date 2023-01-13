from subprocess import call

call(["sudo", "docker", "stop", "g14-productpage"])
call(["sudo", "docker", "rm", "g14-productpage"])
call(["sudo", "docker", "rmi", "g14/product-page"])
