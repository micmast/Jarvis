# This is the "kernel" module/class

import sys
from scheduler import Scheduler

if __name__ == "__main__":
	print "[*] Error: Please use the main entry point!"
	sys.exit(1)

class KernelModules:

	general_type = ''
	flag_use_debug = ''
	handle = ''
	objref = ''

	def __init__(self, objref):
		# Let built the new kernel module
		# Register the handle
		# Save the object to the reference
		# Set some flags: use_debug
		# Set general type: output|input|plugin

		self.objref = objref
		self.flag_use_debug = objref.getType()['debug_use']	
		self.handle = objref.getType()['handle_to_register']
		self.general_type = objref.getType()['type']

	def getDebugFlag(self):
		return self.flag_use_debug

	def getHandle(self):
		return self.handle
	
	def getGeneralType(self):
		return self.general_type
	def getObject(self):
		return self.objref


class ProcessQueue:

	process_type = ''
	process_weight = ''
	running_tasks = []
	def __init__(self, process_type, process_weight):
		self.process_type = process_type
		self.process_weight = process_weight

	def addTask(self, task):
		self.running_tasks.append(task)

	def delTask(self, task):
		# Killing a task or deleting, destroy the object (remove it?)
		pass

class Kernel:

	debug_module = ''
	high_queue = ''
	medium_queue = ''
	low_queue = ''
	default_out_module = ''
	kernel_scheduler = ''

	def __init__(self, parent, debug):
		self.parent = parent
		self.modules = []
		self.debug = debug
		self.pending_input = []

	def setInputPlugins(self, inputplugins):
		# We need to loop through, save them, register the call
		for inputplugin in inputplugins:
			self.modules.append(KernelModules(inputplugin))

	def setOutputPlugins(self, outputplugins):			
		# We need to loop through, save them, register the call
		for outputplugin in outputplugins:
			self.modules.append(KernelModules(outputplugin))


		# Now we set the default out module to jarvis_out 
		# This should be moved to a configuration file, for now hardcoded
		for mod in self.modules:
			if mod.getHandle() == "jarvis_out":
				self.default_out_module = mod


	def sendToDebug(self, msg):
		if self.debug_module == '':
			# We still need to set the debug module
			for module in self.modules:
				if module.getDebugFlag() and module.getGeneralType() == "output": # output only
					# First come first serve
					self.debug_module = module.getObject()
					break
					# break out :)

		if self.debug:
			self.debug_module.sendToDebug(msg)

	def inputPending(self, obj):
		# We have a pending thingy!
		self.pending_input.append(obj)
			
	def initiateInputModules(self):
		# Let us get started on all input devices, how? easy!! just start em
		for module in self.modules:
			if module.getGeneralType() == "input":
				module.getObject().start() # That's it!

	def getInputPending(self):
		return self.pending_input

	def clearInputPending(self):
		self.pending_input = []

	def start(self):
		# The output & input modules are loaded
		# One final check
		inputready = False
		outputready = False
		for kernelmod in self.modules:
			if kernelmod.getGeneralType() == "output":
				outputready = True
			elif kernelmod.getGeneralType() == "input":
				inputready = True

		if (not inputready or not outputready):
			# We cannot continue! Send error and kill
			print "ERROR!!! Either input or output modules missing!! Cannot continue... Quiting"
			sys.exit()

		self.sendToDebug("All prerequisites are met. Continuing setup up the kernel")

		self.high_queue = ProcessQueue('high',10)
		self.medium_queue = ProcessQueue('medium',5)
		self.low_queue = ProcessQueue('low',1)
	
		self.sendToDebug("Queues setup")	
		
		self.kernel_scheduler = Scheduler(self) # the scheduler wants to know who we are, inter connectivity and all :p
		self.kernel_scheduler.start()
