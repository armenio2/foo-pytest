import re


def func(txt):
    str = txt
    x = re.sub("a", "", str)
    return x


def test_answer():
    assert func("aloha") == "loh"
