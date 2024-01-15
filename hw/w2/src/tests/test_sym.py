import unittest
from unittest.mock import patch
from SYM import SYM

class TestSYM(unittest.TestCase):

    def setUp(self):
        self.sym_instance = SYM("TestSYM", 0)  # Initialize SYM instance for testing

    def test_init(self):
        self.assertEqual(self.sym_instance.txt, "TestSYM")
        self.assertEqual(self.sym_instance.at, 0)
        self.assertEqual(self.sym_instance.n, 0)
        self.assertEqual(self.sym_instance.has, {})
        self.assertIsNone(self.sym_instance.mode)
        self.assertEqual(self.sym_instance.most, 0)

    def test_add_single_value(self):
        self.sym_instance.add("Category1")
        self.assertEqual(self.sym_instance.n, 1)
        self.assertEqual(self.sym_instance.has["Category1"], 1)
        self.assertEqual(self.sym_instance.mode, "Category1")
        self.assertEqual(self.sym_instance.most, 1)

    def test_add_multiple_values(self):
        values = ["Category1", "Category2", "Category1", "Category3"]
        for value in values:
            self.sym_instance.add(value)

        self.assertEqual(self.sym_instance.n, 4)
        self.assertEqual(self.sym_instance.has["Category1"], 2)
        self.assertEqual(self.sym_instance.has["Category2"], 1)
        self.assertEqual(self.sym_instance.has["Category3"], 1)
        self.assertEqual(self.sym_instance.mode, "Category1")
        self.assertEqual(self.sym_instance.most, 2)

    def test_add_missing_value(self):
        self.sym_instance.add("?")
        self.assertEqual(self.sym_instance.n, 0)  # Value "?" should not be counted
        self.assertEqual(len(self.sym_instance.has), 0)
        self.assertIsNone(self.sym_instance.mode)
        self.assertEqual(self.sym_instance.most, 0)

    def test_mid(self):
        self.sym_instance.add("Category1")
        self.sym_instance.add("Category2")
        self.assertEqual(self.sym_instance.mid(), "Category1")

    def test_div(self):
        self.sym_instance.add("Category1")
        self.sym_instance.add("Category2")
        entropy = self.sym_instance.div(0)
        self.assertGreaterEqual(entropy, 0)

    def test_small(self):
        self.assertEqual(self.sym_instance.small(), 0)

if __name__ == '__main__':
    unittest.main()
