quad.py provides a simple quadcopter simulation class. The class is initialized
with a string pointing to a confguration file. Once an instance of the class is
initialized, the main interfaces are set_throttle() and step(). set_throttles 
takes a 4 item list as an argument, and sets the throtttle values of the 4 motors
on the quad. step() advances the simultion by one timestep, as defines in the config.
log() take a file name as input, and will begin to log data from the sim once per
timestep close_log() will terminate logging and close the logfile.