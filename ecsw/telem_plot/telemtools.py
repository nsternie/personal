import serial
import time
import os
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pdf

class plot:

	def __init__(self):
		self.active_file = ''			# String for the loaded file
		self.data_start_line = 0		# Line on which the data start after the header
		self.channel_data = {}			# Dict of channel_name:data array
		self.units = {}					# Dict of channel_name:channel_units
		self.num_lines = 0				# Num line in the fileS
		self.timebase_str = 'units'		# Timebase (seconds, millis, micros), poulated from header
		self.timebase = 0.0				# Float of time base in sec
		self.fig_counter = 1			#
		self.in_time = 0
		self.out_time = 0
		#self.time_a = 0

	def load(self, filename):
		self.active_file = filename
		file = open(self.active_file)

		line_counter = 0
		data_in = []
		datafile_array = []

		# Parses file into a 2d array, [row][column]
		for line in file:
			if(line.count('##### Start Data #####')):	# Found the line to mark data start
				self.data_start_line = line_counter + 1	
			line_counter = line_counter + 1				# Keep track of what line were on
														# Useful later, as wel as for data_start
			# Split each line based on a seperator character (Breaks up columns)
			datafile_array.append(line.split('\t')) 	# for a tsv file
		
		self.num_lines = line_counter					# Total length of file in lines (and rows in datafile_array)
		
		

		# Figure out the structure of the header #############################
		channel_num_row = 0
		channel_name_row = 0
		units_row = 0
		timbase_row = 0

		channel_num_options = ['Channel_index', 'Channel Index']
		channel_name_options = ['Channel name', 'Channel_name']
		channel_units_options = ['Units', 'units']
		timebase_options = ['Timebase', 'timebase']

		for n in range(0, self.data_start_line):
			if(datafile_array[n][0] in channel_num_options):
				channel_num_row = n
			if(datafile_array[n][0] in channel_name_options):
				channel_name_row = n
			if(datafile_array[n][0] in channel_units_options):
				units_row = n
			if(datafile_array[n][0] in timebase_options):
				timebase_row = n

		######################################################################

		self.channel_names = datafile_array[channel_name_row][1:]		# Get list of names from header

		# Init channel data arrays
		for channel in self.channel_names:
			self.channel_data[channel] = []

		# Get unit data from the header, and populate data arrays
		n = 1
		for channel in self.channel_names:
			self.units[channel] = datafile_array[units_row][n]
			# n = rol, m = row
			# Go down each column to populate channel data arrays
			for m in range(self.data_start_line, self.num_lines):
				self.channel_data[channel].append(float(datafile_array[m][n]))	
			n = n + 1

		self.units['time'] = datafile_array[timebase_row][1]
		self.timebase = float(datafile_array[timebase_row][2])
		self.channel_data['time'] = []
		for m in range(self.data_start_line, self.num_lines):
			self.channel_data['time'].append(float(datafile_array[m][0]))


		print(self.active_file, "loaded")
		file.close()

	def plot_single_channel(self, channel_name):

		'''
		Plot a single channel, and label axis
		show() must be called to show the plot
		'''

		plt.figure(self.fig_counter)
		self.fig_counter = self.fig_counter + 1
		plt.plot(self.channel_data['time'], self.channel_data[channel_name])
		plt.xlabel('Time, '+self.timebase_str)
		plt.ylabel(self.units[channel_name])
		plt.title(channel_name)

	def show(self):
		plt.show()

	def set_in(self, in_time):
		self.in_time = in_time

	def set_out(self, out_time):
		self.out_time = out_time

	def integrate(self, **kwargs):

		'''
		Returns: Value(float), units(str)
		Arguments: Optionally define stat and end time, otherwise
					uses self.in_time and self.out_time, optional to plot integrated channel
		'''

		start = self.in_time
		end = self.out_time
		for arg, value in kwargs.items():
			if (arg == 'start'):
				start = float(value)
			if (arg == 'end'):
				end = float(value)
			if (arg == 'plot'):
				plot = bool(value)
			if(arg == 'channel'):
				channel = value

		index = 0
		integrate_active = False
		for time in self.channel_data['time']:

			if (not integrate_active and time > start):
				integrate_active = True
				start_index = index

			if(integrate_active and time > end):
				end_index = index

			index = index + 1

		# Just doing left side rectangular for now becasue im lazy
		dt = 0.0
		I = 0.0
		for n in range(start_index, end_index):
			dt = self.channel_data['time'][n+1] - self.channel_data['time'][n]
			I = I + (dt * (self.channel_data[channel][n]))

		I = I * self.timebase
		return I



	def get_channel_data(self, channel):
		''' Returns 2 lists, time, and vhannel value)'''
		return self.channel_data['time'], self.channel_data[channel]

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
		if (self.ser.in_waiting>self.packet_length):
		#	while(self.ser.in_waiting>self.packet_length and not self.ser.read(size=1)==0)

			self.stuffed_packet = []
			for n in range(0, self.packet_length):
				self.stuffed_pcket = self.ser.read(size=self.packet_length)

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
