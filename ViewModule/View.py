from tkinter import Tk, Button, Label, Frame, TOP, BOTH, RAISED, BOTTOM, LEFT, RIGHT

from PIL.Image import Image
from pubsub import pub


class View:
    __root: Tk
    __root_height: int
    __root_width: int
    __top_frame: Frame
    __top_left_frame: Frame
    __top_right_frame: Frame
    __bottom_frame: Frame
    __last_generated_image: Image

    def __init__(self):
        self.init_UI()

    def init_UI(self):
        self.__create_root()
        self.__top_frame = self.__create_top_frame()
        self.__top_left_frame = self.__create_top_left_frame()
        self.__top_right_frame = self.__create_top_right_frame()
        self.__bottom_frame = self.__create_buttom_frame()
        self.__create_buttons()
        self.__create_label_image()

    def __create_root(self) -> None:
        self.__root = Tk()
        self.__root_height = 800
        self.__root_width = 400
        self.__root.minsize(self.__root_height, self.__root_width)
        self.__root.maxsize(self.__root_height, self.__root_width)

    def __create_top_frame(self) -> Frame:
        left_frame = Frame(self.__root, relief=RAISED, name="top_frame")
        left_frame.pack(side=TOP, fill=BOTH, expand=True)
        return left_frame

    def __create_top_left_frame(self) -> Frame:
        top_left_frame = Frame(self.__top_frame, relief=RAISED, borderwidth=1, name="top_left_frame")
        top_left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        return top_left_frame

    def __create_top_right_frame(self) -> Frame:
        top_right_frame = Frame(self.__top_frame, relief=RAISED, borderwidth=1, name="top_right_frame")
        top_right_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        return top_right_frame

    def __create_buttom_frame(self) -> Frame:
        bottom_frame = Frame(self.__root, relief=RAISED, borderwidth=2, name="bottom_frame")
        bottom_frame.pack(side=TOP, fill=BOTH, expand=True)
        return bottom_frame

    def __create_label_image(self) -> None:
        label = Label(self.__bottom_frame, name="image_label")
        label.pack(side=BOTTOM, fill=BOTH, expand=True)

    def __create_buttons(self):
        create_image_button = Button(self.__top_left_frame,
                                     name="create_image_button",
                                     text="Create image",
                                     command=self.create_image_handler)
        create_image_button.pack(side=LEFT)

        run_button = Button(self.__top_right_frame,
                            name="run_button",
                            text="Run",
                            width=10,
                            command=self.run_handler)
        run_button.pack(side=LEFT)

    @staticmethod
    def create_image_handler():
        pub.sendMessage("create_image")

    def run_handler(self):
        pub.sendMessage("run", image=self.__last_generated_image)

    def get_image_label(self):
        return self.__bottom_frame.children.get("image_label")

    def save_generated_image(self, image: Image):
        self.__last_generated_image = image

    @staticmethod
    def get_image_width() -> int:
        return 20

    @staticmethod
    def get_image_height() -> int:
        return 20

    @staticmethod
    def init_image_handler():
        pub.sendMessage("init_image")

    def start(self):
        self.init_image_handler()
        self.__root.mainloop()
