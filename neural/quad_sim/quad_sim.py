import quad
import matplotlib.pyplot as plt

q = quad.Quadcopter('quad.config')

#q.print_variables()

logfile = 'quad.log'

t = [00.0,10.0,0.0,10.0]
q.set_throttle(t)

x = []
y = []
z = []
time = []

q.log(logfile)

for n in range(1000):
	q.step()
t = [00.0,5.0,0.0,10.0]
q.set_throttle(t)
for n in range(2000):
	q.step()
t = [00.0,0.0,0.0,0.0]
q.set_throttle(t)
for n in range(1000):
	q.step()

q.close_log()

data = open(logfile, 'r')

for line in data:
	cols = line.split(',')
	time.append(float(cols[0]))
	x.append(float(cols[1]))
	y.append(float(cols[2]))
	z.append(float(cols[3]))


plt.plot(time,x)
plt.plot(time,y)
plt.plot(time,z)
plt.show()