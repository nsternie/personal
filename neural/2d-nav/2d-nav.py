# Will generate a
# 
# 
import pointGen as pg 
import neuron
import random as rand

neurons = []

##################################
# Configuration
num_neurons = 5			# How many neurons will be used in the neural network
iterations = 100
test_cases = 100000
weight_range = 5
bias_range = 20
##################################

dx = neuron.Neuron(num_neurons)
dy = neuron.Neuron(num_neurons)
lowest_error = 10000
best_weights = []
best_biases = []

for n in range(0, num_neurons):
	neurons.append(neuron.Neuron(4))

for loop in range(0, test_cases):
	# Generate the info used to train it. Look at pointGen.py for more info
	
	# Generate random weights and bias for each neuron
	for n in range(0, num_neurons):
		neurons[n].weights = [rand.uniform(-weight_range, weight_range),rand.uniform(-weight_range, weight_range),rand.uniform(-weight_range, weight_range),rand.uniform(-weight_range, weight_range)]
		neurons[n].bias = rand.uniform(0,bias_range)
		
	# Generate weights for the output neurons
	for m in range(0, num_neurons):
		dx.weights[m] = rand.uniform(-weight_range, weight_range)
		dy.weights[m] = rand.uniform(-weight_range, weight_range)

	dx.bias = rand.uniform(0, bias_range)
	dy.bias = rand.uniform(0, bias_range)
	tot_err = 0
	for foo in range(0, iterations):
		raw = pg.generate(0,1)
		inputs = raw[0:4]
		intermediate = []
		for n in range(0, num_neurons):
			neurons[n].update(inputs)
			intermediate.append(neurons[n].out)
		dx.update(intermediate)
		dy.update(intermediate)

		x_error = dx.out - raw[4]
		y_error = dy.out - raw[5]

		abs_error = ((x_error**2)+(y_error**2))**(0.5)
		tot_err += abs_error
	avg_error = tot_err/iterations
	if avg_error < lowest_error:
		lowest_error = avg_error
		print avg_error

print 'Lowest average error attained was',
print lowest_error


		