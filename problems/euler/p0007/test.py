import unittest

from problems.euler.p0007.main import p0007


class TestP0007(unittest.TestCase):

    def test_p0007(self):
        self.assertEqual(p0007(), 104743)
