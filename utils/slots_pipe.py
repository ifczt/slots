class SlotsPipe:
    def __init__(self, func: callable, **kwargs):
        """
        管道函数
        :param func:
        :param kwargs:
        """
        self.func_result: dict = func(**kwargs)

    def __or__(self, func: callable):
        self.func_result = func(**self.func_result)
        return self
