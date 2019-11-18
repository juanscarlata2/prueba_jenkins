print("Hola Mundo")
a=2

if a==2:
	print ("Es dos")
def hacer():
	global a
	a=34
	return a

def ejecutar():
	global a
	hacer()
	print a


ejecutar()
