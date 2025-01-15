class Resolution:

    def __init__(self, parresolution : tuple):
        self.resolution = parresolution
        self.xsize = self.resolution[0]
        self.ysize = self.resolution[1]


    # ********** property resolution - (setter/getter) ***********
    @property
    def resolution(self) -> type:
        """ The resolution property. """
        return self.__resolution

    @resolution.setter
    def resolution(self, value: type) -> None:
        if not isinstance(value, tuple):
            raise TypeError(f"Resolution is supposed to be {tuple}, got {type(value)}")
        self.__resolution = value

    @property
    def middle_x(self) -> int:
        return int(round(self.resolution[0]/2,0))

    @property
    def middle_y(self) -> int:
        return int(round(self.resolution[1]/2,0))

    # ********** property xsize - (setter/getter) ***********
    @property
    def xsize(self) -> type:
        """ The xsize property. """
        return self.__xsize

    @xsize.setter
    def xsize(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"xsize has to be {int}, not {type(value)}")
        self.__xsize = value
    # ********** property ysize - (setter/getter) ***********
    @property
    def ysize(self) -> type:
        """ The ysize property. """
        return self.__ysize

    @ysize.setter
    def ysize(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"yszie has to be {int}, not {type(value)}")
        self.__ysize = value
