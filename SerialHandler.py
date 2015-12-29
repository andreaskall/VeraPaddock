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
	data = port.readline()
	print(data),
	mode,data = parseData(data)
	if mode == "BASE":
		data = ",".join(data)
  		with open('data.txt','a') as txtFile:
  			txtFile.write(str(numberOfData)+',' + str(data) + "\n")
    		numberOfData += 1
