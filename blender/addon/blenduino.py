import serial
import time
import threading
from multiprocessing import Queue
#from multiprocessing import Process	#Better than threading - but causes trouble with blender!
import bpy


q = Queue()

# Meta information.
bl_info = {
	"name": "Serial Communication",
	"author": "James",
	"version": (1, 0),
	"blender": (2, 79),
	"location": "Tools > Serial",
	"description": "Add Serial",
	"warning": "",
	"support": "TESTING",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Tool"
}



class SerialDataThread(threading.Thread):

	def __init__(self, name='SerialDataThread'):
		print("Starting SDT")
		self._stopevent = threading.Event()
		self._sleepperiod = 1.0

		#= serial.Serial(bpy.context.scene.serial_port, bpy.context.scene.serial_baud)

		try:
			self.ser = serial.Serial( # set parameters, in fact use your own :-)
				port= bpy.context.scene.serial_port,
				baudrate= bpy.context.scene.serial_baud,
				timeout=1 	#Timeout after 1 second. Prevents freezing
				# bytesize=serial.SEVENBITS,
				# parity=serial.PARITY_EVEN,
				# stopbits=serial.STOPBITS_ONE
			)
			self.ser.isOpen() # try to open port, if possible print message and proceed with 'while True:'
			print ("port is opened!")

		except IOError: # if port is already opened, close it and open it again and print message
			self.ser.close()
			self.ser.open()
			print ("port was already open, was closed and opened again!")


		threading.Thread.__init__(self, name=name)
		print("Thread started")
		#thread = threading.Thread(target=self.run, args=())


	def run(self):
		""" main control loop """
		
		while not self._stopevent.isSet():

			if(bpy.types.Scene.isSerialConnected == True):
				#########################
				### Read Serial Here ###
				#########################
				
				#If serial closed, open
				if(self.ser.isOpen() == False):
					print("Opening Serial")
					self.ser.open()

				line = str(self.ser.readline())
				line = line.replace("b'", "")		# Remove byte flag from incoming string
				line = line.replace("\\r\\n'", "")	# Remove end line character
				line = line.rstrip()
				data = line.split(bpy.context.scene.serial_separator)
				#print (data)
				try:
					data.remove("")	#Remove empty data
				except:
					print("No data to remove")	

				# Only print data if it's the expected length
				if(len(data) == bpy.context.scene.serial_expected_length):
					c = 0
					for element in data:
						bpy.context.scene.serial_data[c] = int(element)
						print(element, end="")
						print(" : ", end="")
						print(bpy.context.scene.serial_data[c], end="")
						print(" || ", end="")
						c = c+1
					print()

				#print("Reading Serial")
				#self._stopevent.wait(0.5)

			else:

				#If serial open, closed
				if(self.ser.isOpen() == True):
					print("Closing Serial")
					self.ser.close()

				print("Waiting to activate Serial")
				self._stopevent.wait(1)
			
		print("Thread has come to an end.")

	def join(self, timeout=None):
		""" Stop the thread. """
		print("Asking thread to stop")
		self._stopevent.set()
		threading.Thread.join(self, timeout)


class ToggleSerial(bpy.types.Operator):

	bl_idname = "scene.toggle_serial"  # Access the class by bpy.ops.object.create_serial.
	bl_label = "Toggle Serial"
	bl_description = "Toggle Serial Port"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		scn = bpy.types.Scene
		print(">>> Toggling Serial class")
		
		if(scn.isSerialConnected == False):
			scn.isSerialConnected = True
			
		else:
			scn.isSerialConnected = False
		
		print(scn.isSerialConnected)
		return {'FINISHED'}



# Menu setting.
class CreateSerialPanel(bpy.types.Panel):
	bl_label = "CREATE Serial"
	bl_idname = "create_serial" # class ID.
	bl_space_type = "VIEW_3D"	# Menu accessible from 3D viewport
	bl_region_type = "TOOLS" 	# Menu lives in the left tool shelf.
	bl_category = "Serial" 		# Create new tab for Serial!
	bl_context = (("objectmode"))
	 
	# Menu and input:
	def draw(self, context):
		obj = context.object
		scene = context.scene

		layout = self.layout

		row = layout.row()
		row.label("Serial Port")
		row.prop(scene, "serial_port") # Input button for bpy.types.Scene.float_input.

		row = layout.row()
		row.label("Baud Rate")
		row.prop(scene, "serial_baud")

		row = layout.row()
		row.label("Separator")
		row.prop(scene, "serial_separator")

		row = layout.row()
		row.label("Expected Length")
		row.prop(scene, "serial_expected_length")

		# row = layout.row()
		# row.label("Read Until")
		# row.prop(scene, "serial_read_until")

		txt = "Stop Serial"
		icn = "PAUSE"	
		if bpy.context.scene.isSerialConnected == False:
			txt = "Start Serial"
			icn = "PLAY"

		layout.operator(ToggleSerial.bl_idname, icon=icn, text=txt)
		#layout.operator(ResetSerial.bl_idname, icon="LOOP_BACK", text="Reset Serial")

		c = 0
		for i in bpy.context.scene.serial_data:
			row = layout.row()
			row.label("Serial Data " + str(c) + ": " + str(bpy.context.scene.serial_data[c]))	
			c = c+1
			
			#row.prop(scene, "serial_data")


		#layout.operator(CreateSerial.bl_idname, text=txt, icon=icon)
		#layout.operator(StopSerial.bl_idname)

# Set up scene-wide properties
def initSerialProperties(scn):
	bpy.types.Scene.serial_port = bpy.props.StringProperty(
		name = "Serial Port",
		description = "Set test float",
		default = "COM4"
	)

	bpy.types.Scene.serial_baud =  bpy.props.IntProperty(
		name = "Baud Rate",
		description = "Set Baud Rate",
		default = 9600
	)

	bpy.types.Scene.serial_separator = bpy.props.StringProperty(
		name = "Data Separator",
		description = "What character separates your incoming data?",
		default = ","
	)

	''' Not using readuntil at the moment because using readlines() to read serial
	bpy.types.Scene.serial_read_until = bpy.props.StringProperty(
		name = "Read Until Character",
		description = "What character delimits a new data block?",
		default = "\n"
	)
	'''

	bpy.types.Scene.isSerialConnected = bpy.props.BoolProperty(
		name = "Is Serial Connected",
		description = "Is the serial connected?",
		default = False
	)

	bpy.types.Scene.serial_expected_length = bpy.props.IntProperty(
		name = "Expected Data Length",
		description = "Expected length of incoming data",
		default=9
	)

	bpy.types.Scene.serial_data = bpy.props.IntVectorProperty(
		name = "Serial Data Array",
		description = "What character separates your incoming data?",
		default=(0,0,0,0,0,0,0,0),
		size = 8
	)



def removeSerialProperties():
	scn = bpy.context.scene
	del scn.serial_port
	del scn.serial_baud
	del scn.serial_separator
	#del scn.serial_read_until
	del scn.isSerialConnected
	del scn.serial_expected_length


def register():
	initSerialProperties(bpy.context.scene)
	bpy.utils.register_module(__name__)
	# bpy.types.Scene~　＝　To show the input in the left tool shelf, store "bpy.props.~".
	#   In draw() in the subclass of Panel, access the input value by "context.scene".
	#   In execute() in the class, access the input value by "context.scene.[var]".
	
	### THREADING ###

	# Kill any other Serial threads
	for thread in threading.enumerate():
		if(thread.name == "SerialDataThread"):
			print("Existing Thread Found. Exiting.")
			thread.join()

	serialThread = SerialDataThread()
	serialThread.start()

	print("Blenduino was activated.")

def unregister():
	#Remove addon data
	removeSerialProperties()
	bpy.utils.unregister_module(__name__)
	print("This add-on was deactivated.")

	serialThread.join()


#For local testing
if __name__ == "__main__":
	register()
	
#Todo: Update menu window on serial update.

#todo: [Big picture] implement more reliable threading (use queues?)

	#     def run(self):
	#     	while(True):
				# if(self.stop == True):
				# 	return

				# if(bpy.types.Scene.isSerialConnected == True):
				# 	print ("reading")
				# 	time.sleep(.5)
				# else:
				# 	print("not reading")
				# 	time.sleep(1)



# # Set these values in window?
# def add_driver(
#         source, target, prop, dataPath,
#         index = -1, negative = False, func = ''
#     ):
#     ''' Add driver to source prop (at index), driven by target dataPath '''

#     if index != -1:
#         d = source.driver_add( prop, index ).driver
#     else:
#         d = source.driver_add( prop ).driver

#     v = d.variables.new()
#     v.name                 = prop
#     v.targets[0].id        = target
#     v.targets[0].data_path = dataPath

#     d.expression = func + "(" + v.name + ")" if func else v.name
#     d.expression = d.expression if not negative else "-1 * " + d.expression




# class ResetSerial(bpy.types.Operator):

# 	bl_idname = "scene.reset_serial"  # Access the class by bpy.ops.object.create_serial.
# 	bl_label = "Reset Serial"
# 	bl_description = "Reset Serial Port"
# 	bl_options = {'REGISTER', 'UNDO'}

# 	def execute(self,context):

# 		for thread in threading.enumerate():
# 			if(thread.name == "SerialDataThread"):
# 				print("Existing Thread Found. Exiting.")
# 				thread.join()

# 		serialThread = SerialDataThread()
# 		serialThread.start()
# 		return {'FINISHED'}
