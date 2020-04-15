class Light(object):
    def __init__(self) -> None:
        self.light = False

    def on(self):
        self.light = True

    def off(self):
        self.light = False
