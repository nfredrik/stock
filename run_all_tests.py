import unittest

import test_myclass
import test_mockbors  # mock for Bors
import test_mock      # mock for Morningstar :-)

import test_stock        # test Bors for real, we need internet ...
import test_morningstar  # test Morningstar

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_myclass)

suite.addTests(loader.loadTestsFromModule(test_mockbors))
suite.addTests(loader.loadTestsFromModule(test_mock))

suite.addTests(loader.loadTestsFromModule(test_stock))
suite.addTests(loader.loadTestsFromModule(test_morningstar))

runner = unittest.TextTestRunner(verbosity=10)
result = runner.run(suite)
