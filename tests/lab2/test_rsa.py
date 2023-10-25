import unittest
import sys
from src.lab2.rsa import is_prime

class CalculatorTestCase(unittest.TestCase):

    def test_is_prime1(self):
        self.assertEqual(is_prime(7), True)

    def test_is_prime2(self):
        self.assertEqual(is_prime(11), True)
    
    def test_is_prime3(self):
        self.assertEqual(is_prime(41), True)
