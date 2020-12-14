# 12/09/2020
# Dev: Cody Yarger
# Exercise 2.4: Fibonacci Series

#===============================================================================
def fibonacci(n):
    """The fibonacci function is passed the argument n and returns the nth value
    of the Fibonacci series"""
    # Base case for n = 0 and 1.
    if n <= 1:
        return n
    # Recursive case for n > 1.
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))

#===============================================================================
def lucas(n):
    """The lucas function is passed the argument n and returns the nth value
    of the Lucas series"""
    # Base case for n = 2 and 1.
    if n == 0:
        return 2
    elif n == 1:
        return 1
    # Recursive case for n > 1.
    else:
        return(lucas(n - 1) + lucas(n - 2))

#===============================================================================
def sum_series(n, n0 = 0, n1 = 1):
    """The sum_series function is passed three arguments n, n0 and n1. The
    default values for n0 and n1 are 0 and 1 resulting in sum_series returning
    the nth value of the Fibonacci series. If optional arguments n0 and n1 are
    assigned 2 and 1 respectively, the nth value of the Lucas series is returned.
    Other values of n0 and n1 return the nth value of other series."""

    # if n0 = 0 and n1 = 1 compute nth value of Fibonacci series.
    if n0 == 0 and n1 == 1:
        # Base case for Fibonacci series.
        if n <= 1:
            return n
        # Recursive case for Fibonacci series n > 1.
        else:
            return(sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1))

    # if n0 = 2 and n1 = 1 compute nth value of Lucas series.
    elif n0 == 2 and n1 == 1:
        # Base case for Lucas series.
        if n == 0:
            return 2
        elif n == 1:
            return 1
        # Recursive case for Lucas series n > 1.
        else:
            return(sum_series(n - 1, n0, n1) + sum_series(n - 2, n0 , n1))

    # else compute nth value of Other series.
    else:
        # Base case for Other series.
        if n == 0:
            return n0
        elif n == 1:
            return n1
        # Recursive case for Other series n > 1.
        else:
            return(sum_series(n - 1, n0, n1) + sum_series(n - 2, n0 , n1))

#===============================================================================
# Assert tests check if a condition is True. If the condition fails, assert
# raises an AssertionError. Optional error message has been omitted from tests.
if __name__ == "__main__":

    # Test Fibonacci function
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # Test Lucas function
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7


    # Test that sum_series matches Fibonacci
    assert sum_series(5) == fibonacci(5)
    assert sum_series(7, 0, 1) == fibonacci(7)

    # Test if sum_series matched Lucas
    assert sum_series(5, 2, 1) == lucas(5)

    # Test if sum_series works for arbitrary initial values (Other series)
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
