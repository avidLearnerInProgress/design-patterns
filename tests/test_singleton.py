"""
Author: CHIRAG SHAH
Created On: 7th July 2018
Modified On: 16th July 2018
"""

import unittest, sys, inspect
from pathlib import Path


ROOT_DIR = str(Path(__file__).resolve().parent.parent)
sys.path.append(ROOT_DIR)

from pydesignpatterns.creational import (
	singleton_naive,
	singleton_lazy_instantiation,
	singleton_decorator,
	singleton_thread,
	singleton_metaclass,
	singleton_counter
)

class TestSingleton(unittest.TestCase):

	def test_class(self):
		self.assertEqual(inspect.isclass(singleton_naive.Singleton), True)

	def test_instances(self):
		s1, hs1 = singleton_naive.Singleton()
		s2, hs2 = singleton_naive.Singleton()
		self.assertEqual(id(s1), id(s2))
	
	def test_hashes(self):
		s1, hs1 = singleton_naive.Singleton()
		s2, hs2 = singleton_naive.Singleton()
		self.assertEqual(hs1, hs2)

class TestSingletonLazy(unittest.TestCase):

	def test_class(self):
		self.assertEqual(inspect.isclass(singleton_lazy_instantiation.SingletonLazy), True)

	def test_instances(self):
		s1 = singleton_lazy_instantiation.SingletonLazy().get_instance()
		s2 = singleton_lazy_instantiation.SingletonLazy().get_instance()
		self.assertEqual(s1, s2)
		self.assertEqual(id(s1), id(s2))

	def test_lazy_instantiation(self):
		s1 = singleton_lazy_instantiation.SingletonLazy().get_instance()
		s2 = singleton_lazy_instantiation.SingletonLazy()
		self.assertNotEqual(s1, s2)

class TestSingletonDecorated(unittest.TestCase):

	def test_class(self):
		self.assertEqual(inspect.isclass(singleton_decorator.SingletonDecorated), True)

	def test_instances(self):
		s1 = lambda: singleton_decorator.VeniVediVici().instance()
		s2 = lambda: singleton_decorator.VeniVediVici().instance()
		self.assertEqual(isinstance(s1, singleton_decorator.SingletonDecorated), isinstance(s2, singleton_decorator.SingletonDecorated))

	def test_instance_exception(self):
		self.assertRaises(TypeError, lambda: singleton_decorator.VeniVediVici())

class TestSingletonThreaded(unittest.TestCase):

	def test_class(self):
		self.assertEqual(inspect.isclass(singleton_thread.SingletonThread), True)

	def test_instances(self):
		print("\n")
		s1 = singleton_thread.SingletonThread().get_instance()
		s2 = singleton_thread.SingletonThread().get_instance()
		self.assertEqual(s1, s2)

	def test_threadsafe(self):
		ts1 = singleton_thread.SingletonThread().get_instance().gettid()
		ts2 = singleton_thread.SingletonThread().get_instance().gettid()
		self.assertEqual(ts1, ts2)

class TestSingletonMetaClass(unittest.TestCase):

	def test_class(self):
		self.assertEqual(inspect.isclass(singleton_metaclass.SingletonMetaclass), True)

	def test_instances(self):
		self.assertEqual(isinstance(singleton_metaclass.A, singleton_metaclass.SingletonMetaclass), isinstance(singleton_metaclass.B, singleton_metaclass.SingletonMetaclass))

class TestSingletonCounter(unittest.TestCase):

	def test_class(self):
		self.assertEqual(inspect.isclass(singleton_counter.SingletonCounter), True)

	def test_instances(self):
		s1 = singleton_counter.SingletonCounter.get_instance()
		s2 = singleton_counter.SingletonCounter.get_instance()
		self.assertEqual(s1, s2)

	def test_count(self):
		s1 = singleton_counter.SingletonCounter.get_instance()
		self.assertEqual(s1.get_count(), 1)
		s2 = singleton_counter.SingletonCounter.get_instance()
		self.assertEqual(s2.get_count(), 2)