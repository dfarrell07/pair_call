#!/usr/bin/env python
"""Code for computing team pairs for weekly pair calls."""

import datetime
from datetime import date, timedelta
import sys


class Pair(object):

    """Computes pair of devs that should meet for the current week.

    Uses a simple round robbin algorithm.

    """

    # If you change the dev list, make sure everyone pulls it
    devs = ["Sam", "Chris", "Dave", "Madhu", "Brent", "Flavio", "Daniel"]

    # We started this on 8/17/2014
    start_day = datetime.date(2014, 8, 17)

    def __init__(self):
        """Add a placeholder 'dev' if len(devs) is odd."""
        if len(self.devs) % 2:
            self.devs.append("Day off")

    def build_fixtures(self):
        """Build lists of devs rotated around dev at index zero.

        Note that these lists are apparently called 'fixtures' in
        the lingo of tournament bracket builders. I didn't know this
        as a non-sport person, but it seems pretty well accepted,
        so I'll honor it.

        """
        fixture = list(self.devs)
        fixtures = []
        for i in range(0, len(self.devs) - 1):
            fixtures.append(fixture)
            fixture = [fixture[0]] + [fixture[-1]] + fixture[1:-1]

        return fixtures

    def compute_day_diff(self, start_day, end_day):
        """Find the number of weekdays between the given dates.

        :param start_day: Temporally first day to find diff between.
        :type start_day: date
        :param end_day: Temporally second day to find diff between.
        :type end_day: date

        """
        if not start_day <= end_day:
            err_msg = "Start day ({}) must be before end day ({})".format(
                start_day, end_day)
            sys.stderr.write(err_msg)
            raise ValueError(err_msg)
        daygenerator = (start_day + timedelta(x + 1) for x in xrange((
            end_day - start_day).days))
        day_diff = sum(1 for day in daygenerator if day.weekday() < 5)
        return day_diff

    def compute_pairs(self, day=None):
        """TODO

        TODO: This should take a date

        """
        # If no day given, use today
        # Typically true in production, typically pass day when testing
        if day is None:
            day = date.today()

        # Find number of weekdays since we started these meetings
        day_diff = self.compute_day_diff(self.start_day, day)

        # Fixtures are basically rotations of the dev list
        fixtures = self.build_fixtures()
        # There are len(devs) fixtures, rotate through them based on day
        todays_fixture = fixtures[day_diff % len(fixtures)]
        # Split the fixture in half
        today_first_half_fix = todays_fixture[:len(todays_fixture) / 2]
        # Reverse order of second half to finish classic Round Robin structure
        today_second_half_fix = todays_fixture[len(todays_fixture) / 2:][::-1]

        # Pair off devs in two half fixtures based on indexes
        pairs = {}
        for dev0, dev1 in zip(today_first_half_fix, today_second_half_fix):
            pairs[dev0] = dev1
            pairs[dev1] = dev0
        return pairs


# When run as script
if __name__ == "__main__":
    pair_maker = Pair()
    pairs = pair_maker.compute_pairs()
    print "Your name:",
    dev = raw_input()
    if dev.capitalize() not in pair_maker.devs:
        print "Unknown dev: {}, known devs: {}".format(dev, pair_maker.devs)
        sys.exit(1)
    print "You're paired with: {}".format(pairs[dev])
