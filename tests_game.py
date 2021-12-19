import pytest
from snaki import get_random_apple_position

"""Проверка, чтобы яблоко не появилось за пределами площадки"""

def test_get_random_apple_position():
    assert get_random_apple_position()[0] <= 1545 and get_random_apple_position()[1] <= 765

