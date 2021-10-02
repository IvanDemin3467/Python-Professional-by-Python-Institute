import datetime


@classmethod
def get_instantiation_time(cls: type):
    """
    This class method will be attached to every class instantiated by MetaCleaner metaclass.
    :param cls: A class from which the method is called.
    :return: None
    """
    print(f"Object {cls.__name__} was created at {cls.instantiation_time}")


class MetaCleaner(type):
    """
    This metaclass is responsible for:
        - equipping all newly instantiated classes with time stamps,
            persisted in a class attribute named instantiation_time;
        - equipping all newly instantiated classes with the get_instantiation_time() method.
            The method returns the value of the class attribute instantiation_time.
    Also MetaCleaner metaclass have its own class variable classes_instantiated
        that contains a list of the names of the classes instantiated by the metaclass
    """
    classes_instantiated = []  # A list of the names of the classes instantiated by the metaclass

    def __new__(mcs, name, bases, dictionary):
        MetaCleaner.classes_instantiated.append(name)  # Store names of instantiated classes
        if "instantiation_time" not in dictionary:
            dictionary["instantiation_time"] = datetime.datetime.now()  # Append timestamp to the instantiated class
        if "get_instantiation_time" not in dictionary:
            dictionary["get_instantiation_time"] = get_instantiation_time  # Append method to the instantiated class
        obj = super().__new__(mcs, name, bases, dictionary)  # Pass control to the type metaclass and instantiate class
        return obj


class MyClass1(metaclass=MetaCleaner):
    pass


class MyClass2(metaclass=MetaCleaner):
    pass


class MyClass3(metaclass=MetaCleaner):
    pass


if __name__ == "__main__":
    obj1 = MyClass1
    obj2 = MyClass2
    obj3 = MyClass3
    obj4 = MyClass1
    obj5 = MyClass2
    obj6 = MyClass3
    for entry in (obj1, obj2, obj3, obj4, obj5, obj6):
        entry.get_instantiation_time()

    print(MetaCleaner.classes_instantiated)
