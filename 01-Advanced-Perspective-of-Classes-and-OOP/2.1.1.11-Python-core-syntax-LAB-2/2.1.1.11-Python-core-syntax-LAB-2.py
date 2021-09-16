class TypeChecker:
    """
    Это дескриптор, проверяющий принадлежность значения переменной инстанса с именем name к типу value_type
    """
    def __init__(self, name, value_type):
        self.name = name
        self.value_type = value_type

    def __set__(self, instance, value):
        if isinstance(value, self.value_type):
            instance.__dict__[self.name] = value
        else:
            raise TypeError(f"'{self.name}' {value} must be {self.value_type}")

    def __get__(self, instance, class_):
        return instance.__dict__[self.name]


class Helpers:
    @staticmethod
    def sec_to_time(seconds: int) -> tuple:
        hours = seconds // 3600
        seconds = seconds % 3600
        minutes = seconds // 60
        seconds = seconds % 60
        return hours, minutes, seconds

    @staticmethod
    def time_to_sec(hours: int, minutes: int, seconds: int) -> int:
        return hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def time_to_str(hours: int, minutes: int, seconds: int) -> str:
        return f"{Helpers.int_to_str(hours)}:{Helpers.int_to_str(minutes)}:{Helpers.int_to_str(seconds)}"

    @staticmethod
    def int_to_str(value: int) -> str:
        if value // 10 == 0:
            return str(f"0{value}")
        else:
            return str(value)


class TimeInterval:
    hours = TypeChecker("hours", int)
    minutes = TypeChecker("minutes", int)
    seconds = TypeChecker("seconds", int)

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = Helpers.time_to_sec(self.hours, self.minutes, self.seconds)

    def __str__(self) -> str:
        return Helpers.time_to_str(self.hours, self.minutes, self.seconds)

    def __add__(self, other) -> str:
        if type(other) == int:
            new_time_interval = TimeInterval(hours=0, minutes=0, seconds=other)
        else:
            new_time_interval = other
        total_seconds = self.total_seconds + new_time_interval.total_seconds
        hours, minutes, seconds = Helpers.sec_to_time(total_seconds)
        return Helpers.time_to_str(hours, minutes, seconds)

    def __sub__(self, other) -> str:
        if type(other) == int:
            new_time_interval = TimeInterval(hours=0, minutes=0, seconds=other)
        else:
            new_time_interval = other
        total_seconds = self.total_seconds - new_time_interval.total_seconds
        hours, minutes, seconds = Helpers.sec_to_time(total_seconds)
        return Helpers.time_to_str(hours, minutes, seconds)

    def __mul__(self, other: int) -> str:
        total_seconds = self.total_seconds * other
        hours, minutes, seconds = Helpers.sec_to_time(total_seconds)
        return Helpers.time_to_str(hours, minutes, seconds)


if __name__ == "__main__":
    tti = TimeInterval(hours=21, minutes=58, seconds=50)
    addition = tti + 62
    assert addition == "21:59:52"
    subtraction = tti - 62
    assert subtraction == "21:57:48"
