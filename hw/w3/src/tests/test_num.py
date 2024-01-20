import unittest
from unittest.mock import patch
from NUM import NUM

class TestNUM(unittest.TestCase):
    def setUp(self):
        # Create an instance of NUM for testing
        self.num_instance = NUM()
        self.values = [3, 7, 5, 8, 2]
        for value in self.values:
            self.num_instance.add(value)
        
    def test_num_add(self):
        # Test checking the addition of new number
        self.assertEqual(self.num_instance.n, len(self.values)) 
    
    def test_num_stats(self):
        # Test Checking Stats of Values

        self.assertAlmostEqual(self.num_instance.mid(), sum(self.values) / len(self.values), delta=1e-10)
        self.assertAlmostEqual(self.num_instance.m2, sum((x - self.num_instance.mu) ** 2 for x in self.values), delta=1e-10)
        self.assertEqual(self.num_instance.lo, min(self.values))
        self.assertEqual(self.num_instance.hi, max(self.values))

if __name__ == '__main__':
    unittest.main()