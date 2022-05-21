import unittest

from problems.euler.p0009.main import p0009


class TestP0009(unittest.TestCase):

    def test_p0009(self):
        self.assertEqual(p0009(), 31875000)
