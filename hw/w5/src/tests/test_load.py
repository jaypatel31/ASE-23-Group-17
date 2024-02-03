import unittest
from unittest.mock import mock_open, patch, MagicMock

from COLS import COLS
from ROW import ROW
from NUM import NUM
from SYM import SYM
from DATA import DATA
from load import data1, data2, load, learn


class TestLoad(unittest.TestCase):
    def setUp(self):
        # Mocking the data and row objects
        self.mock_data = MagicMock()
        self.mock_data.cols.klass.at = 0
        self.mock_data.cols.names.cells = ['name1', 'name2']

        self.mock_row = MagicMock()
        self.mock_row.cells = [1, 'value']
        self.mock_row.likes.return_value = [1]

        self.my = {'n': 0, 'tries': 0, 'acc': 0, 'datas': {}}

    def test_learn(self):
        # Initial call to learn
        learn(self.mock_data, self.mock_row, self.my)
        self.assertEqual(self.my['n'], 1)
        self.assertIn(1, self.my['datas'])
        self.assertIsInstance(self.my['datas'][1], DATA)

        # Subsequent call to learn with different row
        self.mock_row.cells = [2, 'another value']
        self.mock_row.likes.return_value = [2]
        learn(self.mock_data, self.mock_row, self.my)
        self.assertEqual(self.my['n'], 2)
        self.assertIn(2, self.my['datas'])
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)
        learn(self.mock_data, self.mock_row, self.my)

        # Check accuracy update
        self.assertEqual(self.my['acc'], 4)  #check if accc is incremented 4 times after 14 calls to learn
    
    @patch('builtins.open', new_callable=mock_open, read_data='mocked file data')
    def test_load(self, mock_file):
        # Call the load method
        load()

        # Verify that the file was opened correctly
        mock_file.assert_called_with('././data/soybean.csv',  'r', encoding='locale', errors=None)

        # Verify that global variables are set correctly
        self.assertIsNotNone(data1)
        self.assertIsNotNone(data2)
        # Add more assertions to verify the content of global_var

if __name__ == '__main__':
    unittest.main()
