import unittest

from problems.euler.p0016.main import p0016


class TestP0016(unittest.TestCase):

    def test_p0016(self):
        self.assertEqual(p0016(), 1366)
