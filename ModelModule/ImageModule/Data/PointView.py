from typing import List

from External.JsonFomatterModule.JsonContract import JsonContract


class PointView(JsonContract):
    x_pos: int  # position x
    y_pos: int  # position y
    color: List[int]  # array of 3 number

    __json_fields = {
        "x": "x_pos",
        "y": "y_pos",
        "c": "color"
    }

    def __init__(self, x_pos: int = None, y_pos: int = None, color: List[int] = None):
        super().__init__(self.__json_fields)

        if x_pos is not None:
            self.x_pos = x_pos
        if x_pos is not None:
            self.y_pos = y_pos
        if color is not None:
            self.color = color
