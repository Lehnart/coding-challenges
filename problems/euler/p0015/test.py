import unittest
from problems.euler.p0015.main import p0015


class TestP0015(unittest.TestCase):

    def test_p0015(self):
        self.assertEqual(p0015(), 137846528820)
