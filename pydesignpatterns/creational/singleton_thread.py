"""
Author: CHIRAG SHAH
Created On: 11th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
import _thread as thread
from pathlib import Path, PureWindowsPath

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class SingletonThread(object):
	"""
	SingletonThread is thread-safe implementation of Singleton Pattern
	"""

	__lockObj = thread.allocate_lock()  #lock object
	__instance = None

	def __new__(cls, *args, **kargs):
		return cls.get_instance(cls)

	def __init__(self):
		pass

	def gettid(self):
		#Printing thread identifier shows that only one thread operates at a given point of time within the class
		
		tid = str(thread.get_ident())
		return tid

	@classmethod
	def get_instance(cls, *args, **kargs):
		"""
		Static method to have a reference to unique instance
		"""

		#Critical section start
		cls.__lockObj.acquire()
		try:
			if cls.__instance is None:
				cls.__instance = object.__new__(cls)

		finally:
			
			
			cls.__lockObj.release()
		#critical section end

		return cls.__instance

def test_thread():
	"""
	Shows how thread-safe singleton works
	"""

	s2 = SingletonThread().get_instance()
	t2 = int(s2.gettid())

	s3 = SingletonThread().get_instance()
	t3 = int(s3.gettid())

	s4 = SingletonThread().get_instance()
	t4 = int(s4.gettid())

	print(s2 is s3 is s4)
	print("tid:" + str(t2))
	if t2 == t3 == t4:
		print(True)

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(SingletonThread)
	b = inspect.getsource(test_thread)
	return a + '\n' + b


def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("singleton.png")
	plt.show()
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("singleton_thread.png")
	plt.show()
	return output

get_outputimage()