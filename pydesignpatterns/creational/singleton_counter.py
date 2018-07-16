"""
Author: CHIRAG SHAH
Created On: 16th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class SingletonCounter(object):
	"""
	SingletonCounter Class is basic example of how to use Singleton pattern in counting objects
	__init__: doesn't return anything; it's only responsible for initializing the instance after it's been created

	@return-values: count value, instance of class
	"""

	__instance = None
	__cnt = 0

	def __init__(self):
		pass
		
	def get_count(self):
		self.__cnt += 1
		return self.__cnt

	def get_instance():
		if SingletonCounter.__instance == None:
			SingletonCounter.__instance = SingletonCounter()
		else:
			pass
		return SingletonCounter.__instance

def test_instance():
	"""
	Check for count++
	"""

	print("Instance id   | Count")

	s1 = SingletonCounter.get_instance()
	print(str(id(s1)) + " : " + str(s1.get_count()))

	s2 = SingletonCounter.get_instance()
	print(str(id(s2)) + " : " + str(s2.get_count()))

	s3 = SingletonCounter.get_instance()
	print(str(id(s2)) + " : " + str(s3.get_count()))


def get_code():
	"""
	@return-values: source code
	"""

	a = inspect.getsource(SingletonCounter)
	b = inspect.getsource(test_instance)
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

	output = output_image("singleton_counter.png")
	#plt.show()
	return output