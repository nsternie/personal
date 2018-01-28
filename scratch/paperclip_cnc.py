import curses
import serial
import time

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

f = 89
b = 90

file = open(str(argv[1]), 'r')
	
bit = []
reps = []
n = 0
for line in file
	device = line[0:2]
	if device == "B+":
		bit[n] = 1
	elif device == "B-"
		bit[n] = 3
	elif device == "F-"
		bit[n] = 4
	elif device == "F+"
		bit[n] = 2
	reps[n] = int(line[2:].rstrip('\n'))
	n = n + 1
ser = serial.Serial('COM8', 115200, timeout=0.000000001)

print(bit)
print(reps)

key = ''
while key != ord('q'):
	key = stdscr.getch()
	stdscr.addch(20,25,key)
	stdscr.refresh()

	out = 0

	if key == curses.KEY_UP:
		out = out | 0b00000001
	if key == curses.KEY_DOWN: 
		out = out | 0b00000100
	if key == curses.KEY_LEFT: 
		out = out | 0b00001000
	if key == curses.KEY_RIGHT: 
		out = out | 0b00000010

	ser.write(chr(out).encode('ascii'))
	print(ser.read(100))

	#time.sleep(10)