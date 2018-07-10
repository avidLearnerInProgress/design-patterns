"""
Author: CHIRAG SHAH
Created On: 8th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class SingletonLazy(object):
	"""
	SingletonLazy Class is naive implementation of Singleton Pattern with help of lazy instantiation
	Lazy instantiation: Object gets created only when its needed
	__init__: doesn't return anything; it's only responsible for initializing the instance after it's been created.

	"""

	__instance = None
	
	def __init__(self): 
		if not SingletonLazy.__instance:
			print("Instance doesn't exist, hence creating it via __init__()")
		else:
			print("Instance already exists:", self.get_instance())

	@classmethod
	def get_instance(cls):
		if not cls.__instance:
			cls.__instance = SingletonLazy()
		return cls.__instance

def test_lazy():
	"""
	Showcases how lazy instantiation works in Singleton Pattern
	"""

	s1 = SingletonLazy() #Here only class is initialised, but object of class isn't created
	print(type(s1))

	print("Object created.", SingletonLazy.get_instance()) #Object is created here

	s2 = SingletonLazy().get_instance() #Object already exists
	s3 = SingletonLazy().get_instance() #Object already exists
	s4 = SingletonLazy().get_instance() #Object already exists

	if id(s3) == id(s4):
		print("SingletonLazy Success")
	else:
		print("Error")

	print("Recheck:")
	recheck = s2 is s3 is s4
	print("s2 == s3 == s4: " +str(recheck))

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(SingletonLazy)
	b = inspect.getsource(test_lazy)
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

	output = output_image("singleton_lazy.png")
	#plt.show()
	return output