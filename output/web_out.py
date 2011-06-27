# This is the standard out module

# This will be used to print items directly to the screen, ideal for testing purposes and startup procedures.

class Plugin:

	def __init__(self, parent):
		# Jarvis wants to have some information in a dictionary
		self.parent = parent

	def getType(self):
		return {'type':'output',
			'handle_to_register':'web_out',
			'debug_use':False
			}


