import serial
import time
import threading

ser = serial.Serial("COM4", 9600)

def readSerialData():
	while True:
		print(ser.readline())

def doOtherStuff():
	print("Hello! I am other stuff")

threading.Thread(target=readSerialData).start()

doOtherStuff()