import pytest


def test_find_max_diff():
    from arrayfunctions import max_diff
    from math import isclose

    list_1_diff = max_diff([1, 4, 10])
    list_2_diff = max_diff([0, -8, -4, 0, 4, 11])
    list_3_diff = max_diff([7, 7, 7, 7, 7])
    list_4_diff = max_diff([0, 0.1, 0.205, 0.3])
    list_5_diff = max_diff([-7, 0, -7])

    assert list_1_diff == 6
    assert list_2_diff == -8
    assert list_3_diff == 0
    assert isclose(list_4_diff, 0.105, abs_tol=10e-9)
    assert list_5_diff == [-7, 7]


def test_max_diff_exceptions(capsys):
    from arrayfunctions import max_diff

    list1 = max_diff([])
    out1, err1 = capsys.readouterr()

    list2 = max_diff([1])
    out2, err2 = capsys.readouterr()

    list3 = max_diff([0, 1, 2, 'Hello'])
    out3, err3 = capsys.readouterr()

    assert list1 is None
    assert list2 is None
    assert list3 is None
    assert out1 == 'Numerical list must be at least of length 2\n'
    assert out2 == 'Numerical list must be at least of length 2\n'
    assert out3 == 'Only numerical lists accepted\n'


def test_sum_list(capsys):
    from arrayfunctions import sum_list
    sum_1 = sum_list([5])
    sum_2 = sum_list([2, 7])
    sum_3 = sum_list([4, 8.5, 1.2])
    sum_4 = sum_list([-4, 6, -2])
    sum_5 = sum_list([0, 0.6, -1.9, 12.3])

    # exceptions
    sum_6 = sum_list([0, 5, 'Heya'])
    out6, err6 = capsys.readouterr()
    sum_7 = sum_list([])
    out7, err7 = capsys.readouterr()
    sum_8 = sum_list([5, float('inf')])
    out8, err8 = capsys.readouterr()

    assert sum_1 == 5
    assert sum_2 == 9
    assert sum_3 == 13.7
    assert sum_4 == 0
    assert sum_5 == 11

    assert sum_6 is None
    assert sum_7 is None
    assert sum_8 is None
    # 6 raises TypeError, 7 raises TypeError, 8 raises ValueError
    assert out6 == 'Only numerical lists are accepted\n'
    assert out7 == 'Only numerical lists are accepted\n'
    assert out8 == 'Input contains inappropriate value\n'


def test_minmax():
    from arrayfunctions import min_max
    x = [1, 5, 3, 9, 5, 6]
    y = [1.5, 3, 4, 912, 10.4, 0, 0]
    z = [1.239, 1.2459, 5.6, -5]
    assert min_max(x) == (1, 9)
    assert min_max(y) == (0, 912)
    assert min_max(z) == (-5, 5.6)
