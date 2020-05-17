from ModelModule.Model import Model


class Controller:
    model: Model

    def __init__(self):
        self.model = Model()
