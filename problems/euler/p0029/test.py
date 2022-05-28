import unittest

from problems.euler.p0029.main import p0029


class TestP0029(unittest.TestCase):

    def test_p0029(self):
        self.assertEqual(p0029(), 9183)
