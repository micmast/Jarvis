# This is the standard in module

# This will be used to print items directly to the screen, ideal for testing purposes and startup procedures.
import sys
import threading
import time
import os

class Plugin(threading.Thread):

	def __init__(self, parent):
		# Jarvis wants to have some information in a dictionary
		self.parent = parent

		threading.Thread.__init__(self)

	def getType(self):
		return {'type':'input',
			'handle_to_register':'standard_in',
			'debug_use':True
			}

	def execute(self, content):
		print "Doing my thing"


	def run(self):
		# I'm an input plugin so I have to start listening myself...
		

		# to fake the threading I sleep a while
		while (1):
			
			time.sleep(1)  # I wait a second, just to make sure I don't overdo it!
			
			# now I read a file, if I have something new, I add it to my list and poke the kernel
			self.parent.sendToDebug("Input plugin Standard_in: Current path: " + os.getcwd())

			filehp = open(os.getcwd() + "/commands.txt","r")

			lines = filehp.readlines()
			added = False			
			for line in lines:
				if line != "":
					self.pending_commands.append(line)
					added = True # I will have to alert the kernel to check up on me.
			
			# close the file and clear it!
			filehp.close()
			filehp = open(os.getcwd() + "/commands.txt","w") # basicly writing a new line
			filehp.write()
			filehp.close()

			self.parent.inputPending(self)
