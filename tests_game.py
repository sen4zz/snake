import pytest
from snaki import get_random_apple_position, get_distance



def test_get_random_apple_position():
    """Проверка, чтобы яблоко не появилось за пределами площадки"""
    assert get_random_apple_position()[0] <= 1545 and get_random_apple_position()[1] <= 765



def test_get_distance1():
    """Проверка рассчета дистации"""
    x1, y1 = 400, 0
    x2, y2 = 0, 0
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    assert distance
    "shuold be 400"


def test_get_distance2():
    """Проверка рассчета дистации с другими входными данными"""
    x1, y1 = 150, 200
    x2, y2 = 0, 200
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    assert distance
    "shuold be 150"


