import pytest

# Определение функции sum
def sum(a, b):
    return a + b

# Определение функции mul
def mul(a, b):
    return a * b

# Определение функции div
def div(a, b):
    return a / b

# Определение функции sub
def sub(a, b):
    return a - b

# Тесты для функции sum
def test_sum_positive_numbers():
    assert sum(3, 5) == 8

def test_sum_negative_numbers():
    assert sum(-3, -5) == -8

def test_sum_mixed_numbers():
    assert sum(3, -5) == -2

# Тесты для функции mul
def test_mul_positive_numbers():
    assert mul(3, 5) == 15

def test_mul_negative_numbers():
    assert mul(-3, -5) == 15

def test_mul_mixed_numbers():
    assert mul(3, -5) == -15

# Тесты для функции div
def test_div_positive_numbers():
    assert div(10, 2) == 5

def test_div_negative_numbers():
    assert div(-10, 2) == -5

def test_div_dividing_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_div_mixed_numbers():
    assert div(15, -3) == -5

# Тесты для функции sub
def test_sub_positive_numbers():
    assert sub(5, 3) == 2

def test_sub_negative_numbers():
    assert sub(-5, -3) == -2

def test_sub_mixed_numbers():
    assert sub(3, -5) == 8
