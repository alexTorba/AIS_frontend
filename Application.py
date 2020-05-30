from ControllerModule.Controller import Controller
from ViewModule.View import View


class Application:
    view: View
    controller: Controller

    def __init__(self):
        self.view = View()
        self.controller = Controller(self.view)

    def run(self):
        self.view.start()
