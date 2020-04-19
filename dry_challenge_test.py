import unittest
from dry_challenge_soln import *

class TestDry(unittest.TestCase):
    def test_ones(self):
        self.assertEqual(sub_thousands(2),"Two")
    def test_hundreds(self):
        self.assertEqual(sub_thousands(423),"Four Hundred Twenty Three")
    def test_thousands(self):
        self.assertEqual(handle_thousands(1000),"One Thousand")
        self.assertEqual(handle_thousands(5672),"Five Thousand, Six Hundred Seventy Two  ")
        self.assertEqual(handle_thousands(45781),"Forty Five Thousand, Seven Hundred Eighty One  ")
    def test_not_ones(self):
        self.assertFalse(sub_thousands(101)=="Two")
    def test_not_hundreds(self):
        self.assertFalse(sub_thousands(200)=="Three Hundred")
    def test_not_thousands(self):
        self.assertFalse(handle_thousands(3)=="Three Thousand")
    def test_type_numbers(self):
        with self.assertRaises(TypeError):
            self.assertFalse(isinstance("Two",'int'))

#if __name__ == "__main__":
#    unittest.main()
