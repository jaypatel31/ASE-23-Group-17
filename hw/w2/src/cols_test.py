import unittest

class TestCOLS(unittest.TestCase):
    def test_add_numeric_row(self):
        row1 = ["A", "B", "C", "D"]
        row2 = ["1", "2", "3", "!"]

        cols_instance = COLS(row1)
        cols_instance.add(row2)

        # Check if the numeric column values have been updated correctly
        self.assertEqual(cols_instance.x[0].value, 1.0)
        self.assertEqual(cols_instance.x[1].value, 2.0)
        self.assertEqual(cols_instance.x[2].value, 3.0)

    def test_add_symbolic_row(self):
        row1 = ["A", "B", "C", "D"]
        row2 = ["apple", "banana", "cherry", "!"]

        cols_instance = COLS(row1)
        cols_instance.add(row2)

        # Check if the symbolic columns remain unchanged after adding a symbolic row
        self.assertEqual(cols_instance.y[0].value, "apple")
        self.assertEqual(cols_instance.y[1].value, "banana")
        self.assertEqual(cols_instance.y[2].value, "cherry")

    def test_class_column(self):
        row1 = ["A", "B", "C", "D!"]
        row2 = ["1", "2", "3", "!"]

        cols_instance = COLS(row1)

        # Check if the class column is correctly identified
        self.assertIsNotNone(cols_instance.klass)
        self.assertEqual(cols_instance.klass.txt, "D!")

if __name__ == '__main__':
    unittest.main()
