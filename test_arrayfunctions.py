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
	

def test_sum_list():
	from arrayfunctions import sum_list
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


def test_minmax():
	from arrayfunctions import min_max
    x = [1, 5, 3, 9, 5, 6]
    y = [1.5, 3, 4, 912, 10.4, 0, 0]
    z = [1.239, 1.2459, 5.6, -5]
    assert min_max(x) == (1, 9)
    assert min_max(y) == (0, 912)
    assert min_max(z) == (-5, 5.6)
