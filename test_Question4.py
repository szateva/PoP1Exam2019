import pytest
from Question4 import *

def test_longest_sequence1():
    assert longest_sequence("dghhhmhmx") == ("h", 3)

def test_longest_sequence2():
    assert longest_sequence("dhkkhhkkkt") == ("k", 3)

def test_longest_sequence3():
    assert longest_sequence("abbbadddadd") == ("b", 3)