import unittest
from problems.euler.p0014.main import p0014


class TestP0014(unittest.TestCase):

    def test_p0014(self):
        self.assertEqual(p0014(), 837799)
