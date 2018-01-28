import curses
import serial

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

f = 89
b = 90



ser = serial.Serial('COM8', 115200, timeout=0.000000001)

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