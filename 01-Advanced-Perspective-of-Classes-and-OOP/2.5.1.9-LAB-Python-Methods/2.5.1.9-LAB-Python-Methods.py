class LuxuryWatch:
    """
    A class, representing luxury watch.
    Has alternative constructor to create watch with engraving
    """
    __watches_created = 0

    def __init__(self):
        """
        Simple constructor. Increments number of watches created
        """
        LuxuryWatch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls) -> str:
        """
        Class method, that returns sing, representing number of watches created
        """
        return f"{cls.__watches_created} luxury watches created"

    @staticmethod
    def __validate_engraving(text: str) -> bool:
        """
        Static method, that accepts text and validates it to some restrictions:
        • it should not be longer than 40 characters;
        • it should consist of alphanumerical characters, so no space characters are allowed;
        :return: bool result of validation
        """
        return type(text) is str and len(text) <= 40 and text.isalnum()

    @classmethod
    def create_with_engraving(cls, engraving: str) -> object:
        """
        Alternative constructor, that creates luxury watches with engraving
        :param: engraving: string, that should be engraved on watch
        :return: LuxuryWatch object with property 'engraving'
            or ValueError if engraving did not pass validation
        """
        if cls.__validate_engraving(engraving):
            watch = LuxuryWatch()
            watch.engraving = engraving
            return watch
        else:
            raise ValueError("Engraving is incorrect")


if __name__ == "__main__":
    # create normal watch
    simple_watch = LuxuryWatch()
    print(LuxuryWatch.get_number_of_watches_created())

    # create watch with normal engraving
    engraved_watch = LuxuryWatch.create_with_engraving("1" * 40)
    print(LuxuryWatch.get_number_of_watches_created())
    print(engraved_watch.engraving)

    # create watch with incorrect engraving
    try:
        incorrect_watch = LuxuryWatch.create_with_engraving("foo@baz.com")
    except ValueError as e:
        print(e)
    print(LuxuryWatch.get_number_of_watches_created())
