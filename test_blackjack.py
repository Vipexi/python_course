#! /usr/bin/python3

import blackjack
import mock
#Examples for a test function
def test_calculate_hand():
    #Here we can create different test cases.
    assert blackjack.calculate_hand([2,10]) == 12
    assert blackjack.calculate_hand([1,10]) == 21

# Next, define test
def test_ask_if_player_wants_card():
    # This line replaces user input, with pre defined value.
    with mock.patch('builtins.input', return_value="yes"):
        # Then the normal assert line.
        assert blackjack.ask_if_player_wants_card([10,10]) == "yes"


def test_print_hands(capsys):
    blackjack.print_hands([1,4],[8,4])
    captured= capsys.readouterr()
    assert captured.out == 'Dealer has [1, 4]\nPlayer has [8, 4]\n'

def test_make_a_new_deck():
    assert len(blackjack.make_a_new_deck()) == 52