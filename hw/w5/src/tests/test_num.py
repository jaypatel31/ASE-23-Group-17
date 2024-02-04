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
    
    def test_like_function(self):
        x = 5
        mu = 5 
        sd = 2
        expected_value = 0.2
        
        with patch.object(NUM, 'mid', return_value=mu):
            with patch.object(NUM, 'div', return_value=sd):
                likelihood = self.num_instance.like(x,0,0)
        
        self.assertAlmostEqual(likelihood, expected_value)
    
    def test_x_question_mark(self):
        # Test when x is "?" and y is a valid value
        x = "?"
        y = 0.3
        expected_distance = 1.3  # Assuming self.norm(0.3) returns 0.3
        self.assertEqual((round(self.num_instance.dist(x, y),1)), expected_distance)

    def test_y_question_mark(self):
        # Test when y is "?" and x is a valid value
        x = 0.8
        y = "?"
        expected_distance = 1.2  # Assuming self.norm(0.8) returns 0.8
        self.assertEqual(self.num_instance.dist(x, y), expected_distance)


if __name__ == '__main__':
    unittest.main()