import serial
import time
import os

class plot:

	def __init__(self):
		self.active_file = ''
		self.data_start_line = 0
		self.datafile_array = []
		self.channel_data = {}
		#self.time_a = 0

	def load(self, filename):
		self.active_file = filename
		file = open(self.active_file)

		line_counter = 0
		data_start = 0
		data_in = []

		## Parses file into a 2d array, [column][row]
		for line in file:

			if(line.count('##### Start Data #####')):
				self.data_start_line = line_counter + 1
			line_counter = line_counter + 1

			## For a tsv file
			self.datafile_array.append(line.split('\t'))
		
		## Datafile header parsing
		self.channel_data['index'] = self.datafile_array[1:][0]
		self.channel_data['name'] = self.datafile_array[1:][1]
		self.channel_data['unit'] = self.datafile_array[1:][2]


		print(self.active_file, "loaded")
		file.close()

	def plot_channel(self, channel_name):
		print('todo')


class stream:

	'''
	Class for streaming telemetry from the engine controller

	Parses a UART stream from the EC, and formats it into a dictionary
	with names to values

	'''

	def __init__(self, port, baudrate):

		## Make a directory for the logfiles if one dosent already exist
		d = os.listdir()
		if not 'Log' in d:
			os.mkdir((os.getcwd()+'/Log'))

		t = time.ctime()
		t = t.replace(':', '_')
		self.log = open(('Log/Stream '+t+'.log'), 'w')
		self.log.write(time.ctime()+': log opened\n')
		self.packet = []
		#self.ser = serial.Serial(port=port, baudrate=baudrate)
		self.template = []
		self.data = {}

	def load_template(self, file):

		''' Loads in telemtry template to an array that can be used by
		other functions. This template us used to parse incoming serial
		packets into meaningful data'''

		try:
			f = open(file)
			self.log.write(time.ctime()+": Loaded "+file+' as template file\n')

			self.template = []
			for line in f:
				self.template.append(line.split('\t'))

		except:
			self.log.write(time.ctime()+": Could not load telemetry template. File requested = "+file)
			print("Could not load telemetry template file. Make sure the file exists")

		## Initialize data dictionary
		for n in range(1, len(self.template)):
			self.data[self.template[n][0]] = 0




