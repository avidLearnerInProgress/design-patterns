"""
Author: CHIRAG SHAH
Created On: 21st September 2018
"""

import inspect, sys, copy
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image


class Prototype:

    """ Object, that can be cloned.
    This is just a base class, so the clone() method
    is not implemented. But all subclasses have to
    override it.
    """

    _type  = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

class Type1(Prototype):

    """ Concrete prototype.
    Implementation of Prototype. Important part is the
    clone() method.
    """

    def __init__(self, number):
        self._type = "Type1"
        self._value = number

    def clone(self):
        return copy.copy(self)

class Type2(Prototype):
    """ Concrete prototype. """

    def __init__(self, number):
        self._type = "Type2"
        self._value = number

    def clone(self):
        return copy.copy(self)

class ObjectFactory:

    """ Manages prototypes.
    Static factory, that encapsulates prototype
    initialization and then allows instatiation
    of the classes from these prototypes.
    """

    __type1Value1 = None
    __type2Value1 = None

    @staticmethod
    def initialize():
        ObjectFactory.__type1Value1 = Type1(1)
        ObjectFactory.__type2Value1 = Type2(1)

    @staticmethod
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()


def test_prototype():
    ObjectFactory.initialize()

    instance = ObjectFactory.getType1Value1()
    print("%s: %s" % (instance.getType(), instance.getValue()))

    instance = ObjectFactory.getType2Value1()
    print("%s: %s" % (instance.getType(), instance.getValue()))

def get_code():
	"""
	@return-values: source code
	"""
	a = inspect.getsource(Prototype)
	b = inspect.getsource(Type1)
	c = inspect.getsource(Type2)
	d = inspect.getsource(ObjectFactory)
	e = inspect.getsource(test_prototype)

	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e

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

	output = output_image("prototype_naive.png")
	plt.show()
	return output

test_prototype()