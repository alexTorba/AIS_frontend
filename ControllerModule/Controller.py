from PIL.ImageTk import PhotoImage
from pubsub import pub

from ModelModule.Model import Model
from ViewModule.View import View
from PIL import Image, ImageTk


class Controller:
    __model: Model
    __view: View

    __image_width: int
    _image_height: int

    def __init__(self, view: View):
        self.__model = Model()
        self.__view = view
        self.__image_width = self.__view.get_image_width()
        self._image_height = self.__view.get_image_height()
        self.init_subscribe()

    def init_subscribe(self):
        pub.subscribe(self.create_image, "create_image")
        pub.subscribe(self.init_image, "init_image")

    def create_image(self):
        p_width: int = round(self.__image_width / 3)
        p_height: int = round(self._image_height / 3)
        image: Image = self.__model.get_random_image(p_width, p_height)
        image = image.resize((self.__image_width, self._image_height))
        photo_image = ImageTk.PhotoImage(image)
        self.__update_view_image(photo_image)

    def init_image(self):
        image: Image = self.__model.get_white_image(self.__image_width, self._image_height)
        photo_image = ImageTk.PhotoImage(image)
        self.__update_view_image(photo_image)

    def __update_view_image(self, ph_image: PhotoImage):
        image_label = self.__view.get_image_label()
        image_label.config(image=ph_image)
        image_label.image = ph_image
