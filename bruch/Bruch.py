"""This module representantes a Bruch engl. fraction"""


class Bruch(object):
    """ Bruch

    This class acts like a full functional fraction object
    so you can invoke all youre favourite fraction operations and
    maybe try some new ones.

    :param zaehler: zaehlererator
    :param nenner: nennerominator
    :type zaehler: int
    :type nenner: int

    - **Unit Tests and Coverage**

    .. image:: _static/unit-coverage.PNG
            :align: center

    .. image:: _static/unit-passed.PNG
            :align: center

    - **Included Functions**
        Following functions / operations can be invoked

        *Addition Functionality* :func:`__add__`, :func:`__iadd__`, :func:`__radd__`

        *Substrtaction Functionality* :func:`__sub__`, :func:`__isub__`, . :func:`__rsub__`

        *Multiplikation Functionality* :func:`__mul__`, . :func:`__imul__`, . :func:`__rmul__`

        *Division Functionality* :func:`__truediv__`, . :func:`__itruediv__`, . :func:`__rdiv__`, . :func:`__rdiv__`

        *Exponential Functionality* :func:`__pow__`

        *iteratiion Functionality* :func:`__iter__`

        *Absolute Functionality* :func:`__abs__`

        *Type Conversion Functionality* :func:`__float__`, :func:`__int__`

    - **How to** use the class
        :Example: Addition of two fractions

        >>> a = new Bruch(3,4)
        >>> b = new Bruch(10,5)
        >>> a_b = a + b

        :Example: Substraktion of two fractions

        >>> a = new Bruch(3,4)
        >>> b = new Bruch(10,5)
        >>> a_b = a - b
    """

    def __init__(self, zaehler=0, nenner=1):
        """Bruch Construktor overrides init from object

        The passed parameters will be validated and if needed Errors will be raised.
        After validation the attributes zaehlererator and nennerominator will be set.

        :param zaehler: zaehlererator or if only one parameter Supplied Bruch
        :param nenner: nennerominator
        :type zaehler: int or if only one parameter Supplied Bruch
        :type nenner: int
        :raise TypeError: conflicting types, incompatible types
        :raise ZeroDivisionError: if nennerominator is 0

        .. warning:: Watch out that your Demoninator doesnt get negative
        """
        # Decide whether there are two int values passed or a Bruch Object
        if isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
            return
        elif type(zaehler) is not int or type(nenner) is not int:
            raise TypeError('conflicting types, incompatible types:')
        elif nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner

    def __str__(self):
        """Converts Object to a String

        This method overrides the __str__ method of object and converts
        the current object as a string and return that string

        :return: object displayed as string
        :rtype: string
        """
        reduced = Bruch.reduce(self.zaehler, self.nenner)
        self.zaehler //= reduced
        self.nenner //= reduced
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __add__(self, value):
        """add

        :param value: zaehlerber as int or instance of Bruch
        :type value: int or Bruch
        :return: Bruch
        :rtype: Bruch

        :Example: Addition of two fractions

        >>> a = new Bruch(3,4)
        >>> b = new Bruch(10,5)
        >>> a_b = a + b
        """
        # Create temporary used fraction
        temp = Bruch()
        if type(value) is int:
            temp.zaehler = value
            temp.nenner = 1
        elif isinstance(value, Bruch):
            temp = value
        else:
            raise TypeError('conflicting types, incompatible types'+type(value).__name__)
        return Bruch(self.zaehler*temp.nenner + temp.zaehler*self.nenner, self.nenner*temp.nenner)

    def __iadd__(self, other):
        """iadd

        :param other: Object of Bruch
        :type other: Bruch
        :return: Object of Bruch
        :rtype: Bruch
        """
        return self.__add__(other)

    def __radd__(self, other):
        """Object of Bruch is on the right hand side

        :param other: should be zaehlereric value
        :type other: int
        :return: Bruch
        :rtype: Bruch
        """
        return self.__add__(other)

    def __eq__(self, other):
        """Compare two fractions with each other

        :param other: The fraction to compare
        :type other: Bruch
        :return: True or False whether they are equal
        :rtype: bool
        """
        if type(other) is int:
            other = Bruch(other, 1)

        if not isinstance(other,Bruch):
            raise TypeError('conflicting types, incompatible types'+type(other).__name__+"should be"+type(self))
        else:
            return (self.zaehler * other.nenner) == (self.nenner * other.zaehler)

    def __float__(self):
        """Returns the Fraction as float

        :return: float
        :rtype: float
        """
        return self.zaehler/self.nenner

    def __rdiv__(self, other):
        """Divides two fractions and returns the result

        :param other:Object of Bruch
        :type other: Bruch
        :return: Bruch
        :rtype: Bruch
        """
        # raise ZeroDivisionError when own zaehlererator is ß
        if self.zaehler == 0:
            raise ZeroDivisionError("Not 0 pls")

        if type(other) is int and not 0:
            temp = Bruch(other,1)
            return Bruch(self.zaehler*temp.nenner,self.nenner*temp.zaehler)
        elif isinstance(other, Bruch):
            if other.zaehler != 0:
                return Bruch(self.zaehler*other.nenner,self.nenner*other.zaehler)
            else:
                raise ZeroDivisionError("Dont use zero pls")
        else:
            raise TypeError("conflicting types, incompatible types");

    def __rtruediv__(self, other):
        """Divides two fractions and returns the result

        :param other:Object of Bruch
        :type other: Bruch
        :return: Bruch
        :rtype: Bruch
        """
        return self.__rdiv__(other)

    def __itruediv__(self, other):
        """

        :param other:
        :return:
        """
        if not isinstance(other,Bruch) and not type(other) == int:
            raise TypeError("conflicting types, incompatible types");
        return self / other

    def __truediv__(self, other):
        """truediv

        :param other:
        :return:
        """
        return self.__rdiv__(other)

    def __iter__(self):
        """Make iteration available

        :return: iterator
        """
        iter = (self.zaehler, self.nenner).__iter__()
        return iter

    def __mul__(self, other):
        """Make Multiplikation of fractions possible

        :param other:
        :return:
        """
        if type(other) is int:
            return Bruch(self.zaehler*other, self.nenner)
        elif isinstance(other, Bruch):
            return Bruch(self.zaehler*other.zaehler, self.nenner*other.nenner)
        else:
            raise TypeError("conflicting types, incompatible types")

    def __imul__(self, other):
        """equivalent to *=

        :param other:
        :return:
        """
        return self.__mul__(other)

    def __rmul__(self, other):
        """right multiplikation

        :param other:
        :return:
        """
        return self.__mul__(other)

    def __sub__(self, value):
        """make Substraktion available

        :param other:
        :return:
        """
        # Create temporary used fraction
        temp = Bruch()
        if type(value) is int:
            temp.zaehler = value
            temp.nenner = 1
        elif isinstance(value, Bruch):
            temp = value
        else:
            raise TypeError('conflicting types, incompatible types' + type(value).__name__)
        return Bruch(self.zaehler * temp.nenner - temp.zaehler * self.nenner, self.nenner * temp.nenner)

    def __isub__(self, other):
        """isub equivalent to -=

        :param other:
        :return:
        """
        return self.__sub__(other)

    def __rsub__(self, other):
        """right version of substraktion

        :param other:
        :return:
        """
        return self.__sub__(other)

    def __ge__(self, other):
        """greater or equal to like >=

        :param other:
        :return:
        """
        if not isinstance(other, Bruch):
            raise TypeError("conflicting types, incompatible types")
        else:
            return self.zaehler * other.nenner >= self.nenner * other.zaehler

    def __gt__(self, other):
        """greater

        :param other:
        :return:
        """
        if not isinstance(other, Bruch):
            raise TypeError("inc types")
        else:
            return self.zaehler * other.nenner >= self.nenner * other.zaehler

    def __abs__(self):
        """absolute value of bruch

        :return:
        :rtype:Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __int__(self):
        """returns the float operation as int

        :return:
        :rtype: int
        """
        return int(self.__float__())

    def __invert__(self):
        """invert thr fraction object

        :return:
        :rtype:Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __neg__(self):
        """negation of the actual fraction

        :return:
        """
        return Bruch(self.zaehler*-1, self.nenner)

    def __pow__(self, power, modulo=None):
        """Takes the fraction to the power of power

        :param power: level of power
        :type power: int
        :param modulo: None
        :return: new Bruch
        :rtype: Bruch
        """
        return Bruch(self.zaehler**power, self.nenner**power)

    def __makeBruch(value):
        """generates a new Bruch object

        :return:
        :rtype: Bruch
        """
        if isinstance(value, Bruch):
            return value
        if type(value) is int:
            b = Bruch(value, 1)
            return b
        else:
            raise TypeError('conflicting types, incompatible types:')

    def reduce(a, b):
        """reduce the given Fraction

        :param int a: first value
        :param int b: second value
        :return: greatest common divisor
        """
        a = abs(a)
        b = abs(b)
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b
        return a

