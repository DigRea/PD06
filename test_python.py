import math

def test_filter_function():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(filter(lambda x: x % 2 == 0, numbers))
    assert result == [2, 4, 6, 8, 10]

def test_map_function():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * 2, numbers))
    assert result == [2, 4, 6, 8, 10]

def test_sorted_function():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = sorted(numbers)
    assert result == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_math_pi():
    assert math.isclose(math.pi, 3.141592653589793, abs_tol=1e-10)

def test_math_sqrt():
    result = math.sqrt(25)
    assert result == 5.0

def test_math_pow():
    result = math.pow(2, 3)
    assert result == 8.0

def test_math_hypot():
    result = math.hypot(3, 4)
    assert result == 5.0
