import unittest
import sys
sys.path.append(r'C:\Users\Даниил\Desktop\cs-102')
from src.lab1.calculator import summ, difference, multiply, division, exponentiation

class CalculatorTestCase(unittest.TestCase):
    
    def test_summ(self):
        self.assertEqual(summ(1, 2), 3)

    def test_difference(self):
        self.assertEqual(difference(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)

    def test_division(self):
        self.assertEqual(division(6, 2), 3)

    def test_exponentiation(self):
        self.assertEqual(exponentiation(3, 3), 27)
