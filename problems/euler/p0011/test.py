import os
import unittest

from problems.euler.p0011.main import p0011


class TestP0011(unittest.TestCase):

    def test_p0011(self):
        file_path_str = os.path.realpath(__file__)
        path_str = os.path.dirname(file_path_str)
        self.assertEqual(p0011(os.path.join(path_str, "grid.txt")), 70600674)
