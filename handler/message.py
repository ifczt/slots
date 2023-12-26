from typing import Dict, List

from handler.round import Round


class Message:
    def __init__(self, rounds: list):
        self.rounds: List[Round] = rounds
        self.index = 0

    def send(self, index: int = None):
        """
        发送消息
        :param index: 回合索引
        """
        index = index or self.index
        if index >= len(self.rounds):
            raise 'index out of range'
        _rounds = self.rounds[index]
        print(_rounds.prizes, _rounds.score)
        [print(game.gamedata_lt) for game in _rounds.game_lt]

    def inc_send(self):
        """
        递增发送消息
        """
        self.send(self.index)
        self.index += 1
