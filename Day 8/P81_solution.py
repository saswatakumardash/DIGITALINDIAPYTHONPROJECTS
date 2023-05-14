# helper library functions
from math import sqrt, pi
import sys, os
from typing import overload
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.misc import FIRST, SECOND, LAST, InvalidInputException

# additional constants
min_side_args = {  # minimum no of numeric 'sides' to be input (apart from 'color' and 'filled' status)
    "shape"         :   0,
    "triangle"      :   3,  # a triangle is defined by at least 3 sides
    "quadrilateral" :   4,  # a quadrilateral is defined by at least 4 sides
    "rectangle"     :   2,  # a rectangle is defined by 2 sides (length, breadth)
    "square"        :   1,  # a square is defined by by its side length
    "n-gon"         :   3,  # a polygon is made up of a minimum of 3 sides
    "circle"        :   1   # a circle is defined by its radius
}
valid_shape_names = min_side_args.keys()

DEFAULT_COLOR = "Black"
DEFAULT_FILLED_STATUS = False


class Shape(object):
    """A top level class for various shapes.
    Class specific attributes:
        Color:  Color of the Shape
        Filled: Fill status of the Shape
    """

    def __init__(self, color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS):
        self.Color = color
        self.Filled = filled

    def is_filled(self):
        """Return the fill status of the Shape."""
        return self.Filled

    def color(self):
        return self.Color

    def perimeter(self):
        """Return the perimeter of the Shape."""
        return None

    def area(self):
        """Return the area of the Shape."""
        return None


class Triangle(Shape):
    """Inherits Shape class.
    Class specific attributes:
        Side1, Side2, Side3
    """

    def __init__(self, side1, side2, side3, color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS):
        if not Triangle.is_valid(side1, side2, side3):
            raise InvalidInputException("Invalid Input: Given three sides can't form a triangle.")
        self.Side1 = float(side1)  # creating and initializing instance variables
        self.Side2 = float(side2)
        self.Side3 = float(side3)
        # invoking the __init__ of the parent class
        super().__init__(color, filled)

    @staticmethod
    def is_valid(side1, side2, side3):
        return side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2

    # overriding perimeter function
    def perimeter(self):
        return self.Side1 + self.Side2 + self.Side3

    # overriding area function
    def area(self):
        a = self.Side1
        b = self.Side2
        c = self.Side3
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))


class Quadrilateral(Shape):
    """Inherits Shape class.
    Class specific attributes:
        Side1, Side2, Side3, Side4
    """

    def __init__(self, side1, side2, side3, side4, color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS):
        self.Side1 = float(side1)
        self.Side2 = float(side2)
        self.Side3 = float(side3)
        self.Side4 = float(side4)
        super().__init__(color, filled)

    def perimeter(self):
        return self.Side1 + self.Side2 + self.Side3 + self.Side4


class Rectangle(Quadrilateral):
    """Inherits Quadrilateral class.
    Class specific attributes:
        Length, Breadth
    """

    def __init__(self, length, breadth, color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS):
        self.Length = float(length)
        self.Breadth = float(breadth)
        # alternatively can override the perimeter method as well
        super().__init__(length, breadth, length, breadth, color, filled)  # required for perimeter calculation

    def area(self):
        return self.Length * self.Breadth


class Square(Rectangle):
    """Inherits Rectangle class.
    Class specific attributes:
        Side
    """

    def __init__(self, side, color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS):
        self.Side = float(side)
        super().__init__(side, side, color, filled)


class Ngon(Shape):
    """Inherits Shape class.
    Class specific attributes:
        Perimeter
    """

    # def __init__(self, *sides, color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS):
    def __init__(self,  color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS, *sides):
        perimeter = 0
        for side in sides:
            perimeter += side
        self.Perimeter = perimeter
        super().__init__(color, filled)

    def perimeter(self):
        return self.Perimeter


class Circle(Shape):
    """Inherits Shape class.
    Class specific attributes:
        Radius
    """

    def __init__(self, radius, color=DEFAULT_COLOR, filled=DEFAULT_FILLED_STATUS):
        self.Radius = float(radius)
        super().__init__(color, filled)

    def perimeter(self):
        return 2 * pi * self.Radius

    def area(self):
        return pi * pow(self.Radius, 2)


switch_shape_func = {
    "shape"         :   Shape,
    "triangle"      :   Triangle,
    "quadrilateral" :   Quadrilateral,
    "rectangle"     :   Rectangle,
    "square"        :   Square,
    "n-gon"         :   Ngon,
    "circle"        :   Circle
}


def parseBoolean(string):
    """Returns parsed boolean value of string.
    Raises exception if not boolean."""
    
    if string.lower() not in ["true", "false"]:
        raise InvalidInputException("Invalid Input: Check filled status.")
    return string.lower() == "true"


def validate_and_parse_args(args):
    """Returns parsed input arguments after validating them."""

    shape_name, other_args = args[FIRST].lower(), args[SECOND:]  # case insensitive shape_name comparison
    sides, color, filled = [], None, None
    try:
        if shape_name not in valid_shape_names:  raise InvalidInputException("Invalid Input: Check shape name.")
        IS_NGON = shape_name == "n-gon"

        expected_no_of_sides = min_side_args[shape_name]  # variable no of sides in case of n-gon
        if len(other_args) < expected_no_of_sides:
            raise InvalidInputException("Invalid Input: Too few arguments.")
        list_of_possible_sides = other_args if IS_NGON else other_args[:expected_no_of_sides]
        index = -1  # to cover the case of shape objects, which don't have any sides specified
        for index, arg in enumerate(list_of_possible_sides):
            try:    sides.append(float(arg))  # sides must be numeric
            except:  # if side not numeric or in case of NGON possibly crossed the last numeric input side
                if not IS_NGON or index < expected_no_of_sides:  # n-gon must have min of 3 input sides
                    raise InvalidInputException("Invalid Input: Check input sides.")

        num_remaining_args = len(other_args) - index - 1
        if num_remaining_args == 1:
            color = other_args[LAST]  # only remaining non-numeric arg must be 'color'
        elif num_remaining_args == 2:
            try:
                filled = parseBoolean(other_args[LAST])  # last arg must be 'filled' boolean input
                color = other_args[LAST-1]  # last but one arg must be 'color'
            except Exception as e:
                raise e
        elif num_remaining_args > 2:
            raise InvalidInputException("Invalid Input: Too many input arguments.")

    except Exception as e:
        raise e
    return shape_name, sides, num_remaining_args, color, filled


def validate_and_create_shape(args):
    """Helper function for creating a Shape Object."""

    shape_name, other_args, num_remaining_args, color, filled = validate_and_parse_args(args)
    IS_NGON = shape_name == "n-gon"
    if IS_NGON:  # n-gon initializer mandatorily takes first two args as color and filled_status, contrary to others
        other_args.insert(FIRST, DEFAULT_COLOR)
        other_args.insert(SECOND, DEFAULT_FILLED_STATUS)
    if num_remaining_args > 0:  # color input
        if IS_NGON  : other_args[FIRST] = color
        else        : other_args.append(color)
    if num_remaining_args > 1:  # filled input
        if IS_NGON  : other_args[SECOND] = filled
        else        : other_args.append(filled)
    try:
        shape = switch_shape_func[shape_name](*other_args)
    except Exception as e:
        if isinstance(e, InvalidInputException):  raise e
        else:  raise InvalidInputException()
    return shape


def main():
    try:
        raw_input = input().split()
        shape = validate_and_create_shape(raw_input)

        area, perimeter, color, fill_status = \
        shape.area(), shape.perimeter(), shape.Color, shape.is_filled()
        if area is not None     :   area = "{:.2f}".format(area)  # round off to 2 decimal places
        if perimeter is not None:   perimeter = "{:.2f}".format(perimeter)
        color = color.title()  # convert to title case
        fill_status = str(fill_status).title()
        print(area, perimeter, color, fill_status)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
