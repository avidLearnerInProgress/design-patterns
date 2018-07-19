"""
Author: CHIRAG SHAH
Created On: 17th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class AbstractCreator(metaclass = ABCMeta):
	"""
	Abstract base class with __init__ as the abstract method
	Used for inheritance by different types of ConcreteCreators

	@return-values: name of creator
	"""

	
	def __init__(self):
		self.product = self.factory_method()

	@abstractmethod
	def factory_method(self):
		pass

	#Logging functions
	def log(self):
		#self.product.interface()
		pass
		
class ConcreteCreatorA(AbstractCreator):
	"""
	Class used for customising the type of creator needed by client / provided by store to client
	Here we use the abstract method __init__ to set the concretecreator attributes

	@params: class to inherit
	"""

	def factory_method(self):
		return ConcreteProductA()

class ConcreteCreatorB(AbstractCreator):
	"""
	Class used for customising the type of creator needed by client / provided by store to client
	Here we use the abstract method __init__ to set the concretecreator attributes

	@params: class to inherit
	"""

	def factory_method(self):
		return ConcreteProductB()

class AbstractProduct(metaclass = ABCMeta):
	"""
	Abstract Interface for creating objects
	Here we do not instantiate the object but pass the instantiation to further subclasses

	@return-values: Complete product delivered to client
	"""

	@abstractmethod
	def interface(self):
		pass
	
class ConcreteProductA(AbstractProduct):
	"""
	Subclass of the product factory for instantiating appropriate concretecreator object
	Here we use the ideal concept of factorymethod design pattern by allowing the subclass to initialise the class

	@return-values: instance of concretecreator
	"""
	
	def interface(self):
		return "I am in A"

class ConcreteProductB(AbstractProduct):
	"""
	Subclass of the product factory for instantiating appropriate concretecreator object
	Here we use the ideal concept of factorymethod design pattern by allowing the subclass to initialise the class

	@return-values: instance of concretecreator
	"""
	
	def interface(self):
		return "I am in B"
		

def test_factory():
	"""
	Demonstration of factorymethod pattern
	"""
	
	concretecreator = ConcreteCreatorA()
	concretecreator.product.interface()
	#concretecreator.log()

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(AbstractCreator)
	b = inspect.getsource(ConcreteCreatorA)
	c = inspect.getsource(ConcreteCreatorB)
	d = inspect.getsource(AbstractProduct)
	e = inspect.getsource(ConcreteProductA)
	f = inspect.getsource(ConcreteProductB)
	g = inspect.getsource(test_factory)
	
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("factorymethod.png")
	#plt.show()
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("factorymethod_naive.png")
	#plt.show()
	return output