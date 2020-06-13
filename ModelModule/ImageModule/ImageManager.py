from PIL import Image
import numpy as np
from typing import List

from ModelModule.ImageModule.Data.ImageView import ImageView
from ModelModule.ImageModule.Data.PointView import PointView


class ImageManager:
    @staticmethod
    def create_random_image(width: int, height: int) -> Image:
        array = ImageManager.create_random_array(width, height)
        return ImageManager.convert_to_image(array)

    @staticmethod
    def create_random_array(width: int, height: int):
        point_count: int = round((height + width) / 10)
        array = ImageManager.create_white_array(width, height)
        for i in range(point_count):
            x = np.random.randint(0, height)
            y = np.random.randint(0, width)
            array[x][y] = ImageManager.__get_black_point()
        return np.array(array, dtype=np.uint8)

    @staticmethod
    def create_white_image(width: int, height: int) -> Image:
        array = ImageManager.create_white_array(width, height)
        return ImageManager.convert_to_image(array)

    @staticmethod
    def create_white_array(width: int, height: int):
        return np.full((height, width, 3), 255, dtype=np.uint8)

    @staticmethod
    def convert_to_array(img: Image):
        return np.asarray(img)

    @staticmethod
    def convert_to_image(array) -> Image:
        return Image.fromarray(array)

    @staticmethod
    def __get_black_point():
        return [0, 0, 0]

    @staticmethod
    def image_to_imageView(image: Image) -> ImageView:
        array = ImageManager.convert_to_array(image)
        points_view: List[PointView] = []

        for x_pos, inner_list in enumerate(array):
            for y_pos, color in enumerate(inner_list):
                if color[0] != 255 and color[1] != 255 and color[2] != 255:  # is not white
                    points_view.append(PointView(x_pos, y_pos, color))

        return ImageView(points_view)


if __name__ == '__main__':
    ImageManager.create_random_image(400, 300).save("random.png")
