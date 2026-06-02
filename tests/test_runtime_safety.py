def test_python_int_arbitrary_precision_guard():
    a = 2**130 + 123456789
    b = 2**97 + 987654321
    assert (a + b) - b == a
    assert (a * b) // b == a
