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


class TimeInterval:
    hours = TypeChecker("hours", int)
    minutes = TypeChecker("minutes", int)
    seconds = TypeChecker("seconds", int)

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = self.time_to_sec(self.hours, self.minutes, self.seconds)

    def __str__(self) -> str:
        return self.time_to_str(self.hours, self.minutes, self.seconds)

    def __add__(self, other) -> str:
        total_seconds = self.total_seconds + other.total_seconds
        hours, minutes, seconds = self.sec_to_time(total_seconds)
        return self.time_to_str(hours, minutes, seconds)

    def __sub__(self, other) -> str:
        total_seconds = self.total_seconds - other.total_seconds
        hours, minutes, seconds = self.sec_to_time(total_seconds)
        return self.time_to_str(hours, minutes, seconds)

    def __mul__(self, other: int) -> str:
        total_seconds = self.total_seconds * other
        hours, minutes, seconds = self.sec_to_time(total_seconds)
        return self.time_to_str(hours, minutes, seconds)

    @staticmethod
    def sec_to_time(seconds: int) -> tuple:
        hours = seconds // 3600
        seconds = seconds % 3600
        minutes = seconds // 60
        seconds = seconds % 60
        return hours, minutes, seconds

    @staticmethod
    def time_to_sec(hours: int, minutes: int, seconds: int) -> int:
        return hours*3600 + minutes*60 + seconds

    @classmethod
    def time_to_str(cls, hours: int, minutes: int, seconds: int) -> str:
        return f"{cls.int_to_str(hours)}:{cls.int_to_str(minutes)}:{cls.int_to_str(seconds)}"

    @staticmethod
    def int_to_str(value: int) -> str:
        if value // 10 == 0:
            return str(f"0{value}")
        else:
            return str(value)


if __name__ == "__main__":
    fti = TimeInterval(hours=21, minutes=58, seconds=50)
    assert str(fti) == "21:58:50"
    sti = TimeInterval(hours=1, minutes=45, seconds=22)
    addition = fti + sti
    assert str(addition) == "23:44:12"
    subtraction = fti - sti
    assert str(subtraction) == "20:13:28"
    multiplication = fti * 2
    assert str(multiplication) == "43:57:40"

    print("Tests performed: 3. Tests successful: 3")
    print("Try TypeChecker:")
    try:
        tti = TimeInterval(hours="1", minutes=45, seconds=22)
    except TypeError as e:
        print(e)
    print("TypeChecker is OK")
