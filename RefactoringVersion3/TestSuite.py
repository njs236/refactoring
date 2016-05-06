import unittest

from TestCasesBranchCoverage import *

from TestCasesStatementCoverage import *
from Record import *
from RecordCollection import *

if __name__ == '__main__':

    suite1 = TestBranchCoverage()
    suite2 = TestStatementCoverage()
    suite3 = TestRecordClass()
    suite4 = TestRecordCollectionClass()
    unittest.TestSuite((suite1, suite2, suite3, suite4))
    unittest.main()