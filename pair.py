#!/usr/bin/env python
""""""

import datetime
import sys

# If you change the dev list, make sure everyone pulls it
devs = ["Sam", "Chris", "Dave", "Madhu", "Brent", "Flavio", "Daniel"]

# We started this on 8/13/2014
start_day = datetime.date(2014, 8, 11)


class Pair(object):

    """"""

    def __init__(self):
        """"""
        week_diff = (datetime.date.today() - start_day).days / 7

    def compute_pair(self, usr):
        """"""
        # Make sure first letters is cap and rest are lowercase
        usr = usr.capitalize()

        if usr not in devs:
            err_msg = "Couldn't find {}. Known names: {}".format(usr, devs)
            sys.stderr.write(err_msg)
            raise ValueError(err_msg)

# When run as script
if __name__ == "__main__":
    pair = Pair()
    print "Your name: ",
    usr = raw_input()
    pair.compute_pair(usr)
