import logging


logging.basicConfig(filename="arrayfunctions.log",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Array:

    def __init__(self,
                 array=[1, 6, 8, 9],
                 sum_all=None,
                 extrema=None,
                 max_diff=None):
        self.array = array
        self.sum_all = sum_all
        self.extrema = extrema
        self.max_diff = max_diff

    def find_max_diff(self):
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
