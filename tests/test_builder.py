"""
Author: CHIRAG SHAH
Created On: 10th October 2018
Modified On: 10th October 2018
"""

import unittest, sys, inspect
from pathlib import Path
from abc import ABCMeta


ROOT_DIR = str(Path(__file__).resolve().parent.parent)
sys.path.append(ROOT_DIR)

from pydesignpatterns.creational import (
	builder_aircraft,
	builder_naive
)

class TestBuilderAircraft(unittest.TestCase):

	def test_classes(self):
		self.assertEqual(inspect.isclass(builder_aircraft.Aircraft), True)
		self.assertEqual(inspect.isclass(builder_aircraft.AircraftBuilder), True)
		self.assertEqual(inspect.isclass(builder_aircraft.Airbus380Builder), True)
		self.assertEqual(inspect.isclass(builder_aircraft.Cessna172Builder), True)
		self.assertEqual(inspect.isclass(builder_aircraft.AircraftDirector), True)

	def test_instances(self):
		self.assertEqual(isinstance(builder_aircraft.AircraftBuilder, ABCMeta), True)
		self.assertEqual(isinstance(builder_aircraft.Airbus380Builder(), builder_aircraft.AircraftBuilder), True)
		self.assertEqual(isinstance(builder_aircraft.Cessna172Builder(), builder_aircraft.AircraftBuilder), True)
		
	def test_builderaircraft(self):
		aircraft_builder = builder_aircraft.Airbus380Builder()
		aircraft_builder.create_aircraft()
		aircraft_director = builder_aircraft.AircraftDirector()
		aircraft = aircraft_director.build(aircraft_builder)
		x = builder_aircraft.get_custom_fields_str(aircraft)
		self.assertEqual(len(x), 105)