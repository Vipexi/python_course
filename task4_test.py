#! /usr/bin/python3

import task4
import mock

def test_side_calculation():
    assert task4.side_calculation([7,7]) == 10
    assert task4.side_calculation([10,7]) == 7
   