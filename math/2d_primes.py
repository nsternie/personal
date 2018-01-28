import numpy as np
import matplotlib.pyplot as plt

upper_limit = 10

S = [np.array([[n], [m]]) for n in range(2, upper_limit) for m in range(2, upper_limit)]
O = [np.array([[0],[0]])]

for v in S:
	for w in S:
		res = (np.multiply(v,w))
		if not any(np.array_equal(res, test) for test in O):
			O.append(res)
			plt.scatter(res[0][0], res[1][0])

plt.xlim(0, upper_limit*2)
plt.ylim(0, upper_limit*2)
plt.show()
print(O)