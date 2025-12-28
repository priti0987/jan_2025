def is_even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"


def test_even_number():
    result = is_even_or_odd(4)
    print(f"test for 4 : {result}")


def test_odd_number():
    result = is_even_or_odd(13)
    print(f"test for 13 : {result}")


def test_check():
    result = is_even_or_odd(122666)
    assert result == "Evefn"