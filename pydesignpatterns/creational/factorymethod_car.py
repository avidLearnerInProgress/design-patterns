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

class Car(metaclass = ABCMeta):
	"""
	Abstract base class with __init__ as the abstract method
	Used for inheritance by different types of Cars

	@return-values: name of car
	"""

	@abstractmethod
	def __init__(self):
		self._cname = None
		self._model = None
		self._type = None
		self._topfeatures = []

	def get_carname(self):
		return self._cname + " " + self._model

	#Logging functions
	def blueprint(self):
		print("Creating blueprint...")

	def prepare(self):
		print("Wielding...")
		print("Drilling...")
		print("Wiring...")
		print("Building...")
		print("Assembling...")
		print("Painting...")

	def test(self):
		print("Testing for regulations...")

		
class TeslaX(Car):
	"""
	Class used for customising the type of car needed by client / provided by store to client
	Here we use the abstract method __init__ to set the car attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(TeslaX, self).__init__()
		self._cname = "Tesla"
		self._model = "Model X"
		self._type = "Electric"
		self._topfeatures.append("outrageous acceleration")
		self._topfeatures.append("sleek design")
		self._topfeatures.append("zero emission driving")
		self._topfeatures.append("falcon wings")
		self._topfeatures.append("auto-summon")

class TeslaS(Car):
	"""
	Class used for customising the type of car needed by client / provided by store to client
	Here we use the abstract method __init__ to set the car attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(TeslaS, self).__init__()
		self._cname = "Tesla"
		self._model = "Model S"
		self._type = "Electric"
		self._topfeatures.append("flush door handles")
		self._topfeatures.append("glass cockpit")
		self._topfeatures.append("zero emission driving")
		self._topfeatures.append("active cruise control")
		self._topfeatures.append("outrageous acceleration")

class Tesla3(Car):
	"""
	Class used for customising the type of car needed by client / provided by store to client
	Here we use the abstract method __init__ to set the car attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(Tesla3, self).__init__()
		self._cname = "Tesla"
		self._model = "Model 3"
		self._type = "Electric"
		self._topfeatures.append("super charging")
		self._topfeatures.append("large cargo capacity")
		self._topfeatures.append("HOA access")
		self._topfeatures.append("latch attachments")
		self._topfeatures.append("aerodynamic")

class BMWi3s(Car):
	"""
	Class used for customising the type of car needed by client / provided by store to client
	Here we use the abstract method __init__ to set the car attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(BMWi3s, self).__init__()
		self._cname = "BMW"
		self._model = "i3s"
		self._type = "Electric"
		self._topfeatures.append("strong horsepower")
		self._topfeatures.append("sports suspension")
		self._topfeatures.append("hardcore metal plating")
		self._topfeatures.append("DA systems")
		self._topfeatures.append("all led lighting")
	
class BMW7(Car):
	"""
	Class used for customising the type of car needed by client / provided by store to client
	Here we use the abstract method __init__ to set the car attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(BMW7, self).__init__()
		self._cname = "BMW"
		self._model = "7i"
		self._type = "Non-Electric"
		self._topfeatures.append("hand gestures")
		self._topfeatures.append("auto park")
		self._topfeatures.append("extremely lightweight")
		self._topfeatures.append("efficient auto system planning")
		self._topfeatures.append("side impact beams")


class CarFactory(metaclass = ABCMeta):
	"""
	Abstract Interface for creating objects
	Here we do not instantiate the object but pass the instantiation to further subclasses

	@return-values: Complete car delivered to client
	"""

	@abstractmethod
	def create_car(self, car):
		pass

	def order_car(self, car_type):
		car = self.create_car(car_type)
		print("---Serving order for: " + car.get_carname() + " ---")
		car.blueprint()
		car.prepare()
		car.test()
		return car


class TeslaFactory(CarFactory):
	"""
	Subclass of the car factory for instantiating appropriate tesla object
	Here we use the ideal concept of factorymethod design pattern by allowing the subclass to initialise the class

	@return-values: instance of tesla car
	"""
	
	def create_car(self, tesla_type):
		if tesla_type == "tesla x":
			return TeslaX()
		elif tesla_type == "tesla s":
			return TeslaS()
		elif tesla_type == "tesla 3":
			return Tesla3()
		else:
			return None


class BMWFactory(CarFactory):
	"""
	Subclass of the car factory for instantiating appropriate bmw object
	Here we use the ideal concept of factorymethod design pattern by allowing the subclass to initialise the class

	@return-values: instance of bmw car
	"""
	
	def create_car(self, bmw_type):
		if bmw_type == "bmw i3s":
			return BMWi3s()
		elif bmw_type == "bmw 7":
			return BMW7()
		else:
			return None

def test_factory():
	"""
	Demonstration of factorymethod pattern
	"""
	
	teslafactory = TeslaFactory()
	bmwfactory = BMWFactory()

	car1 = teslafactory.order_car("tesla x")
	print("Ordered successfully: " + car1.get_carname() + "\n")

	car2 = bmwfactory.order_car("bmw i3s")
	print("Ordered successfully: " + car2.get_carname() + "\n")

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(Car)
	b = inspect.getsource(TeslaX)
	c = inspect.getsource(TeslaS)
	d = inspect.getsource(Tesla3)
	e = inspect.getsource(BMWi3s)
	f = inspect.getsource(BMW7)
	g = inspect.getsource(CarFactory)
	h = inspect.getsource(TeslaFactory)
	i = inspect.getsource(BMWFactory)
	j = inspect.getsource(test_factory)
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g + '\n' + h + '\n' + i + '\n' + j

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

	output = output_image("factorymethod_car.png")
	#plt.show()
	return output