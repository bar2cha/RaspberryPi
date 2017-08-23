import time
import serial
import uinput
# Docs http://pyserial.readthedocs.io/en/latest/shortintro.html
# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h#L74

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Tag1 = str('01058AA2F8D4')

device = uinput.Device([
        uinput.KEY_A,
        uinput.KEY_B,
        uinput.KEY_C,
        uinput.KEY_D,
        uinput.KEY_E,
        uinput.KEY_F,
        uinput.KEY_KP1,
        uinput.KEY_KP2,
        uinput.KEY_KP3,
        uinput.KEY_KP4,
        uinput.KEY_KP5,
        uinput.KEY_KP6,
        uinput.KEY_KP7,
        uinput.KEY_KP8,
        uinput.KEY_KP9,
        uinput.KEY_KP0,
	uinput.KEY_LEFTSHIFT,
        uinput.KEY_ENTER,
        ])

#GPIO.setup(23,GPIO.OUT)
#GPIO.setup(24,GPIO.OUT)
#GPIO.output(23,False)
#GPIO.output(24,False)

print "Start reading RFID"
PortRF = serial.Serial('/dev/ttyS0',9600)
print(PortRF.name)
LastID = ""
Pos = 0
while True:
    ID = ""
    final = ""
    read_byte = PortRF.read()
    if read_byte=="\x02":
        for Counter in range(12):
            read_byte=PortRF.read()
            ID = ID + str(read_byte)
            Bin = str(bin(int(read_byte,16))[2:].zfill(4))
            rBin = Bin[::-1]
            rHex = hex(int(rBin,2))
            sHex = str(rHex)[2:]
            #print str(Counter) + " " + str(read_byte) + " " + Bin + " " + rBin + " " + rHex + " " + str(rHex)[2:]
            #print hex(ord(read_byte))
            if (Counter >= 2) and (Counter <= 9) :
                #print str(rHex)[2:]
                final = final + str(rHex)[2:]
                if sHex == "1" :
                    device.emit_click(uinput.KEY_KP1)
                elif sHex == "2" :
                    device.emit_click(uinput.KEY_KP2)
                elif sHex == "3" :
                    device.emit_click(uinput.KEY_KP3)
                elif sHex == "4" :
                    device.emit_click(uinput.KEY_KP4)
                elif sHex == "5" :
                    device.emit_click(uinput.KEY_KP5)
                elif sHex == "6" :
                    device.emit_click(uinput.KEY_KP6)
                elif sHex == "7" :
                    device.emit_click(uinput.KEY_KP7)
                elif sHex == "8" :
                    device.emit_click(uinput.KEY_KP8)
                elif sHex == "9" :
                    device.emit_click(uinput.KEY_KP9)
                elif sHex == "0" :
                    device.emit_click(uinput.KEY_KP0)
                elif sHex == "a" :
                    device.emit_click(uinput.KEY_A)
                elif sHex == "b" :
                    device.emit_click(uinput.KEY_B)
                elif sHex == "c" :
                    device.emit_click(uinput.KEY_C)
                elif sHex == "d" :
                    device.emit_click(uinput.KEY_D)
                elif sHex == "e" :
                    device.emit_click(uinput.KEY_E)
                elif sHex == "f" :
                    device.emit_click(uinput.KEY_F)
	#print "ID: " + ID
	if ID == Tag1:
		print "matched"
		#GPIO.output(23,True)
		#GPIO.output(24,False)
		#time.sleep(5)
		#GPIO.output(23,False)
	else:
		#GPIO.output(23,False)
		print "Access Denied"
		#GPIO.output(24,True)
		#time.sleep(5)
		#GPIO.output(24,False)
        #
	if ID == LastID: print "Same ID"
	LastID = ID
	#print "Final: " + final
	#print
	#device.emit_click(uinput.KEY_A)
	#device.emit_click(uinput.KEY_B)
	#device.emit_click(uinput.KEY_KP2)
	#device.emit_combo([
		#uinput.KEY_LEFTSHIFT,
		#uinput.KEY_C,
		#])
	#device.emit_click(uinput.KEY_C)
	device.emit_click(uinput.KEY_ENTER)
	time.sleep(1)
	PortRF.flushInput()
