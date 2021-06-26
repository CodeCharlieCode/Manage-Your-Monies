from abc import abstractclassmethod
import unittest
from models.transactions import Transaction

class TestTransaction (  unittest.TestCase  ):

    def setUp(self):
        self.transaction_1 = Transaction("Sainsburys","Food", "Weekly Food Shop", 53.98, 11-11-2020, 96)
        self.transcation_2 = Transaction("Loudons", "Eating Out", "Brunching", 20, 26-6-2021, 5)

    def test_merchant(self):
        expected = "Sainsburys"
        actual = self.transaction_1.merchant
        self.assertEqual(expected, actual)

    def test_category(self):
        expected = "Eating Out"
        actual = self.transcation_2.category
        self.assertEqual(expected, actual)

    def test_description(self):
        expected = "Weekly Food Shop"
        actual = self.transaction_1.description
        self.assertEqual(expected, actual)

    def test_amount(self):
        expected = 53.98
        actual = self.transaction_1.amount
        self.assertEqual(expected, actual)

    def test_date(self):
        expected = 26-6-2021
        actual = self.transcation_2.date
        self.assertEqual(expected, actual)

    def test_id(self):
        expected = 5
        actual = self.transcation_2.id
        self.assertEqual(expected, actual)