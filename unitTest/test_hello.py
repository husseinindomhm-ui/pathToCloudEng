from hello import hello


def test_default_hello():
    assert hello() == "Hello to world"

def test_hello():
    assert hello("Hussein") == "Hello to Hussein"