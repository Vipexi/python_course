#! /usr/bin/python3

import blackjack
#Examples for a test function
def test_calculate_hand():
    #Here we can create different test cases.
    assert blackjack.calculate_hand([2,10]) == 12
    assert blackjack.calculate_hand([1,10]) == 21