import unittest

from TestCasesBranchCoverage import *

from TestCasesStatementCoverage import *

if __name__ == '__main__':

    suite1 = TestBranchCoverage()
    suite2 = TestStatementCoverage()
    unittest.TestSuite((suite1, suite2))
    unittest.main()