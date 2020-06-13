from PIL.ImageTk import PhotoImage
from pubsub import pub

from ModelModule.Model import Model
from ViewModule.View import View
from PIL import Image, ImageTk


class Controller:
    __model: Model
    __view: View

    __image_width: int
    __image_height: int
    __min_image_width: int
    __min_image_height: int

    def __init__(self, view: View):
        self.__model = Model()
        self.__view = view

        self.__image_width = self.__view.get_image_width()
        self.__image_height = self.__view.get_image_height()

        self.__min_image_width = round(self.__image_width / 10)
        self.__min_image_height = round(self.__image_height / 10)

        self.init_subscribe()

    def init_subscribe(self):
        pub.subscribe(self.create_image, "create_image")
        pub.subscribe(self.init_image, "init_image")
        pub.subscribe(self.run, "run")

    def create_image(self):
        image: Image = self.__model.get_random_image(self.__min_image_width, self.__min_image_height)
        image = image.resize((self.__image_width, self.__image_height))
        self.__view.save_generated_image(image)

        ph_image = ImageTk.PhotoImage(image)
        self.__update_view_image(ph_image)

    def run(self, image):
        image = image.resize((self.__min_image_width, self.__min_image_height))
        image_view = self.__model.convert_image_to_imageView(image)
        print()

    def init_image(self):
        image: Image = self.__model.get_white_image(self.__image_width, self.__image_height)
        photo_image = ImageTk.PhotoImage(image)
        self.__update_view_image(photo_image)

    def __update_view_image(self, photo_image):
        image_label = self.__view.get_image_label()
        image_label.config(image=photo_image)
        image_label.image = photo_image
