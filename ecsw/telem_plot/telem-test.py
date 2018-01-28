import telemtools
import time
import os

if (0):
	s = telemtools.stream(port='COM12', baudrate=115200)
	s.load_template(file='telemetry_master.template')

if (1):
	p = telemtools.plot()
	p.load('test.tsv')

	#p.plot_single_channel('thrust')
	p.plot_single_channel('tank_press')
	#p.show()

	print(p.integrate(channel='test', start=10, end=110))


