from __future__ import annotations

import random


class Apple:
    """
    Class representing an apple
    """
    __lower_limit = 0.2  # lower limit for weight
    __upper_limit = 0.5  # upper limit for weight

    def __init__(self):
        """
        Creates apple with random weight
        """
        self._weight = Apple.next_apple_weight()
        print(f"Apple created with wight {self._weight}")

    @classmethod
    def next_apple_weight(cls) -> float:
        """
        Helps to choose random wight for next apple.
        :return: random float between __lower_limit and __upper_limit
        """
        return random.uniform(cls.__lower_limit, cls.__upper_limit)

    @property
    def weight(self):
        return self._weight


class ApplePackage:
    __total_weight = 0.0
    __total_number = 0
    __max_weight = 1000

    @classmethod
    def create_apple_and_stash(cls) -> Apple | None:
        """
        Creates apple and tries to add it to stash
        If overweight achieved -> returns None and reports totals; else returns Apple()
        """
        apple = Apple()
        if cls.check_apple(apple):
            cls.add_apple(apple)
        else:
            cls.print_report()
            return None
        return apple

    @classmethod
    def print_report(cls):
        """
        Prints report about totals: __total_number, __total_weight
        """
        print(f"Apples created: {cls.__total_number}")
        print(f"Total weight: {cls.__total_weight}")

    @classmethod
    def check_apple(cls, apple: Apple) -> bool:
        """
        Checks overweight
        :return: False if overweight else True
        """
        return True if cls.__total_weight + apple.weight <= cls.__max_weight else False

    @classmethod
    def add_apple(cls, apple: Apple):
        """
        Simulates stashing next apple.
        Increments totals: __total_number, __total_weight
        """
        cls.__total_weight += apple.weight
        cls.__total_number += 1

    @classmethod
    def get_total_weight(cls) -> float:
        """
        :return: __total_weight
        """
        return cls.__total_weight

    @classmethod
    def get_total_number(cls) -> int:
        """
        :return: __total_number
        """
        return cls.__total_number

    @classmethod
    def reset(cls):
        """
        Resets totals to zero: __total_number, __total_weight
        """
        cls.__total_weight = 0.0
        cls.__total_number = 0


if __name__ == "__main__":
    while True:
        new_apple = ApplePackage.create_apple_and_stash()
        if new_apple is None:
            break
