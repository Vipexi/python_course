#! /usr/bin/python3

import taskfour
import mock

def test_sided_calculation():
    assert taskfour.side_calculation([11,11,15.56])
    assert taskfour.side_calculation([12,12,16.97])
    assert taskfour.side_calculation([5,7,8.6])