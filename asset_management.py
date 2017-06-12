import argparse
import os, sys, subprocess, time

from shotgun_api3 import Shotgun
parser = argparse.ArgumentParser(description = 'Creador de Versiones.')
args = parser.parse_args()

sg = Shotgun("https://upgdl.shotgunstudio.com", "RamonScript", "03f3c0095aa9ebe07a3006674ed8eda6c6b6ffcb8b4937a9c09fcb3264395f96")
print sg.base_url


#Funciones de validacion
def validateOption(userInput):
	if(userInput == "preview"):
		return "Preview"
	elif(userInput == "shot"):
		return "Shot"
	else:
		recurisveInput = raw_input("ERROR. El tipo de archivo no existe, vuelve a intentar\n Que quieres subir?\n>Shot\n>Preview\n").lower()
		validateOption(recurisveInput)


userOption = raw_input("Que tipo de archivo quieres trabajar?\n>Asset\n>Preview\n").lower()
file_type = validateOption(userOption)

time.sleep(5)