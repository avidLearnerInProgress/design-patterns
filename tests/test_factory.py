"""
Author: CHIRAG SHAH
Created On: 7th July 2018
Modified On: 14th July 2018
"""

import unittest, sys, inspect
from pathlib import Path
from abc import ABCMeta


ROOT_DIR = str(Path(__file__).resolve().parent.parent)
sys.path.append(ROOT_DIR)

from pydesignpatterns.creational import (
	factorymethod_pizza,
	factorymethod_burger
)

class TestFactoryPizza(unittest.TestCase):

	def test_classes(self):
		self.assertEqual(inspect.isclass(factorymethod_pizza.Pizza), True)
		self.assertEqual(inspect.isclass(factorymethod_pizza.DominoesPizzaFactory), True)
		self.assertEqual(inspect.isclass(factorymethod_pizza.MargheritaPizza), True)
		self.assertEqual(inspect.isclass(factorymethod_pizza.PeppyPaneerPizza), True)
		self.assertEqual(inspect.isclass(factorymethod_pizza.CheeseBurstPizza), True)
		self.assertEqual(inspect.isclass(factorymethod_pizza.FarmHousePizza), True)
		self.assertEqual(inspect.isclass(factorymethod_pizza.MexicanPizza), True)
		self.assertEqual(inspect.isclass(factorymethod_pizza.DominoesPizzaStore), True)

	def test_instances(self):
		self.assertEqual(isinstance(factorymethod_pizza.Pizza, ABCMeta), True)
		self.assertEqual(isinstance(factorymethod_pizza.MargheritaPizza(), factorymethod_pizza.Pizza), True)
		self.assertEqual(isinstance(factorymethod_pizza.PeppyPaneerPizza(), factorymethod_pizza.Pizza), True)
		self.assertEqual(isinstance(factorymethod_pizza.CheeseBurstPizza(), factorymethod_pizza.Pizza), True)
		self.assertEqual(isinstance(factorymethod_pizza.FarmHousePizza(), factorymethod_pizza.Pizza), True)
		self.assertEqual(isinstance(factorymethod_pizza.MexicanPizza(), factorymethod_pizza.Pizza), True)

	def test_orderedpizza(self):
		factory = factorymethod_pizza.DominoesPizzaFactory()
		store = factorymethod_pizza.DominoesPizzaStore(factory)

		pizza = store.order_pizza("cheeseburst")
		self.assertEqual(pizza.get_pizzaname(), "Cheese Burst")

		pizza = store.order_pizza("mexican")
		self.assertEqual(pizza.get_pizzaname(), "Mexican")

		pizza = store.order_pizza()
		self.assertEqual(pizza.get_pizzaname(), "Farm House")


class TestFactoryBurger(unittest.TestCase):

	def test_classes(self):
		self.assertEqual(inspect.isclass(factorymethod_burger.Burger), True)
		self.assertEqual(inspect.isclass(factorymethod_burger.BurgerFactory), True)
		self.assertEqual(inspect.isclass(factorymethod_burger.GrilledMushroomBurger), True)
		self.assertEqual(inspect.isclass(factorymethod_burger.MixVeggieBurger), True)
		self.assertEqual(inspect.isclass(factorymethod_burger.CaramalizedOnionBurger), True)
		self.assertEqual(inspect.isclass(factorymethod_burger.CheeseBurger), True)
		self.assertEqual(inspect.isclass(factorymethod_burger.BurgerStore), True)

	def test_instances(self):
		self.assertEqual(isinstance(factorymethod_burger.Burger, ABCMeta), True)
		self.assertEqual(isinstance(factorymethod_burger.MixVeggieBurger(), factorymethod_burger.Burger), True)
		self.assertEqual(isinstance(factorymethod_burger.GrilledMushroomBurger(), factorymethod_burger.Burger), True)
		self.assertEqual(isinstance(factorymethod_burger.CaramalizedOnionBurger(), factorymethod_burger.Burger), True)
		self.assertEqual(isinstance(factorymethod_burger.CheeseBurger(), factorymethod_burger.Burger), True)

	def test_orderedburger(self):
		factory = factorymethod_burger.BurgerFactory()
		store = factorymethod_burger.BurgerStore(factory)

		burger = store.order_burger("mixveggie")
		self.assertEqual(burger.get_burgername(), "Mix Veggie")

		burger = store.order_burger("grilledmushroom")
		self.assertEqual(burger.get_burgername(), "Grilled Mushroom")

		burger = store.order_burger()
		self.assertEqual(burger.get_burgername(), "Mix Veggie")