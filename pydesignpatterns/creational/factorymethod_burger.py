"""
Author: CHIRAG SHAH
Created On: 14th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class Burger(metaclass = ABCMeta):
	"""
	Abstract base class with __init__ as the abstract method
	Used for inheritance by different types of Burgers

	@return-values: name of burger
	"""

	@abstractmethod
	def __init__(self):
		self._name = None
		self._bun = None
		self._sauce = None
		self._toppings = []

	def get_burgername(self):
		return self._name

	#Logging functions
	def assemble(self):
		print("Assembling all the ingrediets for..." + self._name)

	def prepare(self):
		print("Preparing..." + self._name)
		print("Choosing buns...")
		print("Adding sauce...")
		print("Adding toppings: ")
		print(", ".join(self._toppings))

	def pack(self):
		print("Packing with sauce...")
	
class BurgerFactory:
	"""
	Factory interface class used for selecting type of burger
	Here we use the ideal concept of factory design pattern by hiding the object creation logic from the client

	@return-values: instance of burger type selected by user
	"""
	

	@staticmethod
	def create_burger(burger_type):
		burger = None

		if burger_type == "mixveggie":
			burger = MixVeggieBurger()
		elif burger_type == "grilledmushroom":
			burger = GrilledMushroomBurger()
		elif burger_type == "caramalizedonion":
			burger = CaramalizedOnionBurger()
		elif burger_type == "cheese":
			burger = CheeseBurger()

		return burger

class MixVeggieBurger(Burger):
	"""
	Class used for customising the type of burger needed by client / provided by store to client
	Here we use the abstract method __init__ to set the burger attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(MixVeggieBurger, self).__init__()
		self._name = "Mix Veggie"
		self._bun = "English Muffin"
		self._sauce = "Tomato"
		self._toppings.append("red onions")
		self._toppings.append("fresh spinach")
		self._toppings.append("garlic aioli")
		self._toppings.append("grilled pineapple")

class GrilledMushroomBurger(Burger):
	"""
	Class used for customising the type of burger needed by client / provided by store to client
	Here we use the abstract method __init__ to set the burger attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(GrilledMushroomBurger, self).__init__()
		self._name = "Grilled Mushroom"
		self._bun = "Kaiser Roll"
		self._sauce = "Apple"
		self._toppings.append("sliced cucumber")
		self._toppings.append("fresh lettuce")
		self._toppings.append("grilled pineapple")
		self._toppings.append("fresh gucamole")

class CaramalizedOnionBurger(Burger):
	"""
	Class used for customising the type of burger needed by client / provided by store to client
	Here we use the abstract method __init__ to set the burger attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(CaramalizedOnionBurger, self).__init__()
		self._name = "Caramalize Onion"
		self._bun = "Onion Roll"
		self._sauce = "Strawberry"
		self._toppings.append("sliced cucumber")
		self._toppings.append("fresh lettuce")
		self._toppings.append("garlic aioli")
		self._toppings.append("fresh spinach")

class CheeseBurger(Burger):
	"""
	Class used for customising the type of burger needed by client / provided by store to client
	Here we use the abstract method __init__ to set the burger attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(CheeseBurger, self).__init__()
		self._name = "Cheese"
		self._bun = "Potato Roll"
		self._sauce = "Tomato"
		self._toppings.append("red onions")
		self._toppings.append("feta style cheese")
		self._toppings.append("grilled pineapple")
		self._toppings.append("crunched sprouts")

class BurgerStore:
	"""
	Class which interacts with the client to order his burger
	Here we initialise the factory class which serves the functionality of creating instances

	@return-values: Complete burger delivered to client
	"""

	def __init__(self, factory):
		self._factory = factory

	def order_burger(self, burger_type= None):
		if burger_type is None:
			burger_type = "mixveggie"
		burger = BurgerFactory.create_burger(burger_type)
		burger.assemble()
		burger.prepare()
		burger.pack()
		return burger

def test_factory():
	"""
	Demonstration of factory pattern
	"""
	
	factory = BurgerFactory()
	store = BurgerStore(factory)
	burger = store.order_burger("mixveggie")
	print("Burger Ready: " + burger.get_burgername())

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(Burger)
	b = inspect.getsource(BurgerFactory)
	c = inspect.getsource(MixVeggieBurger)
	d = inspect.getsource(GrilledMushroomBurger)
	e = inspect.getsource(CaramalizedOnionBurger)
	f = inspect.getsource(CheeseBurger)
	g = inspect.getsource(BurgerStore)
	h = inspect.getsource(test_factory)
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g + '\n' + h

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

	output = output_image("factorymethod_burger.png")
	#plt.show()
	return output