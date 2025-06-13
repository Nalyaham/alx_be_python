import unittest
from simple_calculator import SimpleCalculator
def setUp(self):
    self.calc = SimpleCalculator()

def test_addition(self):
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)

def setUp(self):
    self.calc = SimpleCalculator()
def test_subtraction(self):
    self.assertEqual(self.calc.subtract(4, 2), 2)
    self.assertEqual(self.calc.subtract(-1, 1), 2)

def setUp(self):
    self.calc = SimpleCalculator()
def test_multiplication(self):
    self.assertEqual(self.calc.multiply(2, 3), 6)
    self.assertEqual(self.calc.multiply(-1, 1), -1)

def setUp(self):
    self.calc = SimpleCalculator()
def test_divide(self):
    self.assertEqual(self.calc.divide(4, 2), 2)
    self.assertEqual(self.calc.divide(-1, 1), -1)
    self.assertEqual(self.calc.divide(2, 0), "None") 
