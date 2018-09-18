"""
Author: CHIRAG SHAH
Created On: 18th September 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class Director:
	"""
	This class constructs an object using the Builder Interface
	"""

	def __init__(self):
		self.build = None

	def construct(self, builder):
		self.build = builder
		self.build.build_a()
		self.build.build_b()
		self.build.build_c()

class Builder(metaclass = ABCMeta):
	"""
	This class specifies abstract interface for creating parts of builder object
	"""

	def __init__(self):
		self.product = Product()

	
	@abstractmethod
	def build_a(self):
		pass

	@abstractmethod
	def build_b(self):
		pass

	@abstractmethod
	def build_c(self):
		pass
	
	
class ConcreteBuilder(Builder):
	"""
	Construct and assemble parts of the product by implementing the Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
	"""

	def build_a(self):
		print('Building A..')

	def build_b(self):
		print('Building B..')
	
	def build_c(self):
		print('Building C..')
	
class Product:
	"""
	Represent object under construction
	"""

	pass


def test_builder():
	"""
	Demonstration of builder pattern
	"""

	concrete_builder = ConcreteBuilder()
	director = Director()
	director.construct(concrete_builder)
	product = concrete_builder.product

def get_code():
	"""
	@return-values: source code
	"""
	a = inspect.getsource(Director)
	b = inspect.getsource(Builder)
	c = inspect.getsource(ConcreteBuilder)
	d = inspect.getsource(Product)
	e = inspect.getsource(test_builder)
	
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("builder.png")
	plt.show()
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("builder_naive.png")
	plt.show()
	return output

get_outputimage()
print(get_code())