import matplotlib.pyplot as plt

#filename = raw_input("Enter telemetry filename: ")
filename = 'test.tsv'
file = open(filename)

lines = 0
data_in = []
for line in file:
	lines = lines + 1
	data_in.append(line.split('\t'))

channel_count = len(data_in[1])-2
channel_names = data_in[0][1:channel_count+2]

n = 0
for channel in channel_names:
	print n,
	print ": ",
	print channel
	n = n + 1

selected_channel = input("Select a channel to plot: ")
print "Selected: ",
print channel_names[selected_channel]

data2 = []
times = []
for n in range(1, lines):
	times.append(data_in[n][0])
	data2.append(data_in[n][selected_channel+1])

print data2
print times

data3 = []
times2 = []
for num in data2:
	data3.append(float(num))


for num in times:
	times2.append(float(num))


plt.plot(times2, data3)
plt.show()

#data2 = {}
#for n in range(0, channel_count):
#	data2[channel_names[n]] = data_in[1:][n+1]
#	n = n + 1

print "done"