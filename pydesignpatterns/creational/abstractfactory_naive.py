"""
Author: CHIRAG SHAH
Created On: 23th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class AbstractFactory(metaclass = ABCMeta):
	"""
	Declares an interface for creating abstract products
	"""

	
	@abstractmethod
	def create_product_a(self):
		pass

	@abstractmethod
	def create_product_b(self):
		pass


class ConcreteFactory1(AbstractFactory):
	"""
	Implement operations to create concrete products

	@return-values: instance of concrete product
	"""

	def create_product_a(self):
		return ConcreteProductA1()

	def create_product_b(self):
		return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
	"""
	Implement operations to create concrete products

	@return-values: instance of concrete product
	"""

	def create_product_a(self):
		return ConcreteProductA2()

	def create_product_b(self):
		return ConcreteProductB2()

class AbstractProductA(metaclass = ABCMeta):
	"""
	Declares interface for type of product
	"""

	@abstractmethod
	def interface_a(self):
		pass

class AbstractProductB(metaclass = ABCMeta):
	"""
	Declares interface for type of product
	"""

	@abstractmethod
	def interface_b(self):
		pass

class ConcreteProductA1(AbstractProductA):
	"""
	Define a product object to be created by the corresponding concrete
    factory.
	"""
	
	def interface_a(self):
		return "I am in A1"

class ConcreteProductA2(AbstractProductA):
	"""
	Define a product object to be created by the corresponding concrete
    factory.
	"""
	
	def interface_a(self):
		return "I am in A2"

class ConcreteProductB1(AbstractProductB):
	"""
	Define a product object to be created by the corresponding concrete
    factory.
	"""
	
	def interface_b(self):
		return "I am in B1"

class ConcreteProductB2(AbstractProductB):
	"""
	Define a product object to be created by the corresponding concrete
    factory.
	"""
	
	def interface_b(self):
		return "I am in B2"

def test_factory():
	"""
	Demonstration of abstractfactory pattern
	"""

	for factory in (ConcreteFactory1(), ConcreteFactory2()):
		p_a = factory.create_product_a()
		p_b = factory.create_product_b()
		print(p_a.interface_a())
		print(p_b.interface_b())
	
def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(AbstractFactory)
	b = inspect.getsource(ConcreteFactory1)
	c = inspect.getsource(ConcreteFactory2)
	d = inspect.getsource(AbstractProductA)
	e = inspect.getsource(AbstractProductB)
	f = inspect.getsource(ConcreteProductA1)
	g = inspect.getsource(ConcreteProductA2)
	h = inspect.getsource(ConcreteProductB1)
	i = inspect.getsource(ConcreteProductB2)
	j = inspect.getsource(test_factory)
	
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g + '\n' + h + '\n' + i + '\n' + j

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("abstractfactory.png")
	plt.show()
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("abstractfactory_naive.png")
	plt.show()
	return output