import pytest

from Question2 import generate_sentences

def test_generate_sequences1():
    assert generate_sentences(["John", "Mary"], ["hates", "loves"], ["apples", "bananas"]) == "John hates apples. John hates bananas. John loves apples. John loves bananas. Mary hates apples. Mary hates bananas. Mary loves apples. Mary loves bananas."
def test_generate_sequence2():
    assert generate_sentences(["Vlad", "Hubie"], ["drives"], ["car", "motorcycle", "bus"]) == "Hubie drives bus.Hubie drives car. Hubie drives motorcycle.Vlad drives bus.Vlad drives car. Vlad drives motorcycle."