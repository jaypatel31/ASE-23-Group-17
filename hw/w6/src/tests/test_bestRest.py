import unittest
from DATA import DATA
from ROW import ROW
from COLS import COLS

class TestBEST(unittest.TestCase):
    def test_bestRest(self):
        # Step 1: Setup Test Data
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))  # Mocking COLS instance
        test_row = [12, 'Jay', 32]
        data.add(test_row)
        test_row2 = [6, 'Jay', 12]
        data.add(test_row2)
        test_row3 = [6, 'Mihir', 12]
        data.add(test_row3)
        
        want = 1 # Number of rows we want in the 'best' list

        expected_best = [12, 'Jay', 32]  # Just the data, not a ROW object
        expected_rest = [ [6, 'Jay', 12], [6, 'Mihir', 12]]  # List of data

        # Step 3: Invoke the Method
        best_data, rest_data = data.bestRest(data.rows, want)

        # Step 4: Assert Outcomes
        self.assertEqual(best_data.rows[0].cells, expected_best)  # Compare data of the first ROW in best_data
        self.assertEqual([row.cells for row in rest_data.rows], expected_rest)  # Compare list of data in rest_data

    def test_bestRest_emptyData(self):
        # Testing with no data added
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))  # Mocking COLS instance

        want = 1
        best_data, rest_data = data.bestRest(data.rows, want)

        self.assertEqual(best_data.rows, [])
        self.assertEqual(rest_data.rows, [])

    def test_branch(self):
        data = DATA([])
        data.cols = COLS(ROW(['Age', 'name', 'Grade!']))  # Mocking COLS instance
        test_row = [12, 'Jay', 32]
        data.add(test_row)
        test_row2 = [6, 'Jay', 12]
        data.add(test_row2)
        test_row3 = [6, 'Mihir', 12]
        data.add(test_row3)

        # Perform branching
        stop_condition = 2  # Define a stopping condition for the branch
        best, rest, evals = data.branch(stop=stop_condition)

        # Assertions
        self.assertTrue(len(best.rows) <= stop_condition, "Best subset exceeds stop condition")
        self.assertTrue(len(rest.rows) <= stop_condition, "Rest subset exceeds stop condition")

        

if __name__ == '__main__':
    unittest.main()
