#!/usr/bin/python3
def raise_exception_msg(message=""):
    """raisees a name exception"""
    try:
        raise NameError

    except NameError:
        print("C is fun")
