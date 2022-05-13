import unittest

import HtmlTestRunner

import FormAuth
import TestMultiFile


class TestSuits(unittest.TestCase):

    def test_suits(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FormAuth.TestFormAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestMultiFile.TestMultiTab)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test Report",
            report_name="Smoke Test"
        )
        runner.run(smoke_test)


