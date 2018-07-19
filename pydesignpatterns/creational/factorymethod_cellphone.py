"""
Author: CHIRAG SHAH
Created On: 19th July 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class Cellphone(metaclass = ABCMeta):
	"""
	Abstract base class with __init__ as the abstract method
	Used for inheritance by different types of Cellphones

	@return-values: name of cellphone
	"""

	@abstractmethod
	def __init__(self):
		self._cname = None
		self._model = None
		self._android = None
		self._topfeatures = []

	def get_cellphonename(self):
		return self._cname + " " + self._model

	#Logging functions
	def prepare(self):
		print("Wiring...")
		print("Building...")
		print("Assembling...")
		print("Painting...")

	def test(self):
		print("Testing for regulations...")

		
class SamsungGalaxyJ8(Cellphone):
	"""
	Class used for customising the type of cellphone needed by client / provided by store to client
	Here we use the abstract method __init__ to set the cellphone attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(SamsungGalaxyJ8, self).__init__()
		self._cname = "Samsung"
		self._model = "Galaxy J8"
		self._android = "Android 8 Oreo"
		self._topfeatures.append("Snapdragon 450")
		self._topfeatures.append("Octacore 1.6")
		self._topfeatures.append("3500mAh battery")
		self._topfeatures.append("4GB Ram")

class SamsungGalaxyA6(Cellphone):
	"""
	Class used for customising the type of cellphone needed by client / provided by store to client
	Here we use the abstract method __init__ to set the cellphone attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(SamsungGalaxyA6, self).__init__()
		self._cname = "Samsung"
		self._model = "Galaxy A6"
		self._android = "Android 8 Oreo"
		self._topfeatures.append("Exynos 7870")
		self._topfeatures.append("Octacore 1.5")
		self._topfeatures.append("3200mAh battery")
		self._topfeatures.append("3GB Ram")

class OppoF7(Cellphone):
	"""
	Class used for customising the type of cellphone needed by client / provided by store to client
	Here we use the abstract method __init__ to set the cellphone attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(OppoF7, self).__init__()
		self._cname = "Oppo"
		self._model = "F7"
		self._android = "Android 8.1 Oreo"
		self._topfeatures.append("MediaTek MT6771")
		self._topfeatures.append("Octacore 2.0")
		self._topfeatures.append("3400mAh battery")
		self._topfeatures.append("4GB Ram")

class OppoF5(Cellphone):
	"""
	Class used for customising the type of cellphone needed by client / provided by store to client
	Here we use the abstract method __init__ to set the cellphone attributes

	@params: class to inherit
	"""

	def __init__(self):
		super(OppoF5, self).__init__()
		self._cname = "Oppo"
		self._model = "F5"
		self._android = "Android 7 Nougat"
		self._topfeatures.append("MediaTek MT6763")
		self._topfeatures.append("Octacore 2.5")
		self._topfeatures.append("3200mAh battery")
		self._topfeatures.append("3GB Ram")

class CellphoneFactory(metaclass = ABCMeta):
	"""
	Abstract Interface for creating objects
	Here we do not instantiate the object but pass the instantiation to further subclasses

	@return-values: Complete cellphone delivered to client
	"""

	@abstractmethod
	def create_cellphone(self, cell):
		pass

	def order_cellphone(self, c_type):
		cellphone = self.create_cellphone(c_type)
		print("---Serving order for: " + cellphone.get_cellphonename() + " ---")
		cellphone.prepare()
		cellphone.test()
		return cellphone


class SamsungFactory(CellphoneFactory):
	"""
	Subclass of the cellphone factory for instantiating appropriate samsung object
	Here we use the ideal concept of factorymethod design pattern by allowing the subclass to initialise the class

	@return-values: instance of samsung cellphone
	"""
	
	def create_cellphone(self, c_type):
		if c_type == "J8":
			return SamsungGalaxyJ8()
		elif tesla_type == "A6":
			return SamsungGalaxyA6()
		else:
			return None

class OppoFactory(CellphoneFactory):
	"""
	Subclass of the cellphone factory for instantiating appropriate oppo object
	Here we use the ideal concept of factorymethod design pattern by allowing the subclass to initialise the class

	@return-values: instance of oppo cellphone
	"""
	
	def create_cellphone(self, c_type):
		if c_type == "F7":
			return OppoF7()
		elif tesla_type == "F5":
			return OppoF5()
		else:
			return None

def test_factory():
	"""
	Demonstration of factorymethod pattern
	"""
	
	samsungfactory = SamsungFactory()
	oppofactory = OppoFactory()

	c1 = samsungfactory.order_cellphone("J8")
	print("Ordered successfully: " + c1.get_cellphonename() + "\n")

	c2 = oppofactory.order_cellphone("F7")
	print("Ordered successfully: " + c2.get_cellphonename() + "\n")

def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(Cellphone)
	b = inspect.getsource(SamsungGalaxyJ8)
	c = inspect.getsource(SamsungGalaxyA6)
	d = inspect.getsource(OppoF7)
	e = inspect.getsource(OppoF5)
	f = inspect.getsource(SamsungFactory)
	g = inspect.getsource(OppoFactory)
	h = inspect.getsource(test_factory)
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g + '\n' + h

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("factorymethod.png")
	plt.show()
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("factorymethod_cellphone.png")
	plt.show()
	return output