import os
import unittest

from problems.euler.p0067.main import p0067


class TestP0067(unittest.TestCase):

    def test_p0067(self):
        file_path_str = os.path.realpath(__file__)
        path_str = os.path.dirname(file_path_str)
        self.assertEqual(p0067(os.path.join(path_str, "triangle.txt")), 7273)
