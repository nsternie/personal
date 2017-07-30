import serial
import time
import os
import math

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
		self.stuffed_packet = [] 	
		self.packet = range(0, 65)
		self.packet_length = 0

		try:
			self.ser = serial.Serial(port=port, baudrate=baudrate)
			self.log.write(time.ctime()+": "+port+" opened at "+str(baudrate)+"\n")
		except:
			self.log.write(time.ctime()+": ERROR: "+port+" could not be opened\n")

		## Data from the telemtry template. Dict of Channel:Property
		self.channels = {}

	def read_buffer(self, timeout):
		
		## There is a packet to read
		if (self.ser.in_waiting>0):
			print('ayo')
		else:
			print('buffer is empty')



	def parse_packet(self):

		'''
		Read the most current valid serial packet
		and write it to the channel.value dictionary

		TODO: the real part
		'''

		try:
			assert len(packet) >= (self.channels[len(self.channels)-1].endbit)/8
			assert len(packet) <= ((self.channels[len(self.channels)-1].endbit)/8)+1

			for channel in self.channels:

				start = channel.startbit
				end = channel.endbit
				length = end - start

				start_byte = floor(start/8)
				end_byte = floor(end/8)
				num_bytes = end_byte - start_byte

				b = []
				for n in range(start_byte, end_byte):
					b.append(self.packet[n])



		except:
			self.log.write(time.cstime()+": ERROR: packet incorrect length\n")

		

	def unstuff_data(self):
		print('todo')

	def stuff_data(self):
		print('todo')

	def load_template(self, file):

		''' 
		Loads in telemtry template to an array that can be used by
		other functions. This template us used to parse incoming serial
		packets into meaningful data
		'''

		try:
			f = open(file)
			self.log.write(time.ctime()+": Loaded \""+file+'\" as template file\n')

			temp = []
			for line in f:
				temp.append(line.split('\t'))

		except:
			self.log.write(time.ctime()+": Could not load telemetry template. File requested was  \""+file+"\"")
			print("Could not load telemetry template file. Make sure the file exists")

		## Initialize channel dictionary
		for n in range(1, len(temp)):
			self.channels[temp[n][0]] = channel(temp[n][0])
			self.channels[temp[n][0]].startbit = int(temp[n][1])
			self.channels[temp[n][0]].endbit = int(temp[n][2])
			self.channels[temp[n][0]].signed = bool(temp[n][3])
			self.channels[temp[n][0]].counts_to_volts = float(temp[n][4])
			self.channels[temp[n][0]].volts_to_units = float(temp[n][5])
			self.channels[temp[n][0]].units = temp[n][6]
			
		self.log.write(time.ctime()+": "+str(len(self.channels))+" telemetry channels loaded.")
		self.packet_length = int(int(temp[len(temp)-1][2])/8)+1

	def print_diagnostics(self):
		print('todo')


class channel:

	''' Basic class that defines a telemetry channel datastructure '''

	def __init__(self, name):
		self.name = name
		self.units = ''
		self.startbit = 0
		self.endbit = 0
		self.counts_to_volts = 0.0
		self.volts_to_units = 0.0
		self.signed = False
		self.value_counts = 0
		self.value = 0.0
