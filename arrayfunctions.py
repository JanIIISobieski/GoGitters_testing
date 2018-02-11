def max_diff(list_input):
    diff_var = []

    for i in range(0, len(list_input)-1):
        diff_var.append(list_input[i+1] - list_input[i])

    if abs(max(diff_var)) > abs(min(diff_var)):
        maxdiff = max(diff_var)
    elif abs(max(diff_var)) < abs(min(diff_var)):
        maxdiff = min(diff_var)
    elif max(diff_var) == min(diff_var):
        maxdiff = max(diff_var)
    else:
        maxdiff = [min(diff_var), max(diff_var)]

    return maxdiff

def sum_list(list):
	import numpy as np
    return np.sum(list)

def min_max(number_list):
	import numpy as np
    min_val = np.amin(number_list)
    max_val = np.amax(number_list)
    minmax_out = (min_val, max_val)
    return minmax_out
