import random
import string


class PasswordGenerator:
    def __init__(self):
        self.__alphabet = []
        self.__length = 0

    def generate(self) -> str:
        if self.__length == 0:
            return ""

        password_letters = []
        for charset in self.__alphabet:
            password_letters.append(random.choice(charset))

        full_alphabet = "".join(self.__alphabet)
        while len(password_letters) < self.__length:
            password_letters.append(random.choice(full_alphabet))

        random.shuffle(password_letters)

        return "".join(password_letters)

    def add_ascii_lowercase(self) -> None:
        if string.ascii_lowercase in self.__alphabet:
            return

        self.__alphabet.append(string.ascii_lowercase)

    def add_ascii_uppercase(self) -> None:
        if string.ascii_uppercase in self.__alphabet:
            return

        self.__alphabet.append(string.ascii_uppercase)

    def add_digits(self) -> None:
        if string.digits in self.__alphabet:
            return

        self.__alphabet.append(string.digits)

    def add_punctuation(self) -> None:
        if string.punctuation in self.__alphabet:
            return

        self.__alphabet.append(string.punctuation)

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, value: int) -> None:
        req_symbols_len = len(self.__alphabet)
        if value < req_symbols_len:
            raise ValueError("new length: %d < required symbols: %d" % (value, req_symbols_len))

        self.__length = value
