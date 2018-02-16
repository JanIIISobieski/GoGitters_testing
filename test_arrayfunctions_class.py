def test_numerical_results():
    from arrayfunctions_class import Array
    from math import isclose
    array1 = Array(array=[0, 5, 20, 21])
    array2 = Array(array=[0, -7, 0])
    array3 = Array(array=[1.2, 1.005, 2.345, 3.298])

    array1.find_sum_all()
    array2.find_sum_all()
    array3.find_sum_all()

    array1.find_extrema()
    array2.find_extrema()
    array3.find_extrema()

    array1.find_max_diff()
    array2.find_max_diff()
    array3.find_max_diff()

    assert array1.sum_all == 46
    assert array2.sum_all == -7
    assert isclose(array3.sum_all, 7.848, abs_tol=10e-9)

    assert array1.extrema == (0, 21)
    assert array2.extrema == (-7, 0)
    assert array3.extrema == (1.005, 3.298)

    assert array1.max_diff == 15
    assert array2.max_diff == [-7, 7]
    assert isclose(array3.max_diff, 1.34, abs_tol=10e-9)


def test_exceptions(capsys):
    from arrayfunctions_class import Array
    array1 = Array(array=[])
    array2 = Array(array=[1, 5, 10, "I'm a number?"])

    array1.find_sum_all()
    out1, err1 = capsys.readouterr()

    array2.find_sum_all()
    out2, err2 = capsys.readouterr()

    array1.find_extrema()
    out3, err3 = capsys.readouterr()

    array2.find_extrema()
    out4, err4 = capsys.readouterr()

    array1.find_max_diff()
    out5, err5 = capsys.readouterr()

    array2.find_max_diff()
    out6, err6 = capsys.readouterr()

    assert array1.sum_all is None
    assert array2.sum_all is None
    assert array1.extrema is None
    assert array2.extrema is None
    assert array1.max_diff is None
    assert array2.max_diff is None

    assert out1 == 'Numerical list must be at least of length 2\n'
    assert out2 == 'Only numerical lists are accepted\n'
    assert out3 == 'Numerical list must be at least of length 2\n'
    assert out4 == 'Only numerical lists accepted\n'
    assert out5 == 'Numerical list must be at least of length 2\n'
    assert out6 == 'Only numerical lists accepted\n'
