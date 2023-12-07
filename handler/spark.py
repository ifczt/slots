class Spark:
    def __init__(self, conf: dict):
        if not conf:
            raise 'spark config is empty'
        self.conf = conf

    def mate(self):
        pass