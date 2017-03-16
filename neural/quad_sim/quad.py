# Motor numbering scheme is
#
#   A
#   | Forward (+X)
#
# 3    0
#  \  / 
#   \/      -> Right (+Y)
#   /\
#  /  \
# 2    1
#
#  Back (-X)
#   |
#   V

import math

class Quadcopter(object):

	def __init__(self, config_file):
		
		self.throttle = [0.0,0.0,0.0,0.0] 	# Throttle Percent of all motors
		self.thrust = [0.0,0.0,0.0]			# Thrust from each of the motors
		self.rates = [0.0,0.0,0.0] 			# Vehicle rates in radians per second, Rx, Ry, Rz
		self.angle = [0.0,0.0,0.0]			# Angles of each axis from zero
		self.moments = [0.0,0.0,0.0] 		# Torqe on the three axes of the vehice
		# Time in the sim of the vehicle
		self.time = 0
		
		# Open the config file
		self.config = open(config_file, 'r')
		self.variables = {}
		# Read all the variables from the config file into a dictionary
		for line in self.config:
			parse = line.split();
			var = parse[0]
			val = parse[1]
			# Load them as a float by default, otherwise load it as a string
			try:
				self.variables[var] = float(val)
			except:
				self.variables[var] = str(val)

		self.thrust_curve = open(variables['thrust.curve'], 'r')
		self.torque_curve = open(variables['torgue.curve'], 'r')


	def print_variables(self):
		print self.variables

	def print_time(self):
		print self.time

	def set_throttle(self, throttles):
		self.throttle = throttles

	def step(self):
		self.calculate_thrusts()
		self.calculate_moments()
		self.calculate_rates()
		self.calculate_angles()
		self.time = self.time + self.variables['timestep']

	def calculate_thrusts(self):


	def calculate_moments(self):
		forces = [0.0,0.0,0.0,0.0]	# Y+, X+, Y-, X-
		forces[0] = 

	def calculate_rates(self):

	def calculate_angles(self):

