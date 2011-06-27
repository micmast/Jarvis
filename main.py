#!/usr/bin/python


# This will startup all main processes

# Loading the kernel
from kernel import Kernel

import os
import sys


class Jarvis:

	debug = True
	mykernel = ''

	def __init__(self):
		self.mykernel = Kernel(self, self.debug)
		self.__loadOutput__()
		self.__loadInput__()
		self.mykernel.setInputPlugins(self.input_modules_object)
		self.mykernel.setOutputPlugins(self.output_modules_object)
		if self.debug:
			self.mykernel.sendToDebug(str(self.output_modules_object))
			self.mykernel.sendToDebug(str(self.input_modules_object))

		# Tell the kernel to get started!
		self.mykernel.start()
	
	def __loadInput__(self):
		self.input_modules_object = []
		files = os.listdir(os.getcwd() + "/input")
		for file_to_load in files:
			if (file_to_load.find("__init") == -1 and file_to_load.find('.pyc') < 0):
				exec "from input import " + file_to_load.replace(".py","") + " as first"
				obj = first.Plugin(self.mykernel)
				if obj.getType()['type'] == "input":
					self.input_modules_object.append(obj)

	def __loadOutput__(self):
		# Time to get stuff loading
		self.output_modules_object = []
		# Fetch the files in the output folder
		files = os.listdir(os.getcwd() + "/output")
		for file_to_load in files:
			if (file_to_load.find("__init") == -1 and file_to_load.find('.pyc')<0):
				# We have a file, load it!	
				exec "from output import " + file_to_load.replace(".py","") + " as first"
				obj = first.Plugin(self.mykernel)
				if obj.getType()['type'] == "output":
					self.output_modules_object.append(obj) # Add the object to our list



# Get this going!!
if __name__ == "__main__":
	jar = Jarvis()
