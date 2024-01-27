import unittest
from unittest.mock import patch

from COLS import COLS
from ROW import ROW
from NUM import NUM
from SYM import SYM


class TestCOLS(unittest.TestCase):

    def test_initialization_of_columns(self):
        # Test initialization of NUM and SYM columns
        row = ROW(['AGE', 'name', 'GRADE!'])
        cols = COLS(row)

        # print(cols.all[0].n)
        row2 = ROW([10, 'JAY', 12])
        
        cols.add(row2)

        row3 = ROW([5, 'JAY', 12])
        cols.add(row3)

        self.assertIsInstance(cols.all[0], NUM, "AGE should be a NUM")
        self.assertIsInstance(cols.all[1], SYM, "name should be a SYM")

        # self.assertEqual(cols.all[0].n, 2, "AGE column should have 2 entries")
        # self.assertEqual(cols.all[1].count, 2, "name column should have 2 entries")
        # self.assertEqual(cols.all[2].mode, 'A', "GRADE column's mode should be 'A'")

    def test_classification_and_handling_of_klass_column(self):
        # Test identification and handling of klass column
        row = ROW(['age', 'name', 'GRADE!'])
        cols = COLS(row)
        self.assertEqual(cols.klass, cols.all[2], "GRADE should be klass")
        self.assertIsInstance(cols.klass, NUM, "GRADE should be a NUM instance")

    def test_update_of_columns_on_row_addition(self):
        # Test update of NUM and SYM columns when new rows are added
        row = ROW(['AGE', 'name', 'GRADE!'])
        cols = COLS(row)

        # print(cols.all[0].n)
        row2 = ROW([11, 'JAY', 12])
        
        cols.add(row2)

        row3 = ROW([5, 'JAY', 12])
        cols.add(row3)
        # Check updates in NUM column
        num_col = cols.all[0]  # Assuming AGE is the first NUM column
        self.assertEqual(num_col.n, 2, "NUM column should have 2 entries")
        self.assertGreater(num_col.mu, 0, "Mean of NUM column should be calculated")

        # Check updates in SYM column
        # sym_col = cols.all[1]  # Assuming name is the first SYM column
        # self.assertEqual(sym_col.count, 2, "SYM column should have 2 entries")
        # self.assertGreaterEqual(sym_col.mode, 'Alice', "Mode of SYM column should be calculated")


if __name__ == '__main__':
    unittest.main()
