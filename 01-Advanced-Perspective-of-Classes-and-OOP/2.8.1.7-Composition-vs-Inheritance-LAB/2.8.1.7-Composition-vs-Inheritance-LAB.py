class Tires:
    def __init__(self, size: int):
        self.size = size
        self.pressure = 0

    def get_pressure(self) -> int:
        return self.pressure

    def pump(self, psi: int):
        self.pressure = psi


class Engine:
    def __init__(self, fuel_type: str):
        self.fuel_type = fuel_type
        self.state = 'off'

    def start(self):
        self.state = 'on'

    def stop(self):
        self.state = 'off'

    def get_state(self) -> str:
        return self.state


class Car:
    def __init__(self, vin: str, engine: Engine, tires: Tires):
        self.VIN = vin
        self.engine = engine
        self.tires = tires


if __name__ == "__main__":
    city_tires = Tires(15)
    off_road_tires = Tires(18)

    electric_engine = Engine('electric')
    petrol_engine = Engine('electric')

    city_car = Car('111A', electric_engine, city_tires)
    all_terrain_car = Car('888S', petrol_engine, off_road_tires)

    # prepare all_terrain_car for a rally
    print('All-terrain car engine is', all_terrain_car.engine.get_state())
    all_terrain_car.tires.pump(10)
    all_terrain_car.engine.start()
    print('All-terrain car engine is', all_terrain_car.engine.get_state())

    # prepare city car for a shopping
    print('City car engine is', city_car.engine.get_state())
    city_car.tires.pump(3)
    city_car.engine.start()
    print('City car engine is', city_car.engine.get_state())
    city_car.engine.stop()
    print('City car engine is', city_car.engine.get_state())
