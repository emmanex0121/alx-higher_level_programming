#!/usr/bin/python3
""" module add_integer """


def add_integer(a, b=98):
    """Function That Adds the integer arguments."""
    def is_not_number(n):
    	"""Function that checks type"""
    	if isinstance(n, int) or isinstance(n,float):
    		return False
    	return True

    if is_not_number(a):
        raise TypeError("a must be an integer")
    if is_not_number(b):
        raise TypeError("b must be an integer")
    	
    return (int(a) + int(b))


