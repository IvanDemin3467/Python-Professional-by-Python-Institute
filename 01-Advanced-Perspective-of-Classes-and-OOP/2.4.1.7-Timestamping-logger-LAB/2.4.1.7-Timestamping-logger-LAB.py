from __future__ import annotations
from datetime import datetime


def timestamp_decorator(given_function):
    """
    Decorator that prints timestamp before decorated function run
    :param given_function: a function to decorate
    :return: decorated function
    """
    def internal_wrapper(*args, **kwargs):
        """
        Prints timestamp and calls decorated function
        :param args: all position arguments of decorated function
        :param kwargs: all keyword arguments of decorated function
        :return: result of decorated function call
        """
        # get current time using now() method
        timestamp = datetime.now()
        # convert timestamp to human-readable string, following passed pattern:
        string_timestamp = timestamp.strftime("Timestamp: %Y-%m-%d %H:%M:%S")
        print(string_timestamp)
        return given_function(*args, **kwargs)

    return internal_wrapper


@timestamp_decorator
def adder(x: int | float, y: int | float) -> int | float:
    """
    Simple function that adds two numbers (int or float)
    :param x: first number to add (int or float)
    :param y: second number to add (int or float)
    :return: result of addition (int or float)
    """
    return x + y


@timestamp_decorator
def multiplier(x: int | float, y: int | float) -> int | float:
    """
    Simple function that multiplies two numbers (int or float)
    :param x: first number to multiply (int or float)
    :param y: second number to multiply (int or float)
    :return: result of multiplication (int or float)
    """
    return x * y


if __name__ == "__main__":
    print(adder(1, 2))
    print(multiplier(1, 2))
