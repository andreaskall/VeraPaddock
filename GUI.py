#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	graph_data = open('data.txt','r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []
	for line in lines:
		if len(line)>1:
			data = line.split(',')
			xs.append(data[0])
			ys.append(data[1])

	ax1.clear()
	ax1.plot(xs, ys)
try:
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()
except:
	sys.exit()