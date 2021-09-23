from abc import ABC, abstractmethod


class AbstractScanner(ABC):
    @abstractmethod
    def scan_document(self):
        """
        returns a string indicating that the document has been printed
        """
        pass

    @classmethod
    @abstractmethod
    def get_scanner_status(cls):
        """
        returns information about the scanner  (max. resolution, serial number)
        """
        pass


class AbstractPrinter(ABC):
    @abstractmethod
    def print_document(self):
        """
        returns a string indicating that the document has been printed;
        """
        pass

    @classmethod
    @abstractmethod
    def get_printer_status(cls):
        """
        returns information about the printer (max. resolution, serial number)
        """


class MFD1(AbstractScanner, AbstractPrinter):
    """
    Is a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) are low
    """
    __scanner_serial_number = 0
    __printer_serial_number = 0

    def __init__(self, printer_resolution="100 dpi", scanner_resolution="110 dpi"):
        self.__printer_resolution = printer_resolution
        self.__scanner_resolution = scanner_resolution
        MFD1.__printer_serial_number += 1
        MFD1.__scanner_serial_number += 1

    def scan_document(self):
        print("Document scanned")

    def print_document(self):
        print("Document printed")

    def get_printer_status(self):
        print(f"Printer resolution: {self.__printer_resolution}, printer serial number: {self.__printer_serial_number}")

    def get_scanner_status(self):
        print(f"Scanner resolution: {self.__scanner_resolution}, scanner serial number: {self.__scanner_serial_number}")


class MFD2(MFD1):
    """
    Is a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) are low
    """

    def __init__(self, printer_resolution="200 dpi", scanner_resolution="220 dpi"):
        super().__init__(printer_resolution=printer_resolution, scanner_resolution=scanner_resolution)
        self.__printing_operations_history = 0

    def scan_document(self):
        super().scan_document()

    def print_document(self):
        super().print_document()
        self.__printing_operations_history += 1

    def get_printer_status(self):
        super().get_printer_status()

    def get_scanner_status(self):
        super().get_scanner_status()

    def get_printing_operations_history(self):
        print(f"Totally printed {self.__printing_operations_history} times")


class MFD3(MFD2):
    """
    Is a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) are low
    """

    def __init__(self, printer_resolution="300 dpi", scanner_resolution="330 dpi"):
        super().__init__(printer_resolution=printer_resolution, scanner_resolution=scanner_resolution)
        self.__printing_operations_history = 0

    def scan_document(self):
        super().scan_document()

    def print_document(self):
        super().print_document()

    def get_printer_status(self):
        super().get_printer_status()

    def get_scanner_status(self):
        super().get_scanner_status()

    def get_printing_operations_history(self):
        super().get_printing_operations_history()

    @staticmethod
    def fax_document():
        print("Document faxed")


if __name__ == "__main__":
    mfd = MFD1()
    mfd.get_scanner_status()
    mfd.get_printer_status()
    mfd.scan_document()
    mfd.print_document()

    mfd = MFD2()
    mfd.get_scanner_status()
    mfd.get_printer_status()
    mfd.scan_document()
    mfd.print_document()
    mfd.print_document()
    mfd.get_printing_operations_history()

    mfd = MFD3()
    mfd.get_scanner_status()
    mfd.get_printer_status()
    mfd.scan_document()
    mfd.print_document()
    mfd.print_document()
    mfd.get_printing_operations_history()
    mfd.fax_document()
