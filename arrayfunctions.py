import logging


logging.basicConfig(filename="arrayfunctions.log",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def max_diff(list_input):
    '''Function to find the maximum magnitude difference between
    consecutive elements in a numerical list

    :param list_input: numerical list of at least length 2
    :returns: The maximum magnitude consecutive difference as a scalar,
    or if the magnitude difference was equal in both positive and negative
    directions, both the positive and negative differences as a vector of
    length 2
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
