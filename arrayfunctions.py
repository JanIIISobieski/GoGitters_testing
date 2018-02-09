import numpy as np

def min_max(number_list):
    min_val = np.amin(number_list)
    max_val = np.amax(number_list)
    return min_val, max_val