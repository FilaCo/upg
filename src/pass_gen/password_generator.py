import random
import string


class PasswordGenerator:
    def __init__(self):
        self.__alphabet = []
        self.__length = 0

    def generate(self) -> str:
        password_letters = random.sample("".join(self.__alphabet), self.__length)

        return "".join(password_letters)

    def add_ascii_lowercase(self) -> None:
        if string.ascii_lowercase in self.__alphabet:
            return

        self.__alphabet += string.ascii_lowercase

    def add_ascii_uppercase(self) -> None:
        if string.ascii_uppercase in self.__alphabet:
            return

        self.__alphabet += string.ascii_uppercase

    def add_digits(self) -> None:
        if string.digits in self.__alphabet:
            return

        self.__alphabet += string.digits

    def add_punctuation(self) -> None:
        if string.punctuation in self.__alphabet:
            return

        self.__alphabet += string.punctuation
