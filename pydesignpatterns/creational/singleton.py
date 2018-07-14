"""
Author: CHIRAG SHAH
Created On: 7th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class Singleton(object):
	"""
	Singleton Class is a naive implementation of Singleton pattern by overriding __new__ method
	__new__: First step of instance creation. It's called first, and is responsible for returning a new instance of your class

	@return-values: instance of class, hash value generated for class
	"""

	__instance = None
	__hsh = None
	def __new__(cls, *args, **kwargs): 
		if not cls.__instance:
			cls.__instance = object.__new__(cls, *args, **kwargs)
			cls.__hsh = cls.__instance.__hash__()
		return cls.__instance, cls.__hsh


def get_instance():
	"""
	Check if single instance is created for same class by using multiple objects
	"""

	s1, hsh1 = Singleton()
	s2, hsh2 = Singleton()

	print("Hash of instance 1: "+ str(hsh1))
	print("Hash of instance 2: "+ str(hsh2))

	if id(s1) == id(s2):
		print("Singleton Success")
	else:
		print("Error")

def get_code():
	"""
	@return-values: source code
	"""

	a = inspect.getsource(Singleton)
	b = inspect.getsource(get_instance)
	return a + '\n' + b

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

	output = output_image("singleton.png")
	#plt.show()
	return output