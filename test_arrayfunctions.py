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
