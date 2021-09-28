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
    def __init__(self, fuel_type: str):
        self.fuel_type = fuel_type
        self.__state = "off"

    def start(self):
        self.__state = "on"
        print(f"Engine with {self.fuel_type} fuel started")

    def stop(self):
        self.__state = "off"
        print(f"Engine with {self.fuel_type} fuel stopped")

    def get_state(self):
        print(f"The state of the engine with {self.fuel_type} fuel is {self.__state}")


class Vehicle:
    def __init__(self, vin: int, engine: Engine, tires: Tires):
        self.vin = vin
        self.engine = engine
        self.tires = tires


if __name__ == "__main__":
    # instantiate two sets of tires
    city_tires = Tires(size=15)
    off_road_tires = Tires(size=18)
    # instantiate two engines
    electric_engine = Engine("electric")
    petrol_engine = Engine("petrol")
    # instantiate two objects representing cars
    city_car = Vehicle(vin=123456, engine=electric_engine, tires=city_tires)
    all_terrain_car = Vehicle(vin=987654, engine=petrol_engine, tires=off_road_tires)

    # calling methods responsible for interaction with components
    print(city_car.engine.fuel_type)
    city_car.engine.start()
    city_car.engine.get_state()
    city_car.engine.stop()
    city_car.engine.get_state()
    print(city_car.tires.size)
    print(city_car.tires.get_pressure())
    city_car.tires.pump()
    print(city_car.tires.get_pressure())

    print(all_terrain_car.engine.fuel_type)
    all_terrain_car.engine.start()
    all_terrain_car.engine.get_state()
    all_terrain_car.engine.stop()
    all_terrain_car.engine.get_state()
    print(all_terrain_car.tires.size)
    print(all_terrain_car.tires.get_pressure())
    all_terrain_car.tires.pump()
    print(all_terrain_car.tires.get_pressure())
