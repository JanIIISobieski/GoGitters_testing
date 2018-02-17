import logging


logging.basicConfig(filename="arrayfunctions.log",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Array:
    '''Class to describe the numerical contents of the array

    :attribute sum_all (int or float): the sum of all the elements in the array
    :attribute extrema (tuple): the minimum and maximum elements in the array
    :attribute max_diff (int, float, or array): the maximum mangnitude
        difference between consecutive element in array
    '''
    def __init__(self,
                 array=[1, 6, 8, 9],
                 sum_all=None,
                 extrema=None,
                 max_diff=None):
        '''__init__ method of the Array class

        :param array (int or float, default=[1, 6, 8, 9]): numerical array of
            at least length 2
        :param sum_all (int or float, optional, default=None): the sum of all
            element in array
        :param extrema (tuple, optional, default=None): the minimum and maximum
            elements in array
        :param max_diff (int, float, or array, optional, default=None): the
            maximum magnitude difference between consecutive elements in array
        '''
        self.array = array
        self.sum_all = sum_all
        self.extrema = extrema
        self.max_diff = max_diff

    def find_max_diff(self):
        '''Method to find the maximum difference between consecutive elements

        :return: The maximum magnitude consecutive difference as a scalar,
            or a vector if equal maximum difference in positive negative
            directions
        :rtype: int, float, or array
        :raises ValueError: if the numerical list input is of length less than
            2
        :raises TypeError: if a non-numerical list is given
        :raises ImportError: if a required package was not loaded
        '''
        diff_var = []
        try:
            for i in range(0, len(self.array)-1):
                diff_var.append(self.array[i+1] - self.array[i])

            if abs(max(diff_var)) > abs(min(diff_var)):
                maxdiff = max(diff_var)
            elif abs(max(diff_var)) < abs(min(diff_var)):
                maxdiff = min(diff_var)
            elif max(diff_var) == min(diff_var):
                maxdiff = max(diff_var)
            else:
                maxdiff = [min(diff_var), max(diff_var)]

            logging.info('max_diff() completed without errors')

        except ImportError:
            # This file does not use any non-standard python packages
            print('Missing package... or basic python installation')
            logging.debug('Required package is not installed')
            maxdiff = None
        except TypeError:
            print('Only numerical lists accepted')
            logging.warning('Found max diff is of type None')
            maxdiff = None
        except ValueError:
            print('Numerical list must be at least of length 2')
            logging.warning('Found max diff is of type None')
            maxdiff = None

        self.max_diff = maxdiff

    def find_extrema(self):
        '''Finds the minimum and maximum values of a numerical list.

        :return: tuple containing the minimum and maximum values of input list
        :rtype: tuple
        :raises ImportError: if numpy is not installed
        :raises TypeError: if a non-numerical list is given
        :raises ValueError: if a numerical list is not of at least length 2
        '''
        try:
            from numpy import amin, amax
            if(len(self.array) < 2):
                raise ValueError
            min_val = amin(self.array)
            max_val = amax(self.array)
            min_max_out = (min_val, max_val)

            logging.info('find_extrema() completed successfully.')

        except ImportError:
            print('Missing package: numpy')
            logging.debug('Required package numpy is not installed')
            min_max_out = None
        except TypeError:
            print('Only numerical lists accepted')
            logging.warning('Only numerical lists accepted')
            min_max_out = None
        except ValueError:
            print('Numerical list must be at least of length 2')
            logging.warning('Numerical list must be at least of length 2')
            min_max_out = None

        self.extrema = min_max_out

    def find_sum_all(self):
        '''Method to find the sum of all the elements in an array

        :return: The sum of the elements in list
        :rtype: int or float
        :raises ValueError: if infinity is in the input array
        :raises TypeError: if list is empty or contains non-numericals
        :raises ImportError: if a required package was not loaded
        '''
        from numpy import sum
        try:
            if(len(self.array) < 2):
                raise ValueError
            sumall = sum(self.array)

            logging.info('sum_all() completed without errors')

        except ImportError:
            print('Missing numpy')
            logging.debug('numpy is not installed')
            sumall = None
        except TypeError:
            print('Only numerical lists are accepted')
            logging.warning('Found sum is of type None')
            sumall = None
        except ValueError:
            print('Numerical list must be at least of length 2')
            logging.warning('Found sum is of type None')
            sumall = None

        self.sum_all = sumall
