import unittest

from models.profile import Profile 

class TestProfile(  unittest.TestCase  ):
    def setUp(self):
        self.profile_1 = Profile(103.02, 127.92, 66)
        self.profile_2 = Profile(158.98, 1049.28, 36)

    def test_balance(self):
        expected = 103.02
        actual = self.profile_1.balance
        self.assertEqual(expected, actual)

    def test_total_budget(self):
        expected = 1049.28
        actual = self.profile_2.total_budget
        self.assertEqual(expected, actual)

    def test_profile_id(self):
        expected = 66
        actual = self.profile_1.id
        self.assertEqual(expected, actual)