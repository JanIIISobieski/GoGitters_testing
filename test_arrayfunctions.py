import numpy
from arrayfunctions import sum_list


def test_sum_list():
    sum_1 = sum_list([5])
    sum_2 = sum_list([2, 7])
    sum_3 = sum_list([4, 8.5, 1.2])
    sum_4 = sum_list([-4, 6, -2])
    sum_5 = sum_list([0, 0.6, -1.9, 12.3])

    assert sum_1 == 5
    assert sum_2 == 9
    assert sum_3 == 13.7
    assert sum_4 == 0
    assert sum_5 == 11
