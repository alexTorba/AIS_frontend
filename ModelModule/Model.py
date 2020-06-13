from PIL import Image

from ModelModule.ImageModule.Data.ImageView import ImageView
from ModelModule.ImageModule.ImageManager import ImageManager


class Model:
    @staticmethod
    def get_random_image(width: int, height: int) -> Image:
        return ImageManager.create_random_image(width, height)

    @staticmethod
    def get_white_image(width: int, height: int) -> Image:
        return ImageManager.create_white_image(width, height)

    @staticmethod
    def convert_image_to_imageView(image: Image) -> ImageView:
        return ImageManager.image_to_imageView(image)
