import unittest
from DATA import DATA
from ROW import ROW
from COLS import COLS

class TestDATA(unittest.TestCase):
    def test_init(self):
        data = DATA([])
        self.assertEqual(data.rows, [])
        self.assertIsNone(data.cols)

    def test_addition_of_rows(self):
        # Test addition of rows to DATA
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))
        test_row = [12, 'Jay', 32]
        data.add(test_row)
        test_row2 = [6, 'Jay', 12]
        data.add(test_row2)
        self.assertEqual(len(data.rows), 2, "Should have 2 rows added")
        self.assertIsNotNone(data.cols, "Cols should be initialized")

    def test_add_with_existing_cols(self):
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))  # Mocking COLS instance
        test_row = [12, 'Jay', 32]
        data.add(test_row)
        test_row2 = [6, 'Jay', 12]
        data.add(test_row2)
        test_row3 = [6, 'Mihir', 12]
        data.add(test_row3)
        # print()
        self.assertEqual(len(data.rows), 3)
        self.assertIsInstance(data.rows[0], ROW)

    # def test_basic_split(self):
    #     # Define the inputs
    #     best = "feature1"
    #     rest = ["feature2", "feature3"]
    #     lite = []  # Lite dataset (not used in the split function)
    #     dark = [ROW(), ROW(), ROW()]  # Dark dataset with rows

    #     # Call the split function
    #     index, selected = DATA.split(best, rest, lite, dark)

    #     # Assert the expected output
    #     self.assertEqual(index, 0)
    #     self.assertEqual(selected, expected_selected)

    def test_no_dark_rows(self):
        # Define the inputs
        best = "feature1"
        rest = ["feature2", "feature3"]
        lite = []  # Lite dataset (not used in the split function)
        dark = []  # Empty dark dataset

        # Call the split function
        index, selected = split(best, rest, lite, dark)

        # Assert the expected output
        self.assertEqual(index, 1)
        self.assertEqual(len(selected), 0)

    def test_max_value_at_beginning(self):
        # Define the inputs
        best = "feature1"
        rest = ["feature2", "feature3"]
        lite = []  # Lite dataset (not used in the split function)
        dark = [ROW(0), ROW(0), ROW(0)]  # Dark dataset with rows

        # Call the split function
        index, selected = split(best, rest, lite, dark)

        # Assert the expected output
        self.assertEqual(index, 0)
        self.assertEqual(selected, dark[0])

if __name__ == '__main__':
    unittest.main()
