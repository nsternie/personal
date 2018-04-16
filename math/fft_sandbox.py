import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import numpy as np

Fs = 44100

data = np.memmap("tone.raw", dtype='h', mode='r')

# f = fft(data)
# freq = np.linspace(0, Fs/len(data), Fs/2)
# temp = f[:len(data)]
# plt.plot(freq, temp)
# plt.show()    
# # freq = 10
# t = [n/freq for n in range(1000*freq)]
# x = [np.sin(val)+np.sin(2*val) for val in t]
# plt.plot(x, label="time_domain")
# f = fft(x)
# plt.plot(np.abs(f), label="fft")
# plt.show() 

# from scipy.fftpack import fft
# Number of sample points
N = len(data)
# sample spacing
T = 1.0 / 44100.0
x = np.linspace(0.0, N*T, N)
y = data
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
# import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.xlim(0, 2500)
plt.grid()
plt.show()