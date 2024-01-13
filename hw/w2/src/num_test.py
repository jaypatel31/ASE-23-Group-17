import unittest
from unittest.mock import patch
from NUM import NUM

class TestNUM(unittest.TestCase):
    def setUp(self):
        # Create an instance of NUM for testing
        self.num_instance = NUM()

    def test_add_multiple_values(self):
        # Test adding multiple numeric values
        values = [3, 7, 5, 8, 2]
        for value in values:
            self.num_instance.add(value)

        self.assertEqual(self.num_instance.n, len(values))
        self.assertAlmostEqual(self.num_instance.mu, sum(values) / len(values), delta=1e-10)
        self.assertAlmostEqual(self.num_instance.m2, sum((x - self.num_instance.mu) ** 2 for x in values), delta=1e-10)
        self.assertEqual(self.num_instance.lo, min(values))
        self.assertEqual(self.num_instance.hi, max(values))

if __name__ == '__main__':
    unittest.main()