import doctest as dt


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        area = round(self.radius ** 2 * 3.14, 1)
        return print('The area of the circle is: {}'.format(area))

    def perimeter(self):
        perimeter = round(2 * 3.14 * self.radius, 1)
        return print('The perimeter of the circle is: {}'.format(perimeter))


def test_circle():
    """
    >>> c = Circle(5)
    >>> c.area()
    The area of the circle is: 78.5
    >>> c.perimeter()
    The perimeter of the circle is: 31.4
    """
    dt.run_docstring_examples(test_circle, globals(), True)


if __name__ == '__main__':
    test_circle()
