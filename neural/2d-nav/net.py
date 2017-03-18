# net.py

class Neural_Network(object):

	def __init__(self, config_file):
		config open(config_file, 'r')
		config_array = []
		for line in config:
			line_split = split(line)
			config_array.append(line_split[1])
		self.activation = config_array[0]
		self.inputs = config_array[1]
		self.outputs = config_array[2]
		self.layers = config_array[3]


