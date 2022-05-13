import unittest
from unittest import runner

import FormAuth
import HtmlTestRunner
import TestFormAuth
import TestMultiFile


class TestSuite(unittest.TestCase):
    def test(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(FormAuth.TestFormAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestMultiFile.TestMultiTab),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            reports_title="My_reports",
            report_name="Smoke_Test"
        )

        runner.run(smoke_test)


