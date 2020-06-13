from typing import List

from External.JsonFomatterModule.JsonContract import JsonContract
from ModelModule.ImageModule.Data.PointView import PointView


class ImageView(JsonContract):
    points: List[PointView]

    __json_fields = {
        "p": "points"
    }

    def __init__(self, points: List[PointView] = None):
        super().__init__(self.__json_fields)

        if points is not None:
            self.points = points
