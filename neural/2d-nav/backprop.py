# Backprop.py
# Basic example to explore how to create a simple neural net with backpropagation
# Goal of neural net is the same as in 2d-nav.py
import pointGen as pg 
import neuron
import random as rand

generations = 10
test_cases
num_neurons = 5
num_inputs = 4
num_outputs = 2
weight_range = 10

# Initialize the neurons in the net and generate initial random synapse weights	
hidden_neurons = []
for n in range(0, num_neurons):
	hidden_neurons.append(neuron.Neuron(num_inputs))
	random_array = []
	for r in range(0, num_inputs):
		random_array.append(random.uniform(-weight_range, weight_range))
	hidden_neurons[n].weights = random_array
output_neurons = []
for n in range(0, num_outputs):
	output_neurons.append(neuron.Neuron(num_neurons))
	random_array = []
	for r in range(0, num_neurons):
		random_array.append(random.uniform(-weight_range, weight_range))
	output_neurons.append(random_array)



for gen in range(0, generations):
	output_errors_x = []
	output_errors_y = []
	neuron_activities = []

	# Get a bunch o' data from test cases
	for t in range(0,test_cases):
		data = pg.generate(0,1)
		inputs = data[0:4]
		activities = []
		for n in hidden_neurons:
			n.update(inputs)
			activties.append(n.out)
		neuron_activities.append(activities)
		for n in output_neurons:
			n.update(activities)
		output_errors_x.append(output_neurons[0].out - raw[4])
		output_errors_y.append(output_neurons[1].out - raw[5])

