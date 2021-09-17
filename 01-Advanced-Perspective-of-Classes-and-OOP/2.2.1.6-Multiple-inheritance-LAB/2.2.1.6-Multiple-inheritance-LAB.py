class Scanner:
    @classmethod
    def scan(cls):
        print(f"'scan() method from Scanner class'")


class Printer:
    @classmethod
    def print(cls):
        print(f"'print() method from Printer class'")


class Fax:
    @classmethod
    def print(cls):
        print(f"'print() method from Fax class'")

    @classmethod
    def send(cls):
        print(f"'send() method from Fax class'")


class MFDSPF(Scanner, Printer, Fax):
    pass


class MFDSFP(Scanner, Fax, Printer):
    pass


if __name__ == "__main__":
    spf = MFDSPF()
    sfp = MFDSFP()
    spf.scan()
    spf.print()
    spf.send()
    sfp.scan()
    sfp.print()
    sfp.send()
