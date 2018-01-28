class net:

	def __init__(self, def_file):
		self.filename = def_file

		file = open(self.filename, 'r')
		self.num_layers = int(file.readline())	
		self.layer_size = []
		for n in range(self.num_layers):
			self.layer_size.append(int(file.readline().rstrip('\n')))
		