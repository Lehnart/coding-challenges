import unittest

from problems.euler.p0036.main import p0036


class TestP0036(unittest.TestCase):

    def test_p0036(self):
        self.assertEqual(p0036(), 872187)
