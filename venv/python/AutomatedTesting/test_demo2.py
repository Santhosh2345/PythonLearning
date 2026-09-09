def multiply(a, b):
    return a/b

def test_multiply():
    assert multiply(1,5), "Math is broken at first assert!"
    assert multiply(1, 2)

def test_multiply2():
    assert multiply(2, 2)