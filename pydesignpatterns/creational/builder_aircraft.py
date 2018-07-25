"""
Author: CHIRAG SHAH
Created On: 26th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class Aircraft:
	"""
	Base initialisation object
	"""

	mark = ''
	model = ''
	max_speed = 0
	takeoff_speed = 0
	passengers_count = 0
	fuel_capacity = 0

class AircraftBuilder(metaclass = ABCMeta):
	"""
	Abstract builder for creating aircraft
	"""

	def __init__(self):
		self.aircraft = None

	def create_aircraft(self):
		self.aircraft = Aircraft()

	@abstractmethod
	def build_mark(self):
		pass

	@abstractmethod
	def build_model(self):
		pass

	@abstractmethod
	def build_max_speed(self):
		pass
	
	@abstractmethod
	def build_takeoff_speed(self):
		pass
	
	@abstractmethod
	def build_passengers_count(self):
		pass

	@abstractmethod
	def build_fuel_capacity(self):
		pass
	
class Airbus380Builder(AircraftBuilder):
	"""
	Concrete aircraft builder used for constructing the attributes of aircraft by inheriting the abstract builder
	"""

	def build_fuel_capacity(self):
		self.aircraft.fuel_capacity = 32000

	def build_takeoff_speed(self):
		self.aircraft.takeoff_speed = 277.8
	
	def build_max_speed(self):
		self.aircraft.max_speed = 1020
	
	def build_passengers_count(self):
		self.aircraft.passengers_count = 538
	
	def build_mark(self):
		self.aircraft.mark = 'Airbus'
	
	def build_model(self):
		self.aircraft.model = 'A-380'

class Cessna172Builder(AircraftBuilder):
	"""
	Concrete aircraft builder used for constructing the attributes of aircraft by inheriting the abstract builder
	"""

	def build_fuel_capacity(self):
		self.aircraft.fuel_capacity = 249.837
	
	def build_takeoff_speed(self):
		self.aircraft.takeoff_speed = 277.8
	
	def build_max_speed(self):
		self.aircraft.max_speed = 302
	
	def build_passengers_count(self):
		self.aircraft.passengers_count = 1
	
	def build_mark(self):
		self.aircraft.mark = 'Cessna'
	
	def build_model(self):
		self.aircraft.model = '172'

class AircraftDirector:
	"""
	Constructs aircraft object using builder interface
	"""

	def __init__(self):
		self._builder = None

	def build(self, aircraft_builder):
		self._builder = aircraft_builder
		self._builder.build_fuel_capacity()
		self._builder.build_takeoff_speed()
		self._builder.build_max_speed()
		self._builder.build_passengers_count()
		self._builder.build_mark()
		self._builder.build_model()
		return self._builder.aircraft

def test_builder():
	"""
	Demonstration of builder pattern
	"""

	def get_custom_fields_str(obj):
		return '\n'.join('{}: {}'.format(field, obj.__getattribute__(field)) for field in dir(obj) if not field.startswith('__'))

	aircraft_builder = Airbus380Builder()
	aircraft_builder.create_aircraft()
	aircraft_director = AircraftDirector()
	aircraft = aircraft_director.build(aircraft_builder)
	print(get_custom_fields_str(aircraft))

def get_code():
	"""
	@return-values: source code
	"""
	a = inspect.getsource(Aircraft)
	b = inspect.getsource(AircraftBuilder)
	c = inspect.getsource(Airbus380Builder)
	d = inspect.getsource(Cessna172Builder)
	e = inspect.getsource(AircraftDirector)
	f = inspect.getsource(test_builder)
	
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f

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

	output = output_image("builder_aircraft.png")
	plt.show()
	return output