# Unit Testing and Continuous Integration with Travis CI


## `max_diff(list)`
The function takes a numerical list as input.
The list must have at least two elements.

### Output
1. The maximum difference between consecutive elements is defined as the
highest magnitude difference.

  For example, in the list [0, -10, -5], the maximum difference output
by the function will be -10 rather than 5, since the magnitude of -10 is
greater than that of 5. The list [0, -2, 5] will return 7, since that is
the largest magnitude difference.

2. If there is an equal magnitude difference in the positive and negative directions,
both differences will be returned.

  For example, the list [0, -7, 0] will return both -7 and 7.