import unittest

from models.merchant import Merchant

class TestMerchant(  unittest.TestCase  ):

    def setUp(self):
        self.merchant_1 = Merchant("ASDA", 12)
        self.merchant_2 = Merchant("Tesco", 18)

    def test_merchant_name(self):
        expected = "ASDA"
        actual = self.merchant_1.name
        self.assertEqual(expected, actual)

    def test_merchant_id(self):
        expected = 18
        actual = self.merchant_2.id
        self.assertEqual(expected, actual)