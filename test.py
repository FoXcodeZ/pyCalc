import unittest
import io
import calculator
from unittest.mock import patch


class Tester(unittest.TestCase):

    def test_validate_integer_valid(self):
        result = calculator.is_number('2')
        self.assertEqual(result, True)

    def test_validate_negative_integer_valid(self):
        result = calculator.is_number('-10')
        self.assertEqual(result, True)

    def test_validate_float_valid(self):
        result = calculator.is_number('5.55')
        self.assertEqual(result, True)

    def test_validate_negative_float_valid(self):
        result = calculator.is_number('-10.49')
        self.assertEqual(result, True)

    def test_convert_integer(self):
        result = calculator.convert_number('10')
        self.assertEqual(result, 10)

    def test_convert_negative_integer(self):
        result = calculator.convert_number('-250')
        self.assertEqual(result, -250)

    def test_convert_float(self):
        result = calculator.convert_number('7.25')
        self.assertAlmostEqual(result, 7.25)

    def test_convert_negative_float(self):
        result = calculator.convert_number('-15.06')
        self.assertAlmostEqual(result, -15.06)

    def test_validate_number_not_valid(self):
        result = calculator.is_number('x')
        self.assertEqual(result, False)

    def test_is_valid_operator_valid_1(self):
        result = calculator.is_valid_operator('+')
        self.assertEqual(result, True)

    def test_is_valid_operator_valid_2(self):
        result = calculator.is_valid_operator('-')
        self.assertEqual(result, True)

    def test_is_valid_operator_valid_3(self):
        result = calculator.is_valid_operator('/')
        self.assertEqual(result, True)

    def test_is_valid_operator_valid_4(self):
        result = calculator.is_valid_operator('*')
        self.assertEqual(result, True)

    def test_is_valid_operator_not_valid_1(self):
        result = calculator.is_valid_operator('%')
        self.assertEqual(result, False)

    def test_is_valid_operator_not_valid_2(self):
        result = calculator.is_valid_operator('t')
        self.assertEqual(result, False)

    def test_calc_plus_1(self):
        a, b = 3, 4
        result = calculator.calc('+', a, b)
        self.assertEqual(result, a + b)

    def test_calc_plus_2(self):
        a, b = -3, 4
        result = calculator.calc('+', a, b)
        self.assertEqual(result, a + b)

    def test_calc_plus_3(self):
        a, b = -3, -4
        result = calculator.calc('+', a, b)
        self.assertEqual(result, a + b)

    def test_calc_minus_1(self):
        a, b = 3, 4
        result = calculator.calc('-', a, b)
        self.assertEqual(result, a - b)

    def test_calc_minus_2(self):
        a, b = -3, 4
        result = calculator.calc('-', a, b)
        self.assertEqual(result, a - b)

    def test_calc_minus_3(self):
        a, b = 3, -4
        result = calculator.calc('-', a, b)
        self.assertEqual(result, a - b)

    def test_calc_minus_4(self):
        a, b = -3, -4
        result = calculator.calc('-', a, b)
        self.assertEqual(result, a - b)

    def test_calc_multiply_1(self):
        a, b = -3, -4
        result = calculator.calc('*', a, b)
        self.assertEqual(result, a * b)

    def test_calc_multiply_2(self):
        a, b = 3, -4
        result = calculator.calc('*', a, b)
        self.assertEqual(result, a * b)

    def test_calc_multiply_3(self):
        a, b = -3, 4
        result = calculator.calc('*', a, b)
        self.assertEqual(result, a * b)

    def test_calc_multiply_4(self):
        a, b = 3, 4
        result = calculator.calc('*', a, b)
        self.assertEqual(result, a * b)

    def test_calc_division_1(self):
        a, b = 3, 4
        result = calculator.calc('/', a, b)
        self.assertEqual(result, a / b)

    def test_calc_division_2(self):
        a, b = -3, 4
        result = calculator.calc('/', a, b)
        self.assertEqual(result, a / b)

    def test_calc_division_3(self):
        a, b = 3, -4
        result = calculator.calc('/', a, b)
        self.assertEqual(result, a / b)

    def test_calc_division_4(self):
        a, b = -3, -4
        result = calculator.calc('/', a, b)
        self.assertEqual(result, a / b)

    def test_calc_division_5(self):
        a, b = -3, 0
        result = calculator.calc('/', a, b)
        self.assertEqual(result, None)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
