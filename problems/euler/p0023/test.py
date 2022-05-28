import unittest

from problems.euler.p0023.main import p0023


class TestP0023(unittest.TestCase):

    def test_p0023(self):
        self.assertEqual(p0023(), 4179871)
