class TimeInterval:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.int_to_str(self.hours)}:{self.int_to_str(self.minutes)}:{self.int_to_str(self.seconds)}"

    @staticmethod
    def int_to_str(value: int) -> str:
        if value // 10 == 0:
            return str(f"0{value}")
        else:
            return str(value)


if __name__ == "__main__":
    fti = TimeInterval(hours=21, minutes=58, seconds=50)
    assert str(fti) == "21:58:50"
