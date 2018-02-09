from arrayfunctions import min_max


def test_minmax():
    x = [1,5,3,9,5,6]
    y = [1.5,3,4,912,10.4,0,0]
    z = [1.239,1.2459,5.6,-5]
    assert min_max(x) == (1,9)
    assert min_max(y) == (0,912)
    assert min_max(z) == (-5,5.6)