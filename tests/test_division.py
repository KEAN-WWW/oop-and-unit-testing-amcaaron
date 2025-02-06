""" TEST DIVISION """
import pytest
from app.division import divide

def test_division():
    """ TEST DIVISION """
    result = divide(9, 3)
    assert result == 3

def test_divide_zero_exception():
    """ TEST DIVISION """
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)
