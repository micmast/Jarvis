# This is the scheduler, which will basicly loop forever and spawn of threads
# It should keep track of the process started
# Look at how many process should run in parallel
# Fetch things from the kernel queue

import threading

class Scheduler(threading.Thread):

	def __init__(self, parent):
		self.parent = parent # The kernel
		threading.Thread.__init__(self)

	def run(self):
		# We should add our loop here

		# Determining the picking order
		# First initiate all input plugins in a threading mode
		# 	--> They will notify the kernel if they have some input ready or not

		# Loop
		# 	Check for input flag
		#	if input --> handle it first
		#	look at the queues
		#	start max 4 high
		#	start max 2 medium
		# 	start max 1 low
		#	


		self.parent.sendToDebug("Starting all input devices")
		self.parent.initiateInputModules() # Tell the kernel to start all input devices
		self.parent.sendToDebug("Input devices have been started")

		quitflag = False
		
		while not quitflag:
			pass
		
