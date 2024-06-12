import unittest
from abc import abstractmethod


class BaseTestForModule(unittest.TestCase):

    @abstractmethod
    def _setUp(self):
        pass

    @abstractmethod
    def _tearDown(self):
        pass

    def setUp(self):
        print('\nHello, I am setup function and I call _setUp')
        self._setUp()

    def tearDown(self):
        print('\nHello, I am tearDown function and I call _tearDown')
        self._tearDown()

    @classmethod
    def setUpClass(cls):
        print('\nHello, I am setup class')

    @classmethod
    def tearDownClass(cls):
        print('\nHello, I am tearDown class')
