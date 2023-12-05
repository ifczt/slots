class Prob:
    def __init__(self, conf: dict):
        if not conf:
            raise 'prob config is empty'
        self.conf = conf
        self.setup()

    def setup(self):
        pass
