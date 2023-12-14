from dataclasses import dataclass
from typing import Optional

from config.game_conf import GameConf
from handler.message import Message
from handler.prob import Prob
from handler.round import Round, BuildRoundParams
from handler.spark import Spark
from handler.winning import Winnings


class Slots:
    def __init__(self, game_id: int):
        self.rounds = []
        self.message: Optional[Message] = None
        self.game_conf = GameConf(game_id)

    def start(self):
        """
        开始游戏
        """
        _round = None
        _round_params = None
        while True:
            round_params = _round_params or self.game_conf.build_round_params
            _round = Round(round_params)
            self.rounds.append(_round)
            if _round.game_end:
                break
            _round_params = _round.get_next_round_params()
        self.message = Message(self.rounds)
        self.message.send()


Slots(50).start()
