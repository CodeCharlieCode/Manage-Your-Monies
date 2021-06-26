import unittest

from models.category import Category

class TestCategory(  unittest.TestCase  ):

    def setUp(self):
        self.category_1 = Category("Extreme Sports", 168.37, 108)
        self.category_2 = Category("Bills", 1089, 47)

    def test_name(self):
        expected = "Extreme Sports"
        actual = self.category_1.name
        self.assertEqual(expected, actual)

    def test_budget(self):
        expected = 1089
        actual = self.category_2.budget
        self.assertEqual(expected, actual)

    def test_id(self):
        expected = 108
        actual = self.category_1.id
        self.assertEqual(expected, actual)