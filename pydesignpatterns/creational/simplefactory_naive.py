"""
Author: CHIRAG SHAH
Created On: 15th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class AbstractProduct(metaclass = ABCMeta):
	"""
	Abstract base class with __init__ as the abstract method
	Used for inheritance by different types of products

	@return-values: name of product
	"""

	@abstractmethod
	def __init__(self):
		pass

	def get_product(self):
		return self._name
	#do something else..
	
class ProductFactory:
	"""
	Factory interface class used for selecting type of product
	Here we use the ideal concept of factory design pattern by hiding the object creation logic from the client

	@return-values: instance of product type selected by user
	"""
	
	@staticmethod
	def create_product(p_type):
		product = None

		if p_type == "product 1":
			product = Product1()
		elif p_type == "product 2":
			product = Product2()
		
		return product

class Product1(AbstractProduct):
	"""
	Class used for customising the type of product needed by client / provided by store to client
	Here we use the abstract method __init__ to set the product attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(Product1, self).__init__()
		self._name = "I am Product A"
	
	#do something else


class Product2(AbstractProduct):
	"""
	Class used for customising the type of product needed by client / provided by store to client
	Here we use the abstract method __init__ to set the product attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(Product2, self).__init__()
		self._name = "I am Product B"

	#do something else
		
class Client:
	"""
	Class which interacts with the client to order his product
	Here we initialise the factory class which serves the functionality of creating instances

	@return-values: Product delivered to client
	"""

	def __init__(self, factory):
		self._factory = factory

	def order_product(self, p_type= None):
		if p_type is None:
			p_type = "product 2"
		order = ProductFactory.create_product(p_type)
		return order

def test_factory():
	"""
	Demonstration of factory pattern
	"""
	
	factory = ProductFactory()
	store = Client(factory)
	product = store.order_product("product 1")
	print("----" + product.get_product() + "----")

	product = store.order_product()
	print("----" + product.get_product() + "----")

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(AbstractProduct)
	b = inspect.getsource(ProductFactory)
	c = inspect.getsource(Product1)
	d = inspect.getsource(Product2)
	e = inspect.getsource(Client)
	f = inspect.getsource(test_factory)
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("simplefactory.png")
	#plt.show()
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("simplefactory_naive.png")
	#plt.show()
	return output