# net.py

class Neural_Network(object):

	# Mostly just parses the config
	def __init__(self, config_file):
		config open(config_file, 'r')
		config_array = []
		for line in config:
			line_split = split(line)
			config_array.append(line_split[1])
		self.activation = config_array[0]
		self.num_layers = config_array[1]
		
		self.layer_size = []		# Will be poulated in the first following for loop
		self.layer_weights = []		# Second for loop
		self.layer_biases = []

		line_num = 4

		for n in range(0, layers)
			self.layer_size[n] = int(config_array[line_num])
			line_num += 1
		self.num_inputs = layer_size[0]
		self.num_outputs = layer_size[num_layers-1]
		# Start at the first hidden layer and go all the thay throught the output
		for n in range(1, layers):
			temp_weights = []
			for m in range(0, layer_sizes[n])
				for i in range(0, layer_sizes[n-1]):
					temp_weights.append(int(config_array[line_num]))
					line_num += 1
			self.layer_weights.append(temp_weights)
		# Start at the first hidden layer and go all the thay throught the output
		for n in range(1, layers):
			temp_biases = []
			for m in range(layer_sizes[n])
				temp.biases.append(config_array[line_num])
				line_num += 1

