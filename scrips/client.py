#!/usr/bin/python
import argparse
import socket

parser = argparse.ArgumentParser(description='Configura los parametros para lanzar escaneos desd SecDevOps')
parser.add_argument('--IP', type=str, nargs=?, help='IP del servidor donde se ejecuta el SecDevOps')
parser.add_argument('--port', type=int, nargs=?, help='puerto donde escucha el SecDevOps')
parser.add_argument('--url', type=str, nargs=?, help='URL a escanear')
parser.add_argument('--tipo', type=str, nargs=?, help='Tipo de escaneo, Estatico (e) o Dinamico (D)')
error=""

server_ip
server_port
url
tipo

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
	error="Es necesario ingresar la URL a testear(--url <url a escanear>)"


def conexion(server_ip):
	respuesta=''
	s = socket.socket()
	msg=u_mac+"->"+u_ip
	try:
		s.connect((server_ip, server_port))
		s.send(msg.encode())
		respuesta=s.recv(1)	
		s.close()
	except socket.error, msg:
		syslog.syslog(syslog.LOG_ERR,"Error con la conexion al Escaner- "+msg)

	return int(respuesta)



def validacion():

