"""
Author: CHIRAG SHAH
Created On: 14th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class SingletonMetaclass(type):
	"""
	SingletonMetaclass is a naive implementation of Singleton pattern by using metaclasses
	__call__: this method is called when the instance is called, it allows to return arbitary values
	__init__: doesn't return anything; it's only responsible for initializing the instance after it's been created

	@return-values: instance of class
	"""

	__instance = None

	def __init__(cls, name, bases, namespace):
		super().__init__(name, bases, namespace)
		cls.__instance = None

	def __call__(cls, *args, **kwargs): 
		if cls.__instance is None:
			cls.__instance = super().__call__(*args, **kwargs)
		return cls.__instance
	
class TestMeta(metaclass = SingletonMetaclass):
	"""
	TestMeta uses SingletonMetaclass as its metaclass
	: metaclass is class of class
	: Python - everything is an object
	: `type` is a special keyword which holds the authority to create classes(which are objects in itself)
	: so we have - object is instance of class and class is instance of `type`
	: Every subclass of this class initialises its instance field to None

	@params: class to be used as metaclass
	"""

	pass

class A(TestMeta):
	"""
	@params: class(metaclass) to inherit
	"""
	
	pass

class B(A):
	"""
	@params: class to inherit
	"""

	pass


def get_instance():
	"""
	Test for instances of metaclass
	"""

	print(A())
	print(B())

	if isinstance(A, SingletonMetaclass) == isinstance(B, SingletonMetaclass):
		print("Metaclass Success")
	else:
		print("Error")


def get_code():
	"""
	@return-values: source code
	"""

	a = inspect.getsource(SingletonMetaclass)
	b = inspect.getsource(TestMeta)
	c = inspect.getsource(A)
	d = inspect.getsource(B)
	e = inspect.getsource(get_instance)
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e

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

	output = output_image("singleton_metaclass.png")
	#plt.show()
	return output