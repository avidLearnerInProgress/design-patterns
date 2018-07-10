"""
Author: CHIRAG SHAH
Created On: 7th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class SingletonDecorated(object):
	"""
	SingletonDecorated class is a naive implementation of Singleton pattern by using decorators

	@return-values: instance of class
	"""

	def __init__(self, decorated):
		self._decorated = decorated

	def instance(self):
		try:
			return self._instance
		except AttributeError:
			self._instance = self._decorated()
			return self._instance

	def __call__(self):
		raise TypeError('Singleton should be accessed through instance method.')

	def __instancecheck__(self, ins):
		return isinstance(ins, self._decorated)

@SingletonDecorated
class VeniVediVici:
	"""
	Using singleton decorator to wrap around functionalities of Singleton pattern for this class
	"""

	def __init__(self):
		print("Veni Vedi Vici means `he came, he saw, he conquered`")


#------------------Log------------------#
def wrapperaround():
	#Using this function and nested class for sole purpose of get_code() function results
	#@SingletonDecorated --> Uncomment this line to understand this decorated class
	class VeniVediVici2:
		"""
		Using singleton decorator to wrap around functionalities of Singleton pattern for this class
		"""
		def __init__(self):
			print("Veni Vedi Vici means `he came, he saw, he conquered`")
#-----------------Log Ends------------------#


def test_decorated():
	"""
	Showcases how decorators can be used in Singleton Pattern
	"""

	#u = VeniVediVici() #Error raised --> Uncomment this line to see the error
	v = VeniVediVici.instance()
	w = VeniVediVici.instance()
	print(v is w)

def get_code():
	"""
	@return-values: source code
	"""

	a = inspect.getsource(SingletonDecorated)
	b = inspect.getsource(wrapperaround)
	c = inspect.getsource(test_decorated)
	return a + '\n' + b + '\n' + c

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("singleton.png")
	#plt.show()
	return diagram
	

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("singleton_decorated.png")
	plt.show()
	return output