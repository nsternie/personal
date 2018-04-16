import numpy as np 
import matplotlib.pyplot as plt
import random

mu = 0
sigma = 0.1

Fs = 100
samples = 10000

data = []

def signal(n):
    return np.sin(n)

def sum(data, length):
    s = 0
    for n in range(length):
        s += data[n]
    return (s/length)

def moving_average(data, window):
    averaged_data = data
    for n in range(0, window):
        averaged_data[n] = sum(data, n+1)
    for n in range(window, len(data)):
        averaged_data[n] = sum(data[int(n-window/2):int(n+window/2)], window)
    return averaged_data

for n in range(samples):
    data.append(signal(n/(Fs*2*np.pi)) + random.normalvariate(mu, sigma))

#data.sort()
plt.plot(data, label="raw")
ma10 = moving_average(data, 10)
plt.plot(ma10, label="Moving average 10")
ma20 = moving_average(data, 20)
plt.plot(ma20, label="Moving average 20")
plt.legend()
plt.show()