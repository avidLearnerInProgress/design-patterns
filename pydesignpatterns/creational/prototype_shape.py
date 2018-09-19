"""
Author: CHIRAG SHAH
Created On: 26th July 2018
"""

import inspect, sys, copy
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class Shape(metaclass = ABCMeta):
	"""
	Abstract class
	"""
	def __init__(self):
		self.id = None
		self.type = None

	@abstractmethod
	def draw(self):
		pass

	def get_type(self):
		return self.type

	def get_id(self):
		return self.id

	def set_id(self, id):
		self.id = id

	def clone(self):
		return copy.copy(self)

class Rectangle(Shape):
	"""
	Concrete class extending base class
	"""

	def __init__(self):
		super().__init__()
		self.type = "Rectangle"

	def draw(self):
		print("Drawing Rectangle with draw()..")

class Circle(Shape):
	"""
	Concrete class extending base class
	"""

	def __init__(self):
		super().__init__()
		self.type = "Circle"

	def draw(self):
		print("Drawing Circle with draw()..")

class Square(Shape):
	"""
	Concrete class extending base class
	"""

	def __init__(self):
		super().__init__()
		self.type = "Square"

	def draw(self):
		print("Drawing Square with draw()..")

class ShapeCacheAddr:
	"""
	Maps classes with their id's in dict.
	Returns object clones when needed
	"""
	cache = {}

	@staticmethod
	def get_shape(shape_id):
		shape = ShapeCacheAddr.cache.get(shape_id, None)
		return shape.clone()

	@staticmethod
	def load():
		circle = Circle()
		circle.set_id("1")
		ShapeCacheAddr.cache[circle.get_id()] = circle

		square = Square()
		square.set_id("2")
		ShapeCacheAddr.cache[square.get_id()] = square

		rectangle = Rectangle()
		rectangle.set_id("3")
		ShapeCacheAddr.cache[rectangle.get_id()] = rectangle

def test_prototype():
	"""
	Demonstration of prototype pattern
	"""

	ShapeCacheAddr.load()
	circle = ShapeCacheAddr.get_shape("1")
	print(circle.get_type())

	square = ShapeCacheAddr.get_shape("2")
	print(square.get_type())

	rectangle = ShapeCacheAddr.get_shape("3")
	print(rectangle.get_type())

def get_code():
	"""
	@return-values: source code
	"""
	a = inspect.getsource(Shape)
	b = inspect.getsource(Circle)
	c = inspect.getsource(Square)
	d = inspect.getsource(Rectangle)
	e = inspect.getsource(ShapeCacheAddr)
	f = inspect.getsource(test_prototype)

	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("prototype.png")
	plt.show()
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("prototype_shape.png")
	plt.show()
	return output

test_prototype()
