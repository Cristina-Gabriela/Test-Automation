import unittest

import HtmlTestRunner

import FormAuth
import TestMultiFile


class TestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FormAuth.TestFormAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestMultiFile.TestMultiTab)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="MyTestReport",
            report_name="SmokeTest"
        )
        runner.run(smoke_test)


