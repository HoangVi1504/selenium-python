import unittest


class TestLifeCycle(unittest.TestCase):

    def setUp(self):
        print('\nHello, I am setup function')
        self.test = 2

    def tearDown(self):
        print('\nHello, I am tearDown function')
        self.test = 2

    def test_something(self):
        print('\nHello, I am testing something')
        x = "this"
        self.test = 3
        print(self.test)
        assert "h" in x

    def test_with_self_assert(self):
        print('\nHello, I am testing but with self Assert')
        x = "that"
        print(self.test)
        self.assertIn("a", x)
