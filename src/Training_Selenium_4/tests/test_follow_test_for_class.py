from abc import ABC

from tests.base_test_for_class import BaseTestForClass


class TestFollowTestForClass(BaseTestForClass, ABC):

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
