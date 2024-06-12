import os
import unittest
from abc import abstractmethod

from dotenv import load_dotenv

# load_dotenv()

class BaseTestForClass(unittest.TestCase):

    @abstractmethod
    def _setUp(self):
        pass

    @abstractmethod
    def _tearDown(self):
        pass

    def setUp(self):
        print('\nHello, I am setup function and I call _setUp')
        self._setUp()
        # print(os.environ['HEHE'])

    def tearDown(self):
        print('\nHello, I am tearDown function and I call _tearDown')
        self._tearDown()

    @classmethod
    def setUpClass(cls):
        print('\nHello, I am setup class')
        print('Increase stock to 100')

    @classmethod
    def tearDownClass(cls):
        print('\nHello, I am tearDown class')
