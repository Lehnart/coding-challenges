import unittest

from euler import p0001, p0002, p0003, p0004, p0005, p0006, p0007, p0008, p0009


class TestEuler(unittest.TestCase):

    def test_0001(self):
        self.assertEqual(p0001.algo(), 233168)

    def test_0002(self):
        self.assertEqual(p0002.algo(), 4613732)

    def test_0003(self):
        self.assertEqual(p0003.algo(), 6857)

    def test_0004(self):
        self.assertEqual(p0004.algo(), 906609)

    def test_0005(self):
        self.assertEqual(p0005.algo(), 232792560)

    def test_0006(self):
        self.assertEqual(p0006.algo(), 25164150)

    def test_0007(self):
        self.assertEqual(p0007.algo(), 104743)

    def test_0008(self):
        self.assertEqual(p0008.algo(), 23514624000)

