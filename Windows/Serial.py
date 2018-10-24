# -*- coding: utf-8 -*-

import threading
import serial
import time
import os, sys

class Sondas(threading.Thread):
	def __init__(self):
		try:
		self.Puerto 
		threading.Thread.__init__(self)

	def run(self):
		
	def LoadInfo(self):
        try:
            #Obtengo la información
            Data = open("Data.smt", 'r').read()

            self.Vel =   int(Data.split(',')[1])
            self.Serial1 =   int(Data.split(',')[2])
            self.Serial2 =   int(Data.split(',')[3])
            self.Serial3 =   int(Data.split(',')[4])



        except:
            self.dataSMT.IdVel = 2
            self.dataSMT.Vel = 9800
            self.rbox.SetSelection(self.dataSMT.IdVel)




try:
	# Ejecutar un comando con "os.popen(comando)" y capturar el puerto serie disponible.
	comando4 = "ls /dev/ttyUSB*"
	PUERTO = os.popen(comando4).read()
	
	# Ejecutar un comando con "os.system(comando)" para darle permisos al puerto disponible.
	# Si su valor es 0 la ejecución finalizó con éxito.
	valor1 = os.system("sudo chmod a+rw "+PUERTO)
	#print (valor1)
	
	# Variable para saber si hemos encontrado el puerto o no
	bEncontrado = 0
	
	# Probamos abrir el puerto
	#print PUERTO[:-1]
	S = serial.Serial(PUERTO[:-1], 9600, parity=serial.PARITY_NONE, timeout=1)
	S.open()
except:
	pass
# Hacemos una condicion saber si encontramos un puerto 
if (valor1 == 0):
    try:
        # Puerto que vamos a probar
        #print S.isOpen()
        if (S.isOpen()):
			# cambiamos el estado de la variable para saber que lo hemos encontrado
			bEncontrado = 1
		
    except:
        # Si hay error, no hacemos nada y continuamos con la busqueda
        bEncontrado = 0
        pass
	
#if len(sys.argv) >= 2:
sonda1 = sys.argv[1]
sonda2 = sys.argv[2]
sonda3 = sys.argv[3]
	
# Mientras encontremos el puerto abierto	
while (bEncontrado == 1):
	try:
		#a=open('sonda.ky','w')
		# Mostramos el puerto de las sondas
		#print('El puerto es: ' + '/dev/ttyUSB' + str(iPuerto))
		#print '\nEstado del puerto: %s ' % (S.isOpen()) 
		S.write('M'+sonda1+'\r\n')   # Tanque 1 
		S.reset_input_buffer()
		S.flush()
		time.sleep(1)
		# leemos hasta que encontramos el final de linea
		s1 = S.readline()
		print s1
		time.sleep(1)
		S.reset_input_buffer()
		
		S.write('M'+sonda2+'\r\n')   # Tanque 2 
		S.reset_input_buffer()
		time.sleep(1)
		s2 = S.readline()
		time.sleep(1)
		S.reset_input_buffer()
		
		S.write('M'+sonda3+'\r\n')   # Tanque 3 
		S.reset_input_buffer()
		time.sleep(1)
		s3 = S.readline()
		time.sleep(1)
		S.reset_input_buffer()
		
		with open('sonda.ky','w') as miArchivo:
			miArchivo.write(s1)
			miArchivo.write(s2)
			miArchivo.write(s3)
			#print "OK"
		
		# Cerramos el archivo y el puerto
		#a.close()
		S.close()
		# Salimos del bucle
		break
		sys.exit()
	except: 
		bEncontrado = 0
		pass
		sys.exit()
