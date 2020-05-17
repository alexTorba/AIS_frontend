from ViewModule.View import View


class Application:
    view: View

    def __init__(self):
        self.view = View()

    def run(self):
        self.view.start()
