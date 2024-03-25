import unittest
from DATA import DATA
class TestSplitMethod(unittest.TestCase):

    def setUp(self):
        # Initialize test data
        self.example_data = {
            "best": DATA(0).add([4, 119, 82, 82, 1, 2720, 19.4, 30]),
            "rest": [4, 5, 6],
            "lite": [7, 8, 9],
            "dark": [[10, 11, 12], [13, 14, 15]]
        }

    def test_basic_split(self):
        # Test the method with basic data
        # best = self.example_data["best"]
        # rest = self.example_data["rest"]
        # lite = self.example_data["lite"]
        # dark = self.example_data["dark"]
        # # Call the split method with the provided data
        # out, selected = DATA(0).split(best, rest, lite, dark)
        # # Write assertions to check if the split is done correctly
        # self.assertEqual(out, 1)  # Adjust the expected output as per your expectations
        # print("out is",out)
        # Sample data for testing the split function
# Define sample rows for best, rest, lite, and dark datasets
        best_data = [
            [1, 2, 3, 4, 5, 6, 7],
            [2, 3, 4, 5, 6, 7, 8],
            [3, 4, 5, 6, 7, 8, 9]
        ]

        rest_data = [
            [4, 5, 6, 7, 8, 9, 10],
            [5, 6, 7, 8, 9, 10, 11],
            [6, 7, 8, 9, 10, 11, 12]
        ]

        lite_data = [
            [7, 8, 9, 10, 11, 12, 13],
            [8, 9, 10, 11, 12, 13, 14],
            [9, 10, 11, 12, 13, 14, 15]
        ]

        dark_data = [
            [10, 11, 12, 13, 14, 15, 16],
            [11, 12, 13, 14, 15, 16, 17],
            [12, 13, 14, 15, 16, 17, 18]
        ]


        row1 = [1, 2, 3, 4, 5, 6, 7]
        row2 = [2, 3, 4, 5, 6, 7, 8]
        row3 = [3, 4, 5, 6, 7, 8, 9]
        # Add rows to DATA object
        self.data.add(row1)
        self.data.add(row2)
        self.data.add(row3)

        # Call the split function
        # Pass appropriate parameters
        out, selected = self.data.split(best=best_data, rest=rest_data, lite=lite_data, dark=dark_data)

        # Define the expected outcome based on your understanding of the split function
        expected_outcome = 0  # Expected value for 'out'
        # You need to define the expected 'selected' data based on your test scenario

        # Assert the correctness of the output
        self.assertEqual(out, expected_outcome)
        # Add assertions for 'selected' based on your test scenario


    def test_empty_inputs(self):
        # Test the method with empty inputs
        best = []
        rest = []
        lite = []
        dark = []
        out, selected = DATA.split(None, best, rest, lite, dark)
        # Write assertions to check if the method handles empty inputs gracefully
        self.assertEqual(out, 0)  # Adjust the expected output as per your expectations


if __name__ == '__main__':
    unittest.main()
