import logging


logging.basicConfig(filename="arrayfunctions.log",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def max_diff(list_input):
    '''Function to find the maximum magnitude difference between
    consecutive elements in a numerical list

    :param array list_input: numerical list of at least length 2
    :return: The maximum magnitude consecutive difference as a scalar,
        or a vector if equal maximum difference in positive negative directions
    :rtype: scalar or array
    :raises ValueError: if the numerical list input is of length less than 2
    :raises TypeError: if a non-numerical list is given
    :raises ImportError: if a required package was not loaded
    '''

    diff_var = []
    try:
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

        logging.info('Function completed without errors')

    except ValueError:
        print('Numerical list must be at least of length 2')
        logging.warning('Found max diff is of type None')
        maxdiff = None
    except TypeError:
        print('Only numerical lists accepted')
        logging.warning('Found max diff is of type None')
        maxdiff = None
    except ImportError:
        # This file does not use any non-standard python packages like numpy
        print('Missing package... or basic python installation')
        logging.debug('Required package is not installed')
        maxdiff = None

    return maxdiff


def sum_list(list):
    '''Function to find the sum of all elements in a list

    :param  array list: numerical list of at least length 1
    :return: The sum of the elements in list
    :raises ValueError: if infinity is in the input array
    :raises TypeError: if list is empty or contains non-numericals
    :raises ImportError: if a required package was not loaded
    '''
    import numpy as np
    try:
        if(float('inf') in list or float('-inf') in list):
            raise ValueError
        if(len(list) == 0):
            raise TypeError
        sum = np.sum(list)
        logging.info('Function completed without errors')

    except ImportError:
        print('Missing Numpy')
        logging.debug('numpy is not installed')
        sum = None
    except TypeError:
        print('Only numerical lists are accepted')
        logging.warning('sum is None')
        sum = None
    except ValueError:
        print('Input contains inappropriate value')
        logging.warning('sum is None')
        sum = None

    return sum


def min_max(number_list):
    """Finds the minimum and maximum values of a numerical list.

    :param number_list: numerical list of at least 2 elements
    :returns: tuple containing the minimum and maximum values of input list
    :raises ImportError: if numpy is not installed
    :raises TypeError: if a non-numerical list is given
    :raises ValueError: if a numerical list is not of at least length 2
    """
    try:
        import numpy as np
        min_val = np.amin(number_list)
        max_val = np.amax(number_list)
        min_max_out = (min_val, max_val)

        logging.info('Function was completed successfully.')

    except ImportError:
        print('Missing package: numpy')
        logging.debug('Required package numpy is not installed')
        min_max_out = None
    except TypeError:
        print('Only numerical lists accepted')
        logging.warning('Min/max is not numerical list')
        min_max_out = None
    except ValueError:
        print('Numerical list must be at least of length 1')
        logging.warning('Min/max not length 1')
        min_max_out = None

    return min_max_out
