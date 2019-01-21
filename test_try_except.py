def func(x):
    try:
        x = str(x)
        return x
    except:
        x = str("An exception occurred")
        return x


def test_answer():
    assert func("Aloha") == "Aloha"

    y = True
    assert func(y) == "An exception occurred"
