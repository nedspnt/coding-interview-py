# PROBLEM 1: maxmimum zero gap for binary

def maximum_zero_gap(array):  
    """ Given a a number, get the longest zeros (between ones) of its binary

    Args:
        array (list): a list-like object

    Returns:
        num_max_zeros (int): maximum number of zeros between ones
    """

    num_max_zeros = len(max(bin(array)[2:].strip('0').split('1')))

    return num_max_zeros

