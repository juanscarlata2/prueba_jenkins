#!/usr/bin/python
import argparse
import socket
import sys
import json

parser = argparse.ArgumentParser(description='Configura los parametros para lanzar escaneos desd SecDevOps')
parser.add_argument('--IP', type=str, help='IP del servidor donde se ejecuta el SecDevOps')
parser.add_argument('--port', type=int, help='puerto donde escucha el SecDevOps')
parser.add_argument('--url', type=str, help='URL a escanear')
parser.add_argument('--tipo', type=str, help='Tipo de escaneo, Estatico (e) o Dinamico (d)')
error=0


args = parser.parse_args()

server_ip=0
server_port=0
url=0
tipo=0

if args.IP:
	server_ip=args.IP
else:
	error="Es necesario ingresar la IP del servidor (--IP <IP del servidor>)"

if args.port:
	server_port=args.port
else:
	error="Es necesario ingresar la IP del servidor (--port <Puerto en el que escucha el servidor>)"

if args.url:
	url=args.url
else:
	error="Es necesario ingresar la URL a testear(--url <url a escanear>)"

if args.tipo:
	tipo=args.tipo
else:
	error="Es necesario ingresar el tipo de escaneo(--tipo <Dinamico (d) o Estatico (e)>)"

if error:
	print error
	sys.exit()


def conexion():
	respuesta=''
	s = socket.socket()
	msg=url+'*a'
	try:
		s.connect((server_ip, server_port))
		s.send(msg.encode())
		respuesta=s.recv(256)
		with open('data.json', 'w') as outfile:
			json.dump(respuesta, outfile)
		s.close()
	except socket.error, msg:
		print "Error con la conexion al SecDevOps: "+str(msg)
		
conexion()
#sh 'python prueba_jenkins/scripsclient.py --IP localhost --port 6969 --url juan --tipo a'









