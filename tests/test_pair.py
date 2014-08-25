"""Test cases for module that does pair computation."""

import unittest
from datetime import date, timedelta

import pair as pair_mod


class TestComputePair(unittest.TestCase):

    """Tests for method that actually does the pair-selection computation."""

    def setUp(self):
        """Build Pair object."""
        self.pair_maker = pair_mod.Pair()

    def test_float_day_param(self):
        """The day param must be type day. Try passing a float."""
        with self.assertRaises(TypeError):
            self.pair_maker.compute_pairs(1.)

    def test_never_paired_with_self(self):
        """Try lots of day_diffs, validating no dev is paired with self."""
        for day_diff in range(366):
            day = self.pair_maker.start_day + timedelta(day_diff)
            pairs = self.pair_maker.compute_pairs(day)
            for dev0, dev1 in pairs.iteritems():
                assert dev0 != dev1

    def test_pairwise_pairs(self):
        """Validate that each member of a pair is paired with the other."""
        for day_diff in range(366):
            day = self.pair_maker.start_day + timedelta(day_diff)
            pairs = self.pair_maker.compute_pairs(day)
            for dev0, dev1 in pairs.iteritems():
                assert dev0 == pairs[dev1], "{} != {}, pairs: {}".format(pairs[dev0], pairs[dev1], pairs)


class TestComputeDayDiff(unittest.TestCase):

    """Test method that finds difference between two days."""

    def setUp(self):
        """Build Pair object and example days."""
        # Days with *0 are one week, days with *1 are the next week
        self.pair_maker = pair_mod.Pair()
        self.monday0 = date(2014, 8, 25)
        self.tuesday0 = date(2014, 8, 26)
        self.friday0 = date(2014, 8, 29)
        self.monday1 = date(2014, 9, 1)

    def test_same_day(self):
        """Test passing start and end days that are equal."""
        day_diff = self.pair_maker.compute_day_diff(self.monday0, self.monday0)
        assert day_diff == 0

    def test_today_and_tomorrow(self):
        """Test start day today and end day tomorrow."""
        day_diff = self.pair_maker.compute_day_diff(self.monday0, self.tuesday0)
        assert day_diff == 1

    def test_one_week_diff(self):
        """Test a Monday and the following Monday."""
        day_diff = self.pair_maker.compute_day_diff(self.monday0, self.monday1)
        assert day_diff == 5

    def test_over_weekend(self):
        """Test a Friday and the next Monday."""
        day_diff = self.pair_maker.compute_day_diff(self.friday0, self.monday1)
        assert day_diff == 1

    def test_invalid_order(self):
        with self.assertRaises(ValueError):
            day_diff = self.pair_maker.compute_day_diff(self.tuesday0,
                                                        self.monday0)
