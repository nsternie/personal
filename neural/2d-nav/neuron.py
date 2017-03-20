# neuron.py
import numpy

class Neuron(object):

	def __init__(self, num_inputs):
		self.weights = [] 	
		for n in range(0, num_inputs):
			self.weights.append(0.0)
		self.activation = '(1/(1+(2.718**(-z))))'
		self.activation_prime = '(2.718**(-z))/((1+(2.718**(-z)))**2)'
		self.out = 0.0

	def update(self, inputs):
		w = numpy.array(self.weights)
		i = numpy.array(inputs)
		e = w * i
		z = sum(e)
		self.out = eval(self.activation)