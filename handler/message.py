class Message:
    def __init__(self, rounds: list):
        self.rounds = rounds
        self.index = 0

    def send(self, index: int = None):
        """
        发送消息
        :param index: 回合索引
        """
        index = index or self.index
        if index >= len(self.rounds):
            raise 'index out of range'


    def inc_send(self):
        """
        递增发送消息
        """
        self.send(self.index)
        self.index += 1
