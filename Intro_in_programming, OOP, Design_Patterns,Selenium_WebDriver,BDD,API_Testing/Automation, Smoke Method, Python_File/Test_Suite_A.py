import unittest
import FormAuth
import HtmlTestRunner
import TestMultiFile
import HTMLTestRunner


class TestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FormAuth.TestFormAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestMultiFile.TestMultiTab)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_report=True,
            report_title="My report test",
            report_name="Smoke Test"
        )
        runner.run(smoke_test)


