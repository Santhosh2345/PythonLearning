import pytest

# Test files should be named test_*.py or *_test.py
# Test functions inside them should be named test_*
def add(a, b):
    return a + b

def test_add():
    assert add(2,2) == 4, "Math is broken!"

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

def test_negative_age_raises_error():
    with pytest.raises(ValueError):
        set_age(-5)