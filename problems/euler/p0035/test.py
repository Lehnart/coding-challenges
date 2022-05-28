import unittest

from problems.euler.p0035.main import p0035


class TestP0035(unittest.TestCase):

    def test_p0035(self):
        self.assertEqual(p0035(), 55)
