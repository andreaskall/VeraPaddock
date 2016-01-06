#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from matplotlib import style


####### HTML snippet to retrieve image of queen elizabeth olympic park
####### https://maps.googleapis.com/maps/api/staticmap?center=51.5399,-0.012778&zoom=16&size=600x550&scale=2&maptype=satellite
#######


#adjust these values based on your location and map, lat and long are in decimal degrees
TRX = 11.978420         #top right longitude
TRY = 57.696324         #top right latitude
BLX = 11.965645         #bottom left longitude
BLY = 57.690052         #bottom left latitude
lat_input = 0           #latitude of home marker
long_input = 0          #longitude of home marker

mapImage = plt.imread('map.png')


plt.rcParams['toolbar'] = 'None'
style.use('fivethirtyeight')

fig = plt.figure()
gs1 = gridspec.GridSpec(3, 3)
gs1.update(left=0.05, right=0.49, wspace=0.05)
temperature = plt.subplot(gs1[1, :])
speedFig    = plt.subplot(gs1[0, :])

gs2 = gridspec.GridSpec(4, 1)
gs2.update(left=0.5, right=0.99, wspace=0)
positionFig = plt.subplot(gs2[:,:1])

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
	plt.imshow(mapImage,extent=[BLX, TRX, BLY, TRY])
	positionFig.grid(False)
	positionFig.set_xticks([])
	positionFig.set_yticks([])
	#w,h = len(mapImage[0]), len(mapImage) 
	#aspect = float(w)/h
	positionFig.set_aspect(2)

	if position[0] != 'None':
		positionFig.set_xlabel('Connected')
		position = (float(position[0]), float(position[1]))
		positionFig.scatter(x=position[1], y=position[0], s = 50, c='r')
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