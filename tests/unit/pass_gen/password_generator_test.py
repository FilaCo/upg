from unittest import TestCase

from pass_gen.password_generator import PasswordGenerator


class PasswordGeneratorTest(TestCase):
    def test__add_ascii_lowercase__add_once__ascii_lowercase_only_password(self):
        # given
        password_generator = PasswordGenerator()
        expected_alphabet = "abcdefghijklmnopqrstuvwxyz"

        # when
        password_generator.add_ascii_lowercase()
        password_generator.length = 100
        sample_password = password_generator.generate()

        # then
        for symbol in sample_password:
            if symbol not in expected_alphabet:
                self.fail("symbol %s was not in expected alphabet" % symbol)

    def test__length__add_one_alphabet_several_times__required_length_changed_once(self):
        # given
        password_generator = PasswordGenerator()

        # when
        password_generator.add_ascii_lowercase()
        password_generator.add_ascii_lowercase()
        password_generator.add_digits()

        def set_length(x: int):
            password_generator.length = x

        # then
        self.assertRaises(ValueError, set_length, 1)
