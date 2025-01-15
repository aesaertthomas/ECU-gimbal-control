class Point:

    def __init__(self, parx : int, pary : int, pardiameter : int, parcolor : tuple):
        self.x = parx
        self.y = pary
        self.diameter = pardiameter
        self.radius = int(round((pardiameter/2),0))
        self.color = parcolor

    # ********** property x - (setter/getter) ***********
    @property
    def x(self) -> type:
        """ The x property. """
        return self.__x

    @x.setter
    def x(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected {int}, got {type(value)}")
        self.__x = value

    # ********** property y - (setter/getter) ***********
    @property
    def y(self) -> type:
        """ The y property. """
        return self.__y

    @y.setter
    def y(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected {int}, got {type(value)}")
        self.__y = value

    # ********** property diameter - (setter/getter) ***********
    @property
    def diameter(self) -> type:
        """ The diameter property. """
        return self.__diameter

    @diameter.setter
    def diameter(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected {int}, got {type(value)}")
        self.__diameter = value

    # ********** property radius - (setter/getter) ***********
    @property
    def radius(self) -> type:
        """ The radius property. """
        return self.__radius

    @radius.setter
    def radius(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected {int}, got {type(value)}")
        self.__radius = value

    # ********** property color - (setter/getter) ***********
    @property
    def color(self) -> type:
        """ The color property. """
        return self.__color

    @color.setter
    def color(self, value: type) -> None:
        if not isinstance(value, tuple):
            raise TypeError(f"Expected {tuple}, got {type(value)}")
        self.__color = value
