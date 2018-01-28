import matplotlib.pyplot as plt

limit = 50

data = []

for n in range(1, limit):
	temp = n**2
	rem = temp % 100
	data.append(rem)
	print(rem)
#print(sums)
plt.plot(s)
#plt.show()