import unittest
from Program import *


class TestStatementCoverage(unittest.TestCase):

    def setUp(self):
        print("test started")
        self.myController = Controller(TestView())

    def tearDown(self):
        print("test finished")

    def test_add(self):
        data = "A001 F 36 92 Normal 700"
        actual = self.myController._add(data)
        expected = True

        self.assertEqual(actual, expected,
                         "passed add test")

    def test_stall(self):
        actual = self.myController._stall()
        expected = True

        self.assertEqual(actual, expected,
                         "passed stall test")

    def test_representrecord(self):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        record = self.myController._theColl.getRecord("A001")
        actual = self.myController._representRecord(record)
        expected = True

        self.assertEqual(actual, expected,
                         "passed represent record test")

    def test_representoption(self):
        option = self.myController._options["AUTOID"]
        actual = self.myController._representOption(option)
        expected = True

        self.assertEqual(actual, expected,
                         "passed represent option test")

    def test_representERP(self):
        actual = self.myController._representERP()
        expected = True

        self.assertEqual(actual, expected,
                         "passed represent ERP test")

    def test_enterrecordselectedstate(self):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        self.myController._selectRecord("A001")
        actual = self.myController._enterRecordSelectedState()
        expected = True

        self.assertEqual(actual, expected,
                         "passed enter record selected state test")

    def test_enteroptionselectedstate(self):
        self.myController._selectOption("AUTOID")
        actual = self.myController._enterOptionSelectedState()
        expected = True

        self.assertEqual(actual, expected,
                         "passed enter option selected state test")

    def test_enterNeutralState(self):
        actual = self.myController._enterNeutralState()
        expected = True

        self.assertEqual(actual, expected,
                         "passed enter neutral state test")

    def test_dographicagechart(self):
        actual = self.myController._printAgeData(0, 100, 10)

        self.assertEqual(actual, True)

    def test_printGenderData(self):
        actual = self.myController._printGenderData()

        self.assertEqual(actual, True)

    def test_selectRecord(self):
        actual = self.myController._selectRecord()

        self.assertEqual(actual, False)

    def test_selectOption(self):
        actual = self.myController._selectOption()

        self.assertEqual(actual, False)

    def test_textSave(self):
        data = "A001 F 36 92 Normal 700"
        self.myController._add(data)
        actual = self.myController._textSave()
        expected = ['A001 F 36 92 Normal 700']
        self.assertEqual(actual, expected)

    def test_editAge(self,):
        actual = self.myController._editAge(20)

        self.assertEqual(actual, False)

    def test_editSales(self):
        actual = self.myController._editSales(455)

        self.assertEqual(actual, False)

    def test_editBmi(self):
        actual = self.myController._editBmi('Normal')

        self.assertEqual(actual, False)

    def test_editIncome(self):
        actual = self.myController._editIncome(999)

        self.assertEqual(actual, False)

    def test_turnOn(self):
        actual = self.myController._turnOn()

        self.assertEqual(actual, False)

    def test_turnOff(self):
        actual = self.myController._turnOff()

        self.assertEqual(actual, False)

    def test_viewRecords(self):
        actual = self.myController._viewRecords()

        self.assertEqual(actual, True)

    def test_viewOptions(self):
        actual = self.myController._viewOptions()

        self.assertEqual(actual, True)
