"""Test cases for module that does pair computation."""

import unittest
from datetime import date, timedelta

import pair as pair_mod


class TestPair(unittest.TestCase):

    """Test Pair object constructor."""

    def test_odd_number_devs(self):
        """Build Pair object with odd number of devs, should be made even."""
        pair_mod.Pair.devs = ["dev1", "dev2", "dev3"]
        pair_maker = pair_mod.Pair()
        assert len(pair_maker.devs) == 4

    def test_even_number_devs(self):
        """Build Pair object with an even number of devs, should stay even."""
        pair_mod.Pair.devs = ["dev1", "dev2"]
        pair_maker = pair_mod.Pair()
        assert len(pair_maker.devs) == 2


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
                assert dev0 == pairs[dev1], "{} != {}, pairs: {}".format(
                    pairs[dev0], pairs[dev1], pairs)


class TestComputeDayDiff(unittest.TestCase):

    """Test method that finds difference between two days."""

    def setUp(self):
        """Build Pair object and example days."""
        self.pair_maker = pair_mod.Pair()
        # Days with *0 are one week, days with *1 are the next week
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
        day_diff = self.pair_maker.compute_day_diff(self.monday0,
                                                    self.tuesday0)
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
        """Pass a start day that's after the end day."""
        with self.assertRaises(ValueError):
            day_diff = self.pair_maker.compute_day_diff(self.tuesday0,
                                                        self.monday0)


class TestBuildFixtures(unittest.TestCase):

    """Test method that builds list of fixtures."""

    def setUp(self):
        """Build Pair object."""
        self.pair_maker = pair_mod.Pair()

    def test_type(self):
        """Confirm that fixtures object is of type list."""
        fixtures = self.pair_maker.build_fixtures()
        assert type(fixtures) is list

    def test_rotate_around_index_zero(self):
        """Confirm that list is rotating around dev at index zero."""
        fixtures = self.pair_maker.build_fixtures()
        dev_at_zero = fixtures[0][0]
        for fixture in fixtures:
            assert dev_at_zero == fixture[0]
