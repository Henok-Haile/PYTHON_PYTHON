# doctest_tracebacks.py

def this_raises():
    """This function always raises an exception.
    
    >>> this_raises()
    Traceback (most recent call last):
        file "<stdin>", line 1, in <module>
        File "/no/such/path/doctest_tracebacks.py", line 14, in
        this_raises
            raise RuntimeError('heree is the error')
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')