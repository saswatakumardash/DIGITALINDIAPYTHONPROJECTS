# helper library functions
from math import gcd
import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.misc import VALID, INVALID, FIRST, SECOND, THIRD, FOURTH, LAST, InvalidInputException

# additional constants
EXPECTED_ARGS_POW_OP, EXPECTED_ARGS_NON_POW_OP = 4, 5

switch_op_func = {
    "+" :   lambda a, b: a + b,
    "-" :   lambda a, b: a - b,
    "*" :   lambda a, b: a * b,
    "/" :   lambda a, b: a / b,
    "<" :   lambda a, b: a < b,
    ">" :   lambda a, b: a > b,
    "<=":   lambda a, b: a <= b,
    ">=":   lambda a, b: a >= b,
    "==":   lambda a, b: a == b,
    "!=":   lambda a, b: a != b
}


class RationalNumber(object):
    """Class for representing rational numbers of the form p/q."""

    def __init__(self, numerator, denominator):
        self.Numerator = numerator
        self.Denominator = denominator

    # supported operators
    Arithmetic_operators = {"+", "-", "*", "/", "**"}
    Logical_operators = {"==", "!=", ">", "<", ">=", "<="}

    @staticmethod
    def consolidate(numerator, denominator):
        """Makes only the numerator negative in case of a negative rational number - for ease of representation and handling.
        Also converts to canonical form.
        """
        
        if (numerator < 0 < denominator) or (denominator < 0 < numerator):  # negative number
            num = RationalNumber(-abs(int(numerator)), abs(int(denominator)))
        else:
            num = RationalNumber(abs(int(numerator)), abs(int(denominator)))
        return num.to_canonical()

    @staticmethod
    def is_valid(p, q):
        """Checks if p and q form a valid Rational Number of the form p/q."""

        try:    int(p) and int(q)  # both p and q need to be integers
        except: return INVALID, "Invalid Input: Both p and q must be Integers in rational number p/q."
        if int(q) == 0: # q shouldn't be 0
            return INVALID, "Invalid Input: q can't be Zero in rational number p/q."
        return VALID, ""

    # overloading the addition (+) operator
    def __add__(self, other):
        gcd_denominator = gcd(self.Denominator, other.Denominator)
        lcm_denominator = (self.Denominator * other.Denominator) / gcd_denominator
        lhs_mul_factor = lcm_denominator / self.Denominator
        rhs_mul_factor = lcm_denominator / other.Denominator
        numerator = self.Numerator * lhs_mul_factor + other.Numerator * rhs_mul_factor
        return RationalNumber.consolidate(numerator, lcm_denominator)

    # overloading the multiplication (*) operator
    def __mul__(self, other):
        numerator = self.Numerator * other.Numerator
        denominator = self.Denominator * other.Denominator
        return RationalNumber.consolidate(numerator, denominator)

    # overloading the subtraction (-) operator
    def __sub__(self, other):
        other_negative = other.__mul__(RationalNumber(-1, 1))
        return self.__add__(other_negative)     # a - b == a + (b * -1)

    # overloading the division (/) operator
    def __truediv__(self, other):
        try:
            other_reciprocal = validate_and_create_rational_number(other.Denominator, other.Numerator)
            return self.__mul__(other_reciprocal)   # a / b == a * (1 / b)
        except:   raise InvalidInputException("Invalid Input: Zero Division Error.") # division by zero

    # overloading the power (**) operator
    def __pow__(self, number):
        numerator = pow(self.Numerator, abs(number))
        denominator = pow(self.Denominator, abs(number))
        if number < 0:  # if power is negative, reciprocate
            numerator, denominator = denominator, numerator
        return RationalNumber.consolidate(numerator, denominator)

    # overloading the less than (<) operator
    def __lt__(self, other):
        lhs = float(self.Numerator / self.Denominator)
        rhs = float(other.Numerator / other.Denominator)
        return lhs < rhs

    # overloading the less than (<) operator
    def __gt__(self, other):
        lhs = float(self.Numerator / self.Denominator)
        rhs = float(other.Numerator / other.Denominator)
        return lhs > rhs

    # overloading the equal to (==) operator
    def __eq__(self, other):
        self = RationalNumber.consolidate(self.Numerator, self.Denominator)
        other = RationalNumber.consolidate(other.Numerator, other.Denominator)
        return self.Numerator == other.Numerator and self.Denominator == other.Denominator

    # overloading the less than or equal to (<=) operator
    def __le__(self, other):
        return not self.__gt__(other)

    # overloading the greater than or equal to (>=) operator
    def __ge__(self, other):
        return not self.__lt__(other)

    # overloading the not equal to (!=) operator
    def __ne__(self, other):
        return not self.__eq__(other)

    # overloading the default string conversion
    def __str__(self):
        return str(self.Numerator) + "/" + str(self.Denominator)

    def is_canonical(self):
        """Whether the rational number is in canonical form."""
        
        return gcd(self.Numerator, self.Denominator) == 1

    def to_canonical(self):
        """Return canonical form of the rational number."""

        gc_div = gcd(self.Numerator, self.Denominator)
        return RationalNumber(int(self.Numerator / gc_div), int(self.Denominator / gc_div))

    def is_integer(self):
        """Whether the rational number is a pure integer."""

        return self.to_canonical().Denominator == 1


def validate_and_create_rational_number(p, q):
    valid, err = RationalNumber.is_valid(p, q)
    if not valid:
        raise InvalidInputException(err)
    return RationalNumber(int(p), int(q))


def validate_and_pass_operator(operator):
    if operator not in RationalNumber.Arithmetic_operators and operator not in RationalNumber.Logical_operators:
        raise InvalidInputException("Invalid Input: '" + operator + "' operator not defined.")
    return operator


def main():

    try:
        raw_input = input().split()
        num_inp_args = len(raw_input)

        if num_inp_args < EXPECTED_ARGS_POW_OP:  raise InvalidInputException()  # min no of arguments
        first_rational_number = validate_and_create_rational_number(raw_input[FIRST], raw_input[SECOND])
        operator = validate_and_pass_operator(raw_input[LAST])

        if operator != "**":  # for all operators other than the 'power' operator
            if num_inp_args < EXPECTED_ARGS_NON_POW_OP:    raise InvalidInputException()  # appropriate no of arguments
            second_rational_number = validate_and_create_rational_number(raw_input[THIRD], raw_input[FOURTH])
            
            result = switch_op_func[operator](first_rational_number, second_rational_number)
        
        else:  # for ** (power) operation, second number is input as a pure integer
            second_rational_number = validate_and_create_rational_number(raw_input[THIRD], 1)
            result = first_rational_number ** second_rational_number.Numerator

        if operator in RationalNumber.Arithmetic_operators:
            print(result.Numerator if result.is_integer() else result)
        else:  # logical operator
            print(str(result).title())  # present the boolean result in title case
    
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
