# Nick Sterenberg - nsternie@umich.edu
#
## Quadcopter simulation module ##
# This library is created with the intend of simulating
# the dynamics of quadcopter flight.


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
#
# 0 spins clockwise! (Im too lazy to make this an option in the config, live with it)

import math

class Quadcopter(object):

	def __init__(self, config_file):
		
		self.throttle = [0.0,0.0,0.0,0.0] 	# Throttle Percent of all motors
		self.thrust = [0.0,0.0,0.0,0.0]		# Thrust from each of the motors
		self.motor_torques = [0.0,0.0,0.0,0.0]	# Torqu pushback from each motor
		self.rates = [0.0,0.0,0.0] 			# Vehicle rates in radians per second, Rx, Ry, Rz
		self.angles = [0.0,0.0,0.0]			# Angles of each axis from zero
		self.alpha = [0.0,0.0,0.0]			# Angular acceleration of the vehicle
		self.torques = [0.0,0.0,0.0] 		# Torqe on the three axes of the vehice
		self.time = 0						# Time in the sim of the vehicle
		
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

		# Strings that are the equation for thrust in N as a function of throttle T
		self.thrust_curve = self.variables['thrust_curve']
		self.torque_curve = self.variables['torque_curve']
		self.moments = [0.0,0.0,0.0]
		self.moments[0] = self.variables['I_X']
		self.moments[1] = self.variables['I_Y']
		self.moments[2] = self.variables['I_Z']
		self.timestep = self.variables['timestep']

		self.logging = False

	def print_variables(self):
		print self.variables

	def print_time(self):
		print self.time

	def set_throttle(self, throttles):
		self.throttle = throttles

	def step(self):
		self.update_kinematics()
		self.time = self.time + self.timestep
		if self.logging:
			self.print_log()

	def update_kinematics(self):
		# Thrust calc #####################################
		for n in range(0,4):
			T = self.throttle[n]
			self.thrust[n] = eval(self.thrust_curve)
		
		# Torque calc #####################################
		# Length of the [virtual] moment arm of each of these forces, in cardinal directions, not arm directions
		moment_arm = math.sqrt(2) * self.variables['arm_length']
		# Calculate the forces on the quad in each axis (Nm)
		# X
		self.torques[0] = ((self.thrust[0] + self.thrust[3])-(self.thrust[1] + self.thrust[2])) / moment_arm
		# Y 
		self.torques[1] = ((self.thrust[2] + self.thrust[3])-(self.thrust[0] + self.thrust[1])) / moment_arm
		# Z
		# First we have to calculate the torque on the vehicle as a result of each of the motors
		# then, we just sum them to get the torque on the vehicle about the Z axis
		for motor in range(0,4):
			T = self.throttle[motor]
			self.motor_torques[motor] = eval(self.torque_curve)
		# Invert the torques from motors 1 and 3 since they spin counter clockwise
		self.motor_torques[1] *= -1
		1
		self.motor_torques[3] *= -1

		self.torques[2] = sum(self.motor_torques)
		

		# Angular calculations ############################
		for n in range(0,3):
			self.alpha[n] = self.torques[n]/self.moments[n]
			self.rates[n] = self.rates[n] + (self.alpha[n]*self.timestep)
			self.angles[n] = self.angles[n] + (self.rates[n]*self.timestep)

	def print_kinematics(self):
		print "Throttles:",
		print self.throttle
		print "Thrusts:",
		print self.thrust
		print "Motor Torques:",
		print self.motor_torques
		print "Body torques:",
		print self.torques
		print "Alpha",
		print self.alpha
		print "Rates",
		print self.rates

	def print_log(self):
		self.logfile.write(str(self.time)),
		self.logfile.write(','),
		self.logfile.write(str(self.angles[0])),
		self.logfile.write(','),
		self.logfile.write(str(self.angles[1])),
		self.logfile.write(','),
		self.logfile.write(str(self.angles[2])),
		self.logfile.write('\n')

	def log(self, filename):
		self.logfile = file(filename, 'w')
		self.logging = True

	def close_log(self):
		self.logging = False
		self.logfile.close()

	def get_angles(self):
		return self.angles