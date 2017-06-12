import argparse
import os, sys, subprocess, time

from shotgun_api3 import Shotgun
parser = argparse.ArgumentParser(description = 'Creador de Versiones.')
args = parser.parse_args()

sg = Shotgun("https://upgdl.shotgunstudio.com", "RamonScript", "03f3c0095aa9ebe07a3006674ed8eda6c6b6ffcb8b4937a9c09fcb3264395f96")
print sg.base_url


#Funciones de validacion
def validateOption(userInput):
	while True:
		if(userInput == "preview"):
			return "Preview"
		elif(userInput == "asset"):
			return "Asset"
		else:
			userInput = raw_input("ERROR. El tipo de archivo no existe, vuelve a intentar\n Que quieres subir?\n>Asset\n>Preview\n").lower()
			#validateOption(recurisveInput)

def validateID(userInput):
	while True:
		try:
			userInput = int(userInput)
			return int(userInput)
		except:
			userInput = raw_input ("ERROR. El ID debe ser un numero entero\n Intentar otro valor\n")
			#validateID(recurisveInput)

def validateShotgunID(userInput):
	while True:
		result = sg.find_one(file_type, [["id", "is", userInput]], ["id", "code", "sg_status_list"])
		if(result == None):
			newInput = raw_input("El %s no tiene el ID %03d, intenta con otro numero\n" %(file_type, userInput))
			try:
				userInput = validateID(newInput)
			except exception as e:
				print e
		else:
			print ("El %s tiene el codigo: %s" %(file_type,result['code']))
			return	result


#Entrada inicial del usuario
userOption = raw_input("Que tipo de archivo quieres trabajar?\n>Asset\n>Preview\n").lower()
file_type = validateOption(userOption)
#Usuario define el ID del elemento
assetID = raw_input("Cual es el ID de tu archivo?\n")
file_ID = validateID(assetID)
#Revisamos que el elemento se encuentre dentro de shotgun
shotgun_Info = validateShotgunID(file_ID)

time.sleep(5)