import pytest
from Question4 import *

assert longest_sequence("dghhhmhmx") == ("h", 3)
assert longest_sequence("dhkkhhkkkt") == ("k", 3)
assert longest_sequence("abbbadddadd") == ("b", 3)