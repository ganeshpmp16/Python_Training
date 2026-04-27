import unittest # 
from calclualator import add # Importing the add function from the calclualator module to test it   
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -5), -10)
if __name__ == '__main__':
    unittest.main()