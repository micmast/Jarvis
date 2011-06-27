# This is the Jarvis out module 
# Jarvis has the ability to speak! Awesome


import sys
import os
import commands

class Plugin:

	def __init__(self, parent):
		# Jarvis wants to have some information in a dictionary
		self.parent = parent
		self.execute("Good morning!")
	def getType(self):
		return {'type':'output',
			'handle_to_register':'jarvis_out',
			'debug_use':False
			}

	def execute(self, content):
		commands.getoutput("spd-say -o openmary \"" + content + "\"")

