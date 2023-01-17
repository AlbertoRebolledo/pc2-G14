from subprocess import call
call(["git", "config", "--global", "user.email", "alberto.rebolledo.j@gmail.com"])
call(["git", "config", "--global", "user.name", "\"AlbertoRebolledo\""])
print("Se han configurado variables globales de git. Ahora puedes utilizar git commit para guardar los cambios.")
