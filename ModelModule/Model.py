from PIL import Image

from External.ImageModule.ImageManager import ImageManager


class Model:
    @staticmethod
    def get_random_image(width: int, height: int) -> Image:
        return ImageManager.create_random_image(width, height)

    @staticmethod
    def get_white_image(width: int, height: int) -> Image:
        return ImageManager.create_white_image(width, height)
