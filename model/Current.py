from model.Point import Point
from model.Target import Target

class Current(Point):

    def __init__(self, parx : int, pary : int, pardiameter : int, parcolor : tuple = (255, 255, 0)):
        super().__init__(parx=parx, pary=pary, pardiameter=pardiameter, parcolor=parcolor)

    def __str__(self) -> str:
        RESET = "\033[0m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        info = (
            f"{GREEN}Current: \n"
            f"\t{RESET}X: {self.x}\n"
            f"\tY: {self.y}"
        )
        return info
