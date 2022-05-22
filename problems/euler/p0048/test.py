import unittest

from problems.euler.p0048.main import p0048


class TestP0048(unittest.TestCase):

    def test_p0048(self):
        self.assertEqual(p0048(), 9110846700)
