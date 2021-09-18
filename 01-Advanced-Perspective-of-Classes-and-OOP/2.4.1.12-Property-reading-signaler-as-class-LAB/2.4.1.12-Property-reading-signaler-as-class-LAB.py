from __future__ import annotations
from datetime import datetime


class TimestampDecorator:
    """
    Decorator class that prints timestamp before decorated function run
    """
    def __init__(self, own_function):
        """
        Simple initialization
        :param own_function: a function to decorate
        """
        self.func = own_function

    def __call__(self, *args, **kwargs):
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
        return self.func(*args, **kwargs)


@TimestampDecorator
def adder(x: int | float, y: int | float) -> int | float:
    """
    Simple function that adds two numbers (int or float)
    :param x: first number to add (int or float)
    :param y: second number to add (int or float)
    :return: result of addition (int or float)
    """
    return x + y


@TimestampDecorator
def multiplier(x: int | float, y: int | float) -> int | float:
    """
    Simple function that multiplies two numbers (int or float)
    :param x: first number to multiply (int or float)
    :param y: second number to multiply (int or float)
    :return: result of multiplication (int or float)
    """
    return x * y


if __name__ == "__main__":
    print("1 + 2 =", adder(1, 2))
    print("1 * 2 =", multiplier(1, 2))
