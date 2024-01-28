import unittest
from DATA import DATA
class TestSplitMethod(unittest.TestCase):

    def setUp(self):
        # Initialize test data
        self.example_data = {
            "best": [1, 2, 3],
            "rest": [4, 5, 6],
            "lite": [7, 8, 9],
            "dark": [[10, 11, 12], [13, 14, 15]]
        }

    def test_basic_split(self):
        # Test the method with basic data
        best = self.example_data["best"]
        rest = self.example_data["rest"]
        lite = self.example_data["lite"]
        dark = self.example_data["dark"]
        # Call the split method with the provided data
        out, selected = DATA.split(None, best, rest, lite, dark)
        # Write assertions to check if the split is done correctly
        self.assertEqual(out, 1)  # Adjust the expected output as per your expectations

    def test_empty_inputs(self):
        # Test the method with empty inputs
        best = []
        rest = []
        lite = []
        dark = []
        out, selected = DATA.split(None, best, rest, lite, dark)
        # Write assertions to check if the method handles empty inputs gracefully
        self.assertEqual(out, 0)  # Adjust the expected output as per your expectations

    # Add more test cases following the same pattern for different scenarios

if __name__ == '__main__':
    unittest.main()
