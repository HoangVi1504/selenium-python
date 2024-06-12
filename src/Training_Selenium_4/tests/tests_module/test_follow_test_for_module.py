import unittest
from abc import ABC

from src.Training_Selenium_4.tests.tests_module.base_test_for_module import BaseTestForModule

def setUpModule():
    print('\nHello, I am setUp this module tests_module')


def tearDownModule():
    print('\nHello, I am tearDown this module tests_module')


class TestFollowTestForClass(BaseTestForModule, ABC):

    def _setUp(self):
        print('\nHello, I override _setup method')

    def _tearDown(self):
        print('\nHello, I override _tearDown method')

    def test_something(self):
        print('\nHello, I am testing something')
        x = "this"
        assert "h" in x

    def test_with_self_assert(self):
        print('\nHello, I am testing but with self Assert')
        x = "that"
        self.assertIn("a", x)

