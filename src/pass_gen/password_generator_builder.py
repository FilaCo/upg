from pass_gen.password_generator import PasswordGenerator


class PasswordGeneratorBuilder:
    def __init__(self) -> None:
        self.__password_generator = PasswordGenerator()

    def at_least_one_lowercase(self) -> None:
        self.__password_generator.add_ascii_lowercase()

    def at_least_one_uppercase(self) -> None:
        self.__password_generator.add_ascii_uppercase()

    def at_least_one_digit(self) -> None:
        self.__password_generator.add_digits()

    def at_least_one_punctuation(self) -> None:
        self.__password_generator.add_punctuation()

    @property
    def password_generator(self) -> PasswordGenerator:
        return self.__password_generator

    def reset(self) -> None:
        self.__password_generator = PasswordGenerator()
