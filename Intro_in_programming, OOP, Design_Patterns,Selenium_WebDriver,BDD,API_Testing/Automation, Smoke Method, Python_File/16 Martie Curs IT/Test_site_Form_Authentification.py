import unittest

import FormAuth
import TestMultiFile

import HtmlTestRunner


class TestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FormAuth.TestFormAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestMultiFile.TestMultiTab)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='My reports',
            report_name='Smoke Test',
        )
        runner.run(smoke_test)


