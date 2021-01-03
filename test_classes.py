#! /usr/bin/python3

import mock
import classes_goofing

def test_my_car(capsys):
    car_object = testing.Car( 1450,4,"ford","mondeo")
    car_object.my_car()
    captured = capsys.readouterr()
    assert captured.out == "manufacturer : ford\nmodel : mondeo\nweight : 1450\ndoors : 4"