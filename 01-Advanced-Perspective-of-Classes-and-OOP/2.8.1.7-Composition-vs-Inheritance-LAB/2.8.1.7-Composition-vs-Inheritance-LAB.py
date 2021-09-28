class Tires:
    def __init__(self, size: int):
        self.__pressure = 0.0
        self.size = size

    def get_pressure(self) -> float:
        return self.__pressure

    def pump(self):
        print("Pumping tires to 1.4 bar")
        self.__pressure = 1.4


class Engine:
    pass
