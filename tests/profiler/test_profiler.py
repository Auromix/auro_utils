import unittest
from auro_utils.profiler import auro_profiler
import time


class TestProfiler(unittest.TestCase):
    def setUp(self):
        self.state = 0

    @staticmethod
    @auro_profiler
    def test_profiler_decorator_for_static_method():
        time.sleep(1)

    @auro_profiler
    def test_profiler_decorator_for_method(self):
        time.sleep(1)
        self.state = 1

    def test_state_after_method(self):
        self.test_profiler_decorator_for_method()
        self.assertEqual(self.state, 1)


if __name__ == '__main__':
    unittest.main()
