import pytest

from Question3 import *

ap789 = Airplane(0, 0, 10, 3000)

def test_go_to():
    assert ap789.goto(95, 70) == True
def test_position():
    assert ap789.position[0] == 95 and ap789.position[1] == 70
def test_fuel_level():
    assert abs(ap789.fuel_level - 1819.96) < 0.01
