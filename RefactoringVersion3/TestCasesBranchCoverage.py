import unittest
from Program import *

class TestBranchCoverage(unittest.TestCase):

    def setUp(self):
        print("test started")
        self.myController = Controller(TestView())

    def tearDown(self):
        print("test finished")

    def test_add(self):
        data = "A001 F 36 92 Normal"
        with self.assertRaises(InsufficientArgumentsException) as context:
            self.myController._add(data)

        self.assertTrue("Not Enough Arguments Provided", context.exception)