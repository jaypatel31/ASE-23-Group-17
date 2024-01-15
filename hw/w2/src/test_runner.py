import argparse
import unittest
import os
import sys


sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests'))

from NUM import NUM
from test_num import TestNUM

class CollectAfterT(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, [option_string] + values)

def run_tests(test_name):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNUM)
    suite_all = unittest.TestLoader().loadTestsFromTestCase(TestNUM)

    if "all" in test_name:
        # Run all tests if "all" is passed
        pass
    else:
        filtered_suite = unittest.TestSuite()
        for test in suite:
            if any(name == test.id() for name in test_name):
                filtered_suite.addTest(test)
        suite = filtered_suite
        # suite = unittest.TestSuite([test for test in suite if any(name in test.id() for name in test_name)])
    

    if(len(suite._tests)==0):
        print("No tests found for: ", test_name)
        print("Available Tests are:")
        for test in suite_all:
            print(test.id())
        return 1
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return len(result.failures)

def test():
    args = sys.argv[1:]
    test_index = args.index('-t') if '-t' in args else args.index('--test') if '--test' in args else -1

    if test_index != -1:
        next_option_index = next((i for i, arg in enumerate(args[test_index + 1:], start=test_index + 1) if arg.startswith('-')), len(args))
        test_args = args[test_index + 1:next_option_index]
        print(f"Running tests: {test_args}\n")
    

    fail_count = run_tests(test_args)

    if fail_count > 0:
        exit(fail_count)

if __name__ == '__main__':
    test()