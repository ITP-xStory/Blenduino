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

 
# Operation.


class ToggleSerial(bpy.types.Operator):

	bl_idname = "scene.toggle_serial"  # Access the class by bpy.ops.object.create_serial.
	bl_label = "Toggle Serial"
	bl_description = "Toggle Serial Port"
	bl_options = {'REGISTER', 'UNDO'}
	



	def execute(self, context):
		scn = bpy.context.scene
		print(">>> Toggleing Serial class")
		global q
		if(scn.isSerialConnected == False):
			scn.isSerialConnected = True
			q.put(True)

		else:
			scn.isSerialConnected = False
			q.put(False)

		
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
		row.label("Read Until")
		row.prop(scene, "serial_read_until")

		txt = "Stop Serial"
		icn = "PAUSE"	
		if bpy.context.scene.isSerialConnected == False:
			txt = "Start Serial"
			icn = "PLAY"

		layout.operator(ToggleSerial.bl_idname, icon=icn, text=txt)
		#layout.label(text= txt)

		#layout.operator(CreateSerial.bl_idname, text=txt, icon=icon)
		#layout.operator(StopSerial.bl_idname)


class SerialDataThread(threading.Thread):

	def __init__(self, name='SerialDataThread'):
		print("Starting SDT")
		self._stopevent = threading.Event()
		self._sleepperiod = 1.0

		threading.Thread.__init__(self, name=name)
		print("Thread started")
		#thread = threading.Thread(target=self.run, args=())


	def run(self):
		""" main control loop """
		state = False
		while not self._stopevent.isSet():
			global q
			try:
				state = q.get()
			except:
				print("No new state")
			
			if(state == True):
				print("Reading Serial")
				self._stopevent.wait(0.5)
			elif (state == False):
				print("Not Reading Serial")
				self._stopevent.wait(1)
			
		print("Thread has come to an end.")

	def join(self, timeout=None):
		""" Stop the thread. """
		print("Asking thread to stop")
		self._stopevent.set()
		threading.Thread.join(self, timeout)





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

	bpy.types.Scene.serial_read_until = bpy.props.StringProperty(
		name = "Read Until Character",
		description = "What character delimits a new data block?",
		default = "\n"
	)

	bpy.types.Scene.isSerialConnected = bpy.props.BoolProperty(
		name = "Is Serial Connected",
		description = "Is the serial connected?",
		default = False
	)

	

def removeSerialProperties():
	scn = bpy.types.Scene
	del scn.serial_port
	del scn.serial_baud
	del scn.serial_separator
	del scn.serial_read_until
	del scn.isSerialConnected


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
	
	

#todo: Figure out who thread is seemingly not looping.

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