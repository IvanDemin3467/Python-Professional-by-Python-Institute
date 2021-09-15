import random


class MobilePhone:
    """
    Simulates mobile phone
    """
    def __init__(self, number):
        """
        Saves phone number taken on instantiation
        :param number: phone number of this phone
        """
        self.__number = number

    def turn_on(self):
        """
        Simulates turning on the phone
        :return: the message 'mobile phone {number} is turned on'
        """
        return f"mobile phone {self.__number} is turned on"

    @staticmethod
    def turn_off():
        """
        Simulates turning off the phone
        :return: the message 'mobile phone is turned off'
        """
        return "mobile phone is turned off"

    @staticmethod
    def call(number):
        """
        Simulates calling to the phone
        :param number: phone number to call
        :return: the message 'calling {number}'
        """
        return f"calling {number}"

    def get_number(self):
        """
        getter for private property __number
        :return: number of this phone
        """
        return self.__number


class Helper:
    """
    Helps generate random phone number
    """
    @staticmethod
    def rand_numbers(number):
        """
        Helps generate random digits
        :param number: amount of digits to generate
        :return: generated random digits
        """
        result = ""
        for i in range(number):
            result += str(random.randint(0, 9))
        return result

    @classmethod
    def rand_phone_number(cls):
        """
        Helps generate random phone number
        :return: phone number in format +7(9xx)xxx-xx-xx
        """
        return f"+7(9{cls.rand_numbers(2)}){cls.rand_numbers(3)}-{cls.rand_numbers(2)}-{cls.rand_numbers(2)}"


if __name__ == "__main__":
    """
    Some tests
    """
    phone1 = MobilePhone(Helper.rand_phone_number())
    print(phone1.turn_on())
    phone2 = MobilePhone(Helper.rand_phone_number())
    print(phone2.turn_on())

    print(phone1.call(phone2.get_number()))

    print(phone1.turn_off())
    print(phone2.turn_off())
