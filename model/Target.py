from model.Point import Point

class Target(Point):
    # GREEN = "\033[32m"
    # YELLOW = "\033[33m"

    def __init__(self, parx : float, pary : float, pardiameter : int, partarget_type : str = "None", parcolor : tuple = (255, 0, 0)):
        super().__init__(parx=parx, pary=pary, pardiameter=pardiameter, parcolor=parcolor)
        self.target_type = partarget_type

    def __str__(self) -> str:
        RED = "\033[31m"
        RESET = "\033[0m"

        info = (
            f"{RED}Target: \n"
            f"\t{RESET}X: {self.x}\n"
            f"\tY: {self.y}"
        )
        return info
