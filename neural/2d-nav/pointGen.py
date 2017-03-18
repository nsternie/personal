# pointGen.py
# Will generate a random set of points, return pair 1, pair 2, and the delta
# Purpose is for input to a basic neural network will attempt to predict the 
# delta from the two points

import random

def generate(lower, upper):
	out = []
	x1 = random.uniform(lower, upper)
	out.append(x1)
	y1 = random.uniform(lower, upper)
	out.append(y1)
	x2 = random.uniform(lower, upper)
	out.append(x2)
	y2 = random.uniform(lower, upper)
	out.append(y2)
	out.append((x1 - x2))
	out.append((y1 - y2))

	return out

# Future me: turns out you have to close and reopen it for an update
# to a module to be recognized. (You spend 20 minutes debugging a non
# existant problem while writing this)