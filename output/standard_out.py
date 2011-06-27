# This is the standard out module

# This will be used to print items directly to the screen, ideal for testing purposes and startup procedures.
import sys

class Plugin:

	def __init__(self, parent):
		# Jarvis wants to have some information in a dictionary
		self.parent = parent

	def getType(self):
		return {'type':'output',
			'handle_to_register':'standard_out',
			'debug_use':True
			}

	def execute(self, content):
		print "Doing my thing"

	def sendToDebug(self, msg):
		# Default print out
		sys.stdout.write("[*] Debug: " + msg + "\n")		

	def sendToError(self, msg):
		sys.stdout.write("[*] Error: " + msg + "\n")
