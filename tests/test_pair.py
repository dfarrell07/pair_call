""""""

import unittest
import pair as pair_mod

class TestComputePair(unittest.TestCase):

    """"""

    def setUp(self):
        """"""
        self.pair = pair_mod.Pair()

    def test_unknown_dev(self):
        """"""
        with self.assertRaises(ValueError):
            self.pair.compute_pair("not_a_dev")
