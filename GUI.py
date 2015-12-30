#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style




#adjust these values based on your location and map, lat and long are in decimal degrees
TRX = 11.979496          #top right longitude
TRY = 57.695401          #top right latitude
BLX = 11.967124          #bottom left longitude
BLY = 57.691521          #bottom left latitude
lat_input = 0            #latitude of home marker
long_input = 0           #longitude of home marker

mapImage = plt.imread('map.png')


plt.rcParams['toolbar'] = 'None'
style.use('fivethirtyeight')

fig = plt.figure()
temperature = plt.subplot2grid((3, 4), (1, 0), colspan=2)
speedFig = plt.subplot2grid((3, 4), (0, 0), colspan=2)
positionFig = plt.subplot2grid((3,4),(0,2), colspan=2, rowspan=2)

def animate(i):
	graph_data = open('data.txt','r').read()
	lines = graph_data.split('\n')
	xs = []
	cylinderTemp = []
	cylinderHeadTemp = []
	engineBlockTemp = []

	speed = []

	position = (0,0)
	
	for line in lines:
		if len(xs) >50:
			xs = xs[1:]
			cylinderTemp = cylinderTemp[1:]
			cylinderHeadTemp = cylinderHeadTemp[1:]
			engineBlockTemp = engineBlockTemp[1:]

			speed = speed[1:]
			
		if len(line)>1:
			data = line.split(',')
			if data[1] != 'None':
				xs.append(data[0])
				cylinderTemp.append(data[1])
				cylinderHeadTemp.append(data[2])
				engineBlockTemp.append(data[3])
				speed.append(data[10])
			else:
				xs.append(data[0])
				cylinderTemp.append(0)
				cylinderHeadTemp.append(0)
				engineBlockTemp.append(0)
				speed.append(0)


			

	position = (lines[-2].split(',')[11], lines[-2].split(',')[12])
	positionFig.clear()
	positionFig.set_title('Position')
	plt.imshow(mapImage,extent=[BLX, TRX, BLY, TRY])
	positionFig.grid(False)
	positionFig.set_xticks([])
	positionFig.set_yticks([])
	w,h = len(mapImage[0]), len(mapImage) 
	aspect = float(w)/h
	positionFig.set_aspect(aspect)

	if position[0] != 'None':
		positionFig.set_xlabel('Connected')
		position = (float(position[0]), float(position[1]))
		positionFig.scatter(x=[position[1]], y=[position[0]], s = 20, c='r')
	else:
		positionFig.set_xlabel('Not connected')
		

	temperature.clear()
	temperature.set_title('Temperatures [C]')
	temperature.plot(xs, cylinderTemp, linewidth=2.0, label='Cylinder')
	temperature.plot(xs, cylinderHeadTemp, linewidth=2.0, label='Cylinder head')
	temperature.plot(xs, engineBlockTemp, linewidth=2.0, label='Engine block')
	temperature.legend(framealpha=0.5)

	speedFig.clear()
	speedFig.set_title('Speed')
	speedFig.set_ylabel('Km/h')
	speedFig.plot(xs, speed, linewidth=2.0, label='Speed')
	speedFig.legend(framealpha=0.5)
	speedFig.xaxis.set_major_formatter(plt.NullFormatter())


	positionFig
try:
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()
except:
	sys.exit()