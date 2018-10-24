# -*- coding: utf-8 -*-

import serial
import time
try:
	ser = serial.Serial( # set parameters, in fact use your own :-)
		port="COM55",
		baudrate=9600,
		timeout = 1
	)
	ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
	print ("port is opened!")

except IOError: # if port is already opened, close it and open it again and print message
	ser = serial.Serial( # set parameters, in fact use your own :-)
		port="COM55",
		baudrate=9600,
		timeout = 1
	)
	ser.close()
	ser.open()
	print ("port was already open, was closed and opened again!")

for u in range(100):
	try:
		ser.write(b'M32099\r\n')
		time.sleep(0.25)
		Trama = str(ser.readline()).split('=');
		try:
			if(len(Trama)==5):
				Serial = Trama[0]
				Serial = str(str(Serial).split('N')[0])
				try:
					print('\nIteracion: ' + str(u+1)+'\n')
					print(Serial)
				except e as Exception:
					print(e)
					pass
		except e as Exception:
			ser.close()
		print(Trama)
	except:
		ser.close()
ser.close()