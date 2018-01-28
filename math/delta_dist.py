import pandas as pd
import sys
import matplotlib.pyplot as plt

print("Opening input data")
data = pd.read_csv(sys.argv[1])
data_col = 1
if len(sys.argv) == 3:
	data_col = sys.argv[2]
	print("Using column", sys.argv[2])

list_in = data[data_col]

delta = [list_in[n+1] - list_in[n] +100 for n in range(0, len(list_in)-1)]

dist = [0]*1000
for element in delta:
	dist[element] += 1

plt.plot(dist)
plt.show()