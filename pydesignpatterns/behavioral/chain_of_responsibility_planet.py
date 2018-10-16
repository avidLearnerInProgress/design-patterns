"""
Author: CHIRAG SHAH
Created On: 16th October 2018
"""

import inspect, sys
import matplotlib.pyplot as plt
from pathlib import Path, PureWindowsPath
from abc import ABCMeta, abstractmethod
from enum import IntEnum

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utility import class_diagram, output_image

class PlanetEnum(IntEnum):
	"""
	Setter class
	"""
	MERCURY = 1
	VENUS = 2
    EARTH = 3
    MARS =4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8


'''
Understanding:
In this pattern, normally each receiver contains reference to another receiver. If one object cannot handle the request then it passes the same to the next receiver and so on. The first object in the chain receives the request and decides either to handle the request or to pass it on to the next object in the chain. The request flows through all objects in the chain one after the other until the request is handled by one of the handlers in the chain or the request reaches the end of the chain without getting processed.
'''
class PlanetHandler(metaclass=ABCMeta):
	"""
	Abstract base class so that subclasses utilise the set_next_handler() and implement handle_request
	"""

    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def handle_request(self, request):
        pass

    def set_next_handler(self, handler):
        self.next_handler = handler


class MercuryHandler(PlanetHandler):
	"""
	Subclass
	"""

    def handle_request(self, request):
        if request is PlanetEnum.MERCURY:
            print("MercuryHandler handles " + request.name)
            print("Mercury is hot.")
        else:
            print("MercuryHandler doesn't handle " + request.name)
            if self.next_handler is not None:
                self.next_handler.handle_request(request)


class VenusHandler(PlanetHandler):
	"""
	Subclass
	"""

    def handle_request(self, request):
        if request is PlanetEnum.VENUS:
            print("VenusHandler handles " + request.name)
            print("Venus is poisonous.")
        else:
            print("VenusHandler doesn't handle " + request.name)
            if self.next_handler is not None:
                self.next_handler.handle_request(request)


class EarthHandler(PlanetHandler):
	"""
	Subclass
	"""

    def handle_request(self, request):
        if request is PlanetEnum.EARTH:
            print("EarthHandler handles " + request.name)
            print("Earth is comfortable.")
        else:
            print("EarthHandler doesn't handle " + request.name)
            if self.next_handler is not None:
                self.next_handler.handle_request(request)


def set_up_chain():
    mercury_handler = MercuryHandler()
    venus_handler = VenusHandler()
    earth_handler = EarthHandler()
    mercury_handler.set_next_handler(venus_handler)
    venus_handler.set_next_handler(earth_handler)

    return mercury_handler


def test_chain_of_responsibility()
    chain = set_up_chain()
    chain.handle_request(PlanetEnum.VENUS)
    chain.handle_request(PlanetEnum.MERCURY)
    chain.handle_request(PlanetEnum.EARTH)
    chain.handle_request(PlanetEnum.JUPITER)


def get_code():
	"""
	@return-values: source code
	"""
	
	a = inspect.getsource(PlanetEnum)
	b = inspect.getsource(PlanetHandler)
	c = inspect.getsource(MercuryHandler)
	d = inspect.getsource(VenusHandler)
	e = inspect.getsource(Earth)
	f = inspect.getsource(set_up_chain)
	g = inspect.getsource(test_chain_of_responsibility)
	return a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g

def get_classdiagram():
	"""
	@return-values: matplotlib object with class diagram
	"""

	diagram = class_diagram("chainofresponsibility.png")
	plt.show()	
	return diagram

def get_outputimage():
	"""
	@return-values: matplotlib object with code output
	"""

	output = output_image("chainofresponsibility_planet.png")
	plt.show()
	return output