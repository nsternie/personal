import telemtools
import time
import os

s = telemtools.stream(port='COM12', baudrate=115200)

s.load_template(file='telemetry_master.template')

p = telemtools.plot()
p.load('test.tsv')
#p.plot_channel('val3')
print(p.channel_names)
print(p.units)

print(p.channel_data['time'])
print(p.channel_data['thrust'])
p.plot_single_channel('thrust')
#s.read_buffer(timeout=1)

#print(s.packet_length)

