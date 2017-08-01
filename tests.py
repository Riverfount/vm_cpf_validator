import unittest

from vm_cpf_validator import cpf_is_digits, cpf_has_correct_length, cpf_is_valid, format_cpf


class CpfValidatorTests(unittest.TestCase):

    def test_cpf_is_digits(self):
        """CPF must only accpet digits"""
        self.assertTrue(cpf_is_digits('12345678900'))

    def test_cpf_is_not_digits(self):
        """CPF must only accpet digits"""
        self.assertFalse(cpf_is_digits('123456789AA'))

    def test_cpf_has_correct_digits(self):
        """CPF must have 11 digits."""
        self.assertTrue(cpf_has_correct_length("11144477711"))

    def test_cpf_has_not_correct_digits(self):
        """CPF must have 11 digits."""
        self.assertFalse(cpf_has_correct_length("111444777"))

    def test_cpf_is_valid(self):
        """CPF must have a valid final digits"""
        self.assertTrue(cpf_is_valid('11144477735'))

    def test_cpf_is_not_valid(self):
        self.assertFalse(cpf_is_valid('11144477711'))

    def test_format_cpf(self):
        expected = '123.456.789-11'
        self.assertEqual(format_cpf('12345678911'), expected)

if __name__ == '__main__':
    unittest.main()
