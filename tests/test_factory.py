"""
Author: CHIRAG SHAH
Created On: 15th July 2018
Modified On: 19th July 2018
"""

import unittest, sys, inspect
from pathlib import Path
from abc import ABCMeta


ROOT_DIR = str(Path(__file__).resolve().parent.parent)
sys.path.append(ROOT_DIR)

from pydesignpatterns.creational import (
	simplefactory_naive,
	simplefactory_pizza,
	simplefactory_burger,
	factorymethod_naive,
	factorymethod_car
)

class TestFactory(unittest.TestCase):

	def test_classes(self):
		self.assertEqual(inspect.isclass(simplefactory_naive.AbstractProduct), True)
		self.assertEqual(inspect.isclass(simplefactory_naive.ProductFactory), True)
		self.assertEqual(inspect.isclass(simplefactory_naive.Product1), True)
		self.assertEqual(inspect.isclass(simplefactory_naive.Product2), True)
		self.assertEqual(inspect.isclass(simplefactory_naive.Client), True)

	def test_instances(self):
		self.assertEqual(isinstance(simplefactory_naive.AbstractProduct, ABCMeta), True)
		self.assertEqual(isinstance(simplefactory_naive.Product1(), simplefactory_naive.AbstractProduct), True)
		self.assertEqual(isinstance(simplefactory_naive.Product2(), simplefactory_naive.AbstractProduct), True)
		
	def test_orderedproduct(self):
		factory = simplefactory_naive.ProductFactory()
		store = simplefactory_naive.Client(factory)

		product = store.order_product("product 1")
		self.assertEqual(product.get_product(), "I am Product A")

		product = store.order_product("product 2")
		self.assertEqual(product.get_product(), "I am Product B")

		product = store.order_product()
		self.assertEqual(product.get_product(), "I am Product B")

class TestFactoryPizza(unittest.TestCase):

	def test_classes(self):
		self.assertEqual(inspect.isclass(simplefactory_pizza.Pizza), True)
		self.assertEqual(inspect.isclass(simplefactory_pizza.DominoesPizzaFactory), True)
		self.assertEqual(inspect.isclass(simplefactory_pizza.MargheritaPizza), True)
		self.assertEqual(inspect.isclass(simplefactory_pizza.PeppyPaneerPizza), True)
		self.assertEqual(inspect.isclass(simplefactory_pizza.CheeseBurstPizza), True)
		self.assertEqual(inspect.isclass(simplefactory_pizza.FarmHousePizza), True)
		self.assertEqual(inspect.isclass(simplefactory_pizza.MexicanPizza), True)
		self.assertEqual(inspect.isclass(simplefactory_pizza.DominoesPizzaStore), True)

	def test_instances(self):
		self.assertEqual(isinstance(simplefactory_pizza.Pizza, ABCMeta), True)
		self.assertEqual(isinstance(simplefactory_pizza.MargheritaPizza(), simplefactory_pizza.Pizza), True)
		self.assertEqual(isinstance(simplefactory_pizza.PeppyPaneerPizza(), simplefactory_pizza.Pizza), True)
		self.assertEqual(isinstance(simplefactory_pizza.CheeseBurstPizza(), simplefactory_pizza.Pizza), True)
		self.assertEqual(isinstance(simplefactory_pizza.FarmHousePizza(), simplefactory_pizza.Pizza), True)
		self.assertEqual(isinstance(simplefactory_pizza.MexicanPizza(), simplefactory_pizza.Pizza), True)

	def test_orderedpizza(self):
		factory = simplefactory_pizza.DominoesPizzaFactory()
		store = simplefactory_pizza.DominoesPizzaStore(factory)

		pizza = store.order_pizza("cheeseburst")
		self.assertEqual(pizza.get_pizzaname(), "Cheese Burst")

		pizza = store.order_pizza("mexican")
		self.assertEqual(pizza.get_pizzaname(), "Mexican")

		pizza = store.order_pizza()
		self.assertEqual(pizza.get_pizzaname(), "Farm House")


class TestFactoryBurger(unittest.TestCase):

	def test_classes(self):
		self.assertEqual(inspect.isclass(simplefactory_burger.Burger), True)
		self.assertEqual(inspect.isclass(simplefactory_burger.BurgerFactory), True)
		self.assertEqual(inspect.isclass(simplefactory_burger.GrilledMushroomBurger), True)
		self.assertEqual(inspect.isclass(simplefactory_burger.MixVeggieBurger), True)
		self.assertEqual(inspect.isclass(simplefactory_burger.CaramalizedOnionBurger), True)
		self.assertEqual(inspect.isclass(simplefactory_burger.CheeseBurger), True)
		self.assertEqual(inspect.isclass(simplefactory_burger.BurgerStore), True)

	def test_instances(self):
		self.assertEqual(isinstance(simplefactory_burger.Burger, ABCMeta), True)
		self.assertEqual(isinstance(simplefactory_burger.MixVeggieBurger(), simplefactory_burger.Burger), True)
		self.assertEqual(isinstance(simplefactory_burger.GrilledMushroomBurger(), simplefactory_burger.Burger), True)
		self.assertEqual(isinstance(simplefactory_burger.CaramalizedOnionBurger(), simplefactory_burger.Burger), True)
		self.assertEqual(isinstance(simplefactory_burger.CheeseBurger(), simplefactory_burger.Burger), True)

	def test_orderedburger(self):
		factory = simplefactory_burger.BurgerFactory()
		store = simplefactory_burger.BurgerStore(factory)

		burger = store.order_burger("mixveggie")
		self.assertEqual(burger.get_burgername(), "Mix Veggie")

		burger = store.order_burger("grilledmushroom")
		self.assertEqual(burger.get_burgername(), "Grilled Mushroom")

		burger = store.order_burger()
		self.assertEqual(burger.get_burgername(), "Mix Veggie")

class TestFactoryMethodNaive(unittest.TestCase):
	def test_classes(self):
		self.assertEqual(inspect.isclass(factorymethod_naive.AbstractCreator), True)
		self.assertEqual(inspect.isclass(factorymethod_naive.ConcreteCreatorA), True)
		self.assertEqual(inspect.isclass(factorymethod_naive.ConcreteCreatorB), True)
		self.assertEqual(inspect.isclass(factorymethod_naive.AbstractProduct), True)
		self.assertEqual(inspect.isclass(factorymethod_naive.ConcreteProductA), True)
		self.assertEqual(inspect.isclass(factorymethod_naive.ConcreteProductB), True)

	def test_instances(self):
		self.assertEqual(isinstance(factorymethod_naive.AbstractCreator, ABCMeta), True)
		self.assertEqual(isinstance(factorymethod_naive.ConcreteCreatorA(), factorymethod_naive.AbstractCreator), True)
		self.assertEqual(isinstance(factorymethod_naive.ConcreteCreatorB(), factorymethod_naive.AbstractCreator), True)
		self.assertEqual(isinstance(factorymethod_naive.AbstractProduct, ABCMeta), True)
		self.assertEqual(isinstance(factorymethod_naive.ConcreteProductA(), factorymethod_naive.AbstractProduct), True)
		self.assertEqual(isinstance(factorymethod_naive.ConcreteProductB(), factorymethod_naive.AbstractProduct), True)

	def test_factorymethod(self):

		concretecreator = factorymethod_naive.ConcreteCreatorA()
		self.assertEqual(concretecreator.product.interface(), "I am in A")

class TestFactoryMethodCar(unittest.TestCase):

	def test_classes(self):
		self.assertEqual(inspect.isclass(factorymethod_car.Car), True)
		self.assertEqual(inspect.isclass(factorymethod_car.TeslaX), True)
		self.assertEqual(inspect.isclass(factorymethod_car.TeslaS), True)
		self.assertEqual(inspect.isclass(factorymethod_car.Tesla3), True)
		self.assertEqual(inspect.isclass(factorymethod_car.BMWi3s), True)
		self.assertEqual(inspect.isclass(factorymethod_car.BMW7), True)
		self.assertEqual(inspect.isclass(factorymethod_car.CarFactory), True)
		self.assertEqual(inspect.isclass(factorymethod_car.TeslaFactory), True)
		self.assertEqual(inspect.isclass(factorymethod_car.BMWFactory), True)

	def test_instances(self):
		self.assertEqual(isinstance(factorymethod_car.Car, ABCMeta), True)
		self.assertEqual(isinstance(factorymethod_car.TeslaX(), factorymethod_car.Car), True)
		self.assertEqual(isinstance(factorymethod_car.TeslaS(), factorymethod_car.Car), True)
		self.assertEqual(isinstance(factorymethod_car.Tesla3(), factorymethod_car.Car), True)
		self.assertEqual(isinstance(factorymethod_car.BMWi3s(), factorymethod_car.Car), True)
		self.assertEqual(isinstance(factorymethod_car.BMW7(), factorymethod_car.Car), True)
		self.assertEqual(isinstance(factorymethod_car.CarFactory, ABCMeta), True)
		self.assertEqual(isinstance(factorymethod_car.TeslaFactory(), factorymethod_car.CarFactory), True)
		self.assertEqual(isinstance(factorymethod_car.BMWFactory(), factorymethod_car.CarFactory), True)

	def test_orderedcar(self):
		teslafactory = factorymethod_car.TeslaFactory()
		bmwfactory = factorymethod_car.BMWFactory()

		car1 = teslafactory.order_car("tesla x")
		self.assertEqual(car1.get_carname(), "Tesla Model X")

		car2 = bmwfactory.order_car("bmw i3s")
		self.assertEqual(car2.get_carname(), "BMW i3s")