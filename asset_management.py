import argparse, os, sys, subprocess, pprint, re
from shotgun_api3 import Shotgun

#Seccion Parser
parser = argparse.ArgumentParser(description = 'Creador de Versiones.')

parser.add_argument('--user', dest = 'User', action = 'store', help = 'user code')
parser.add_argument('--project', dest = 'Project', action = 'store', help = 'project code')
parser.add_argument('--asset', dest = 'Asset', action = 'store', help = 'asset code')
parser.add_argument('--id', dest = 'ID', action = 'store', help = 'id code')
parser.add_argument('--task', dest = 'Task', action = 'store', help = 'task code')
parser.add_argument('--path', dest = 'Path', action = 'store', help = 'path code')

args = parser.parse_args()

#print args.Asset

#Validacion
def checkArguments():
	argumentList = {'User':args.User,'Project':args.Project,'Asset':args.Asset, 'ID':args.ID,'Path':args.Path, 'Task':args.Task}
	for key, value in argumentList.iteritems():
		#Usar value para obtener el valor introducido
		if not value:
			print "ERROR: El elemento %s se encuentra vacio, asegurate de introducirlo" %key
		else:

			print "%s introducido con el valor: %s" %(key, value)

checkArguments()
#Convertir argumentos
file_name = str(args.Asset)
file_user = int(args.User)
file_project = int(args.Project)
file_id = int(args.ID)
file_task=int(args.Task)
file_path = str(args.Path)

#Seccion Shotgun
sg = Shotgun("https://upgdl.shotgunstudio.com", "RamonScript", "03f3c0095aa9ebe07a3006674ed8eda6c6b6ffcb8b4937a9c09fcb3264395f96")

#Subir versiones

entity = {'id': file_id, 'type':'Asset'}
task = {'id':file_task ,'type':'Task'}

filters = [['entity', 'is', entity],
				['sg_task', 'is', task]]
fields = ['created_at', 'code']

result = sg.find("Version", filters, fields)

version_token = r"v\d\d\d"
max_ver = 0
for ver in result:
	tokens = re.findall(version_token,ver['code'])
	if len(tokens) != 0:
		ver_num = int(tokens[0][1:])
		if  ver_num> max_ver:
			max_ver = ver_num

#Nomenclatura y versionado
pipe_name = "%sv%03d" %(file_name, max_ver + 1)
print pipe_name

data = {'code':pipe_name,
			'entity': entity,
			'description': 'Pipeline Test',
			'sg_task':task,
			'user':{'id':file_user, 'type': 'HumanUser'},
			'sg_status_list':'rev',
			'project':{'id':file_project,'type':'Project'}}

result = sg.create("Version", data)
pprint.pprint(result)

sg.upload("Version", result['id'], args.Path, field_name="sg_uploaded_movie",display_name="Latest Media")

#Creacion de elementos dentro de Shotgun
"""
data = {'code':file_name,
		'sg_asset_typ': 'Prop',
		'description': 'Pipeline Test',
		'project':{'id':file_project,'type':'Project'}}
result = sg.create("Asset", data)
"""