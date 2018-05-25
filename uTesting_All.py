import unittest

from uTesting_server import FlaskTestCase

'''
    This file executes ALL of the test files. 
    The test files can still be executed individually,
        if you only wish to execute a single set of tests. 
'''

if __name__ == '__main__':
    # Run specified tests
    test_classes_to_run = [
        FlaskTestCase
    ]

    suites_list = []
    for test_class in test_classes_to_run:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    results = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suites_list))

    print("Test success:", results.wasSuccessful())  # Overall success.
    results.printErrors()
