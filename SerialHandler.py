#!/usr/bin/env python
import serial, time

numberOfData = 0
port = serial.Serial('/dev/tty.usbserial-FTB3M4C2', 9600)
open('data.txt', 'w').close()

def parseData(dataString):
	mode, data = dataString.split(':')
	mode = mode.split('#')[1]
	data=data.split('+')
	data[-1] = data[-1].split('&')[0]
	return (mode,data)


while True:
	try:
		data = port.readline()
	except:
		data = None
		try:
			port.close()
		except:
			pass
		try:
			port = serial.Serial('/dev/tty.usbserial-FTB3M4C2', 9600)
		except:
			pass
	print(data),
	if data != None:
		mode,data = parseData(data)
		if mode == "BASE":
			data = ",".join(data)
  			with open('data.txt','a') as txtFile:
  				txtFile.write(str(numberOfData)+',' + str(data) + "\n")
    			numberOfData += 1
   	else:
   		time.sleep(1)
