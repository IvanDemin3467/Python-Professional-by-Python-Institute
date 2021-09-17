class TypeChecker:
    """
    This is a descriptor that checks whether the value of the instance variable "name" is of type "value_type"
    """
    def __init__(self, name: str, value_type: type):
        """
        Saves "name" and "value_type" during init
        :param name: string, containing the name of the variable to check
        :param value_type: type of the variable to check
        """
        self.name = name
        self.value_type = value_type

    def __set__(self, instance: type, value: object) -> None:
        """
        Checks the type of a variable in an instance
        :param instance: the instance in which the variable is checked
        :param value: the value of the variable to be checked
        :return: None; saves variable in __dict__ of instance
        """
        if isinstance(value, self.value_type):
            instance.__dict__[self.name] = value
        else:
            raise TypeError(f"'{self.name}' {value} must be {self.value_type}")

    def __get__(self, instance, class_):
        """
        Returns the value of a variable from instance
        :param instance: the instance in which the variable is stored
        :param class_: unused parameter, representing class of the instance
        :return: value of the requested variable
        """
        return instance.__dict__[self.name]


class Helpers:
    """
    Provides some helpers to convert time-related values
    """
    @staticmethod
    def sec_to_time(seconds: int) -> tuple:
        """
        Converts seconds into (hours, minutes, seconds)
        :param seconds: integer seconds variable to convert
        :return: dict of integers: (hours, minutes, seconds)
        """
        hours = seconds // 3600
        seconds = seconds % 3600
        minutes = seconds // 60
        seconds = seconds % 60
        return hours, minutes, seconds

    @staticmethod
    def time_to_sec(hours: int, minutes: int, seconds: int) -> int:
        """
        Converts integers of (hours, minutes, seconds) into seconds
        :param hours: integer value of hours to be converted
        :param minutes: integer value of minutes to be converted
        :param seconds: integer value of seconds to be converted
        :return: integer value of total seconds
        """
        return hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def time_to_str(hours: int, minutes: int, seconds: int) -> str:
        """
        Formats tuple of integers (hours, minutes, seconds) into string 'HH:MM:SS'
        :param hours: integer value of hours to be formatted
        :param minutes: integer value of minutes to be formatted
        :param seconds: integer value of seconds to be formatted
        :return: formatted string 'HH:MM:SS'
        """
        return f"{Helpers.int_to_str(hours)}:{Helpers.int_to_str(minutes)}:{Helpers.int_to_str(seconds)}"

    @staticmethod
    def int_to_str(value: int) -> str:
        """
        Formats single integer into string 'XX', where X is a digit
        :param value: integer to be formatted
        :return: string of format 'XX', where X is a digit
        """
        if value // 10 == 0:
            return str(f"0{value}")
        else:
            return str(value)


class TimeInterval:
    """
    Class representing time interval
    Implements methods to store, format, add, subtract and multiply time intervals
    """
    hours = TypeChecker("hours", int)
    minutes = TypeChecker("minutes", int)
    seconds = TypeChecker("seconds", int)

    def __init__(self, hours: int, minutes: int, seconds: int):
        """
        Saves parameters for future processing
        Also calculates total amount of seconds in a given time interval
        :param hours: integer value of hours to be stored
        :param minutes: integer value of minutes to be stored
        :param seconds: integer value of seconds to be stored
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = Helpers.time_to_sec(self.hours, self.minutes, self.seconds)

    def __str__(self) -> str:
        """
        Formats self into human-readable-string
        :return: formatted string 'HH:MM:SS'
        """
        return Helpers.time_to_str(self.hours, self.minutes, self.seconds)

    def __add__(self, other) -> str:
        """
        Adds self to an other time interval
        If other is integer -> adds it to itself as the amount of seconds
        :param other: another TimeInterval to be added (or integer)
        :return: result of summation as formatted string 'HH:MM:SS'
        """
        if type(other) == int:
            new_time_interval = TimeInterval(hours=0, minutes=0, seconds=other)
        else:
            new_time_interval = other
        total_seconds = self.total_seconds + new_time_interval.total_seconds
        hours, minutes, seconds = Helpers.sec_to_time(total_seconds)
        return Helpers.time_to_str(hours, minutes, seconds)

    def __sub__(self, other) -> str:
        """
        Subtracts other time interval from self
        If other is integer -> subtracts it from itself as the amount of seconds
        :param other: another TimeInterval to be subtracted (or integer)
        :return: result of subtraction as formatted string 'HH:MM:SS'
        """
        if type(other) == int:
            new_time_interval = TimeInterval(hours=0, minutes=0, seconds=other)
        else:
            new_time_interval = other
        total_seconds = self.total_seconds - new_time_interval.total_seconds
        hours, minutes, seconds = Helpers.sec_to_time(total_seconds)
        return Helpers.time_to_str(hours, minutes, seconds)

    def __mul__(self, other: int) -> str:
        """
        Multiplies self by integer
        :param other: integer to multiply by
        :return: result of multiplication as formatted string 'HH:MM:SS'
        """
        total_seconds = self.total_seconds * other
        hours, minutes, seconds = Helpers.sec_to_time(total_seconds)
        return Helpers.time_to_str(hours, minutes, seconds)


if __name__ == "__main__":
    """
    Some tests
    """
    tti = TimeInterval(hours=21, minutes=58, seconds=50)
    addition = tti + 62
    assert addition == "21:59:52"
    subtraction = tti - 62
    assert subtraction == "21:57:48"
