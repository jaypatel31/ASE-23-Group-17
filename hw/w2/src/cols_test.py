import unittest
from unittest.mock import patch

# Assuming NUM, SYM, and COLS classes are defined in the same file or are properly accessible
from NUM import NUM
from SYM import SYM
from COLS import COLS

class TestCOLS(unittest.TestCase):

    def test_init(self):
        row = ["A", "B", "C", "Class!"]
        cols_instance = COLS(row)
        
        # Checking if the columns are initialized correctly
        self.assertEqual(len(cols_instance.x), 3)
        self.assertEqual(len(cols_instance.y), 1)
        self.assertEqual(len(cols_instance.all), 4)
        self.assertIsNotNone(cols_instance.klass)
        self.assertEqual(cols_instance.klass.txt, "Class!")

    def test_add(self):
        row = ["A", "B", "C", "Class!"]
        cols_instance = COLS(row)
        
        # Adding values to the columns instance
        new_row = ["1", "2", "3", "Positive"]
        cols_instance.add(new_row) 
        
        # Checking if the values are added to the columns correctly
        self.assertEqual(cols_instance.x[0].n, 1)
        self.assertEqual(cols_instance.x[1].n, 2)
        self.assertEqual(cols_instance.x[2].n, 3)
        self.assertEqual(cols_instance.y[0].n, 1)

    def test_add_with_missing_values(self):
        row = ["A", "B", "C", "Class!"]
        cols_instance = COLS(row)
        
        # Adding values with missing values to the columns instance
        new_row = ["1", "?", "3", "?"]
        cols_instance.add(new_row)
        
        # Checking if the missing values are handled correctly
        self.assertEqual(float(cols_instance.x[0].n), 1)
        self.assertEqual(cols_instance.x[1].n, 0)  # Missing value should not affect count
        self.assertEqual(cols_instance.x[2].n, 3)
        self.assertEqual(cols_instance.y[0].n, 1)

    def test_add_multiple_rows(self):
        row = ["A", "B", "C", "Class!"]
        cols_instance = COLS(row)
        
        # Adding multiple rows to the columns instance
        new_rows = [["1", "2", "3", "Positive"], ["4", "5", "6", "Negative"]]
        for r in new_rows:
            cols_instance.add(r)
        
        # Checking if values are added from multiple rows correctly
        self.assertEqual(cols_instance.x[0].n, 5)
        self.assertEqual(cols_instance.x[1].n, 7)
        self.assertEqual(cols_instance.x[2].n, 9)
        self.assertEqual(cols_instance.y[0].n, 2)

if __name__ == '__main__':
    unittest.main()
