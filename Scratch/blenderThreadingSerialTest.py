import serial
import time
import threading
import bpy

print("-----")

#Setup random cubez
from random import randint

#how many cubes you want to add
count = 8

for c in range(0,count):
	x = c*1.2
	y = 0
	z = 0
	bpy.ops.mesh.primitive_cube_add(location=(x,y,z))



for cube in range (0, len(bpy.data.objects)):
	print(bpy.data.objects[cube])

print("-----")



ser = serial.Serial("COM4", 9600)


def readSerialData():
	while True:
		line = str(ser.readline())
		line = line.replace("b'", "")
		line = line.replace("\\r\\n'", "")
		print(type(line))
		d = line.split(':')
		print(d)
		

		for i in range (0, len(d)-1):
			if(d[i] == "1"):
				bpy.data.objects[i].scale = (1, 10, 1)
			else:
				bpy.data.objects[i].scale = (1, 1, 1)

def doOtherStuff():
	txt = input("INPUT: ")
	if(txt == "0"):
		exit()

threading.Thread(target=readSerialData).start()
#threading.Thread(target=doOtherStuff).start()
