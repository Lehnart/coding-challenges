import unittest

from euler import p0001, p0002, p0003, p0004, p0005, p0006, p0007, p0008, p0009, p0010, p0011, p0012, p0013, p0014, \
    p0015, p0016, p0017


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

    def test_0009(self):
        self.assertEqual(p0009.algo(), 31875000)

    def test_0010(self):
        self.assertEqual(p0010.algo(), 142913828922)

    def test_0011(self):
        self.assertEqual(p0011.algo(), 70600674)

    def test_0012(self):
        self.assertEqual(p0012.algo(), 76576500)

    def test_0013(self):
        self.assertEqual(p0013.algo(), 5537376230)

    def test_0014(self):
        self.assertEqual(p0014.algo(), 837799)

    def test_0015(self):
        self.assertEqual(p0015.algo(), 137846528820)

    def test_0016(self):
        self.assertEqual(p0016.algo(), 1366)

    def test_0017(self):
        self.assertEqual(p0017.algo(), 21124)