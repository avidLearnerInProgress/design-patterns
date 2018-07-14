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

class Pizza(metaclass = ABCMeta):
	"""
	Abstract base class with __init__ as the abstract method
	Used for inheritance by different types of Pizzas

	@return-values: name of pizza
	"""

	@abstractmethod
	def __init__(self):
		pass

	def get_pizzaname(self):
		return self._name

	#Logging functions
	def make(self):
		print("Preparing: "+ self._name)

	def bake(self):
		print("Baking: "+ self._name)

	def chop(self):
		print("Chopping into pieces: "+ self._name)

	def pack(self):
		print("Packing for delivery: "+ self._name)


class DominoesPizzaFactory:
	"""
	Factory interface class used for selecting type of pizza
	Here we use the ideal concept of factory design pattern by hiding the object creation logic from the client

	@return-values: instance of pizza type selected by user
	"""

	@staticmethod
	def create_pizza(pizza_type):
		pizza = None
		if pizza_type == "margherita":
			pizza = MargheritaPizza()

		elif pizza_type == "peppypaneer":
			pizza = PeppyPaneerPizza()

		elif pizza_type == "cheeseburst":
			pizza = CheeseBurstPizza()

		elif pizza_type == "farmhouse":
			pizza = FarmHousePizza()

		elif pizza_type == "mexican":
			pizza = MexicanPizza()

		return pizza

class MargheritaPizza(Pizza):
	"""
	Class used for customising the type of pizza needed by client / provided by store to client
	Here we use the abstract method __init__ to set the pizza attributes

	@params: class to inherit
	"""

	def __init__(self):
		self._name = "Margherita Pizza"
		self._dough = "Wheat Thin Crust"
		self._size = "Medium"
		self._sauce = "Tomato"
		self._toppings = []
		self._toppings.append("Fresh Mozzarella")
		self._toppings.append("Sliced Tomato")
		self._toppings.append("Sliced Black Olives")

class PeppyPaneerPizza(Pizza):
	"""
	Class used for customising the type of pizza needed by client / provided by store to client
	Here we use the abstract method __init__ to set the pizza attributes

	@params: class to inherit
	"""
	
	def __init__(self):
		self._name = "Peppy Paneer"
		self._dough = "Classic Hand Tossed"
		self._size = "Small"
		self._sauce = "Marinara"
		self._toppings = []
		self._toppings.append("Sliced Paneer")
		self._toppings.append("Sliced Onion")
		self._toppings.append("Sliced Pepperoni")

class CheeseBurstPizza(Pizza):
	"""
	Class used for customising the type of pizza needed by client / provided by store to client
	Here we use the abstract method __init__ to set the pizza attributes

	@params: class to inherit
	"""
	
	def __init__(self):
		self._name = "Cheese Burst"
		self._dough = "Pan Pizza"
		self._size = "Medium"
		self._sauce = "Tomato"
		self._toppings = []
		self._toppings.append("Sliced Corns")
		self._toppings.append("Roasted Red Pepper")
		self._toppings.append("Sliced Broccoli")

class FarmHousePizza(Pizza):
	"""
	Class used for customising the type of pizza needed by client / provided by store to client
	Here we use the abstract method __init__ to set the pizza attributes

	@params: class to inherit
	"""

	def __init__(self):
		self._name = "Farm House"
		self._dough = "Thick Crust"
		self._size = "Large"
		self._sauce = "Marinara"
		self._toppings = []
		self._toppings.append("Sliced Onions")
		self._toppings.append("Sliced Capsicum")
		self._toppings.append("Sliced Garlic")
		self._toppings.append("Fresh Mushrooms")
		self._toppings.append("Jalapeno Peppers")
		self._toppings.append("Fresh Pineapple")

class MexicanPizza(Pizza):
	"""
	Class used for customising the type of pizza needed by client / provided by store to client
	Here we use the abstract method __init__ to set the pizza attributes

	@params: class to inherit
	"""

	def __init__(self):
		self._name = "Mexican"
		self._dough = "Classic Hand Tossed"
		self._size = "Small"
		self._sauce = "Mexican"
		self._toppings = []
		self._toppings.append("Sliced Zucchini")
		self._toppings.append("Caramalised Onions")
		self._toppings.append("Roasted Garlic")


class DominoesPizzaStore:
	"""
	Class which interacts with the client to order his pizza
	Here we initialise the factory class which serves the functionality of creating instances

	@return-values: Complete pizza delivered to client
	"""

	def __init__(self, factory):
		self._factory = factory

	def order_pizza(self, pizza_type= None):
		if pizza_type is None:
			pizza_type = "farmhouse"
		
		pizza = DominoesPizzaFactory.create_pizza(pizza_type)
		pizza.make()
		pizza.bake()
		pizza.chop()
		pizza.pack()
		return pizza


def test_factory():
	"""
	Demonstration of factory pattern
	"""
	
	factory = DominoesPizzaFactory()
	store = DominoesPizzaStore(factory)
	pizza = store.order_pizza()
	print("Ordered: " + pizza.get_pizzaname())

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(Pizza)
	b = inspect.getsource(DominoesPizzaFactory)
	c = inspect.getsource(MargheritaPizza)
	d = inspect.getsource(PeppyPaneerPizza)
	e = inspect.getsource(CheeseBurstPizza)
	f = inspect.getsource(FarmHousePizza)
	g = inspect.getsource(MexicanPizza)
	h = inspect.getsource(DominoesPizzaStore)
	i = inspect.getsource(test_factory)
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g + '\n' + h + '\n' + i

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

	output = output_image("factorymethod_pizza.png")
	#plt.show()
	return output