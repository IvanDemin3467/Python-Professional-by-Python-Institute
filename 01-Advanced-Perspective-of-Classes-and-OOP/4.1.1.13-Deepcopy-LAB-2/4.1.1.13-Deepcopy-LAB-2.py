import copy


class Delicacy:
    def __init__(self, name: str, price: float, weight: int):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, weight: {self.weight}"


if __name__ == "__main__":
    warehouse = list()
    warehouse.append(Delicacy(name='Lolly Pop', price=0.4, weight=133))
    warehouse.append(Delicacy(name='Licorice', price=0.1, weight=251))
    warehouse.append(Delicacy(name='Chocolate', price=1, weight=601))
    warehouse.append(Delicacy(name='Sours', price=0.01, weight=513))
    warehouse.append(Delicacy(name='Hard candies', price=0.03, weight=433))

    shallow_warehouse = copy.copy(warehouse)
    for item in shallow_warehouse:
        if item.weight > 300:
            item.price *= 0.8

    deep_warehouse = copy.deepcopy(shallow_warehouse)
    for item in deep_warehouse:
        if item.weight > 300:
            item.price *= 0.8

    print('*' * 20)
    print('Source list of candies')
    for item in warehouse:
        print(item)

    print('*' * 20)
    print('Shallow copy')
    for item in warehouse:
        print(item)

    print('*' * 20)
    print('Deep copy')
    for item in deep_warehouse:
        print(item)
