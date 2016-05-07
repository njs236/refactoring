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

    def test_selectRecord(self):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        actual = self.myController._selectRecord('A001')

        self.assertEqual(actual, True)

    def test_selectOption(self):
        actual = self.myController._selectOption('AUTOID')

        self.assertEqual(actual, True)

    def test_editAge(self,):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        self.myController._selectRecord('A001')
        actual = self.myController._editAge(20)

        self.assertEqual(actual, True)

    def test_editSales(self):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        self.myController._selectRecord('A001')
        actual = self.myController._editSales(455)

        self.assertEqual(actual, True)

    def test_editBmi(self):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        self.myController._selectRecord('A001')
        actual = self.myController._editBmi('Normal')

        self.assertEqual(actual, True)

    def test_editIncome(self):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        self.myController._selectRecord('A001')
        actual = self.myController._editIncome(999)

        self.assertEqual(actual, True)

    def test_turnOn(self):
        self.myController._selectOption('AUTOID')
        actual = self.myController._turnOn()

        self.assertEqual(actual, True)

    def test_turnOff(self):
        self.myController._selectOption('AUTOID')
        actual = self.myController._turnOff()

        self.assertEqual(actual, True)
