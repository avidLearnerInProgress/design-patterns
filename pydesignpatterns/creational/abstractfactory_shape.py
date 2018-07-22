"""
Author: CHIRAG SHAH
Created On: 22th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class DrawFactory(metaclass = ABCMeta):
	"""
	Abstract Factory which creates families of related objects
	Used for inheritance by different concrete factories
	"""

	@abstractmethod
	def create_shape(self):
		pass

	@abstractmethod
	def fill_shape(self):
		pass

class CircleFactory(DrawFactory):
	"""
	Concrete factory used to initialise the appropriate class

	@return-values: instance of class
	"""

	def create_shape(self):
		return CircleShape()

	def fill_shape(self):
		return CircleColor()

class TriangleFactory(DrawFactory):
	"""
	Concrete factory used to initialise the appropriate class

	@return-values: instance of class
	"""

	def create_shape(self):
		return TriangleShape()

	def fill_shape(self):
		return TriangleColor()

class CreateShape(metaclass = ABCMeta):
	"""
	Abstract Product which has to be inherited by concrete products
	"""
	@abstractmethod
	def create(self, CreateShape):
		pass

class FillShape(metaclass = ABCMeta):
	"""
	Abstract Product which has to be inherited by concrete products
	"""

	@abstractmethod
	def fill(self, CreateShape):
		pass


class CircleShape(CreateShape):
	"""
	Concrete product which implements abstract method from the abstrct product
	"""

	def create(self):
		print("Creating shape: " + type(self).__name__)

class CircleColor(FillShape):
	"""
	Concrete product which implements abstract method from the abstrct product
	"""

	def fill(self, CreateShape):
		print("Created, now filling shape: " + type(self).__name__)

class TriangleShape(CreateShape):
	"""
	Concrete product which implements abstract method from the abstrct product
	"""

	def create(self):
		print("Creating shape: " + type(self).__name__)

class TriangleColor(FillShape):
	"""
	Concrete product which implements abstract method from the abstrct product
	"""

	def fill(self, CreateShape):
		print("Created, now filling shape: " + type(self).__name__)


class ShapeFactoryStore:
	"""
	Class to interact with client
	"""
	def __init__(self):
		pass

	def make_shape(self):
		for factory in [CircleFactory(), TriangleFactory()]:
			self.factory = factory
			self.createshape = self.factory.create_shape()
			self.fillshape = self.factory.fill_shape()
			self.createshape.create()
			self.fillshape.fill(self.createshape)

def test_factory():
	"""
	Demonstration of abstract factory pattern
	"""
	
	shape = ShapeFactoryStore()
	shape.make_shape()

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(DrawFactory)
	b = inspect.getsource(CircleFactory)
	c = inspect.getsource(TriangleFactory)
	d = inspect.getsource(CreateShape)
	e = inspect.getsource(FillShape)
	f = inspect.getsource(CircleShape)
	g = inspect.getsource(CircleColor)
	h = inspect.getsource(TriangleShape)
	i = inspect.getsource(TriangleColor)
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

	output = output_image("abstractfactory_shape.png")
	plt.show()
	return output

print(get_code())