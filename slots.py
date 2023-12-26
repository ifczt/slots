import os
from dataclasses import dataclass
from typing import Optional

import toml

from config.game_conf import GameConf, GameHandler
from games.game import BuildGameParamsDc
from handler.game_state import GameType, GameState
from handler.message import Message
from handler.prob import Prob
from handler.round import Round, BuildRoundParamsDc
from handler.spark import Spark
from handler.winning import Winnings
from utils import convert_keys_to_numbers


class Slots:
    def __init__(self, game_id: (int, str)):
        self.rounds = []
        self.message: Optional[Message] = None
        self.game_id = game_id
        self._config = None
        # handler ↓
        self._winnings = None
        self._prob = None
        self._spark = None
        self._game_state = None
        self.game_handler = None
        self.setup()

    def setup(self):
        """
        初始化
        :return:
        """
        path = f'config/{self.game_id}.toml'
        if not os.path.exists(path):
            raise '未找到配置文件'
        self._config = toml.load(path)
        self._winnings = Winnings(self.winnings_conf, self.game_conf)
        self._spark = Spark(self.spark_conf, self.game_conf) if self.spark_conf else None
        self._prob = Prob(self.prob_conf)
        self.game_handler = GameHandler(winnings=self._winnings, prob=self._prob, spark=self._spark)

    # region config属性
    @property
    def spark_conf(self):
        return self._config.get('spark', {})

    @property
    def game_conf(self):
        return self._config.get('game', {})

    @property
    def round_conf(self):
        return self._config.get('round', {})

    @property
    def winnings_conf(self):
        return convert_keys_to_numbers(self._config.get('winnings', {}))

    @property
    def prob_conf(self):
        return self._config.get('prob', {})

    # endregion

    def start(self, bet, bet_type=GameType.NORMAL):
        """
        开始游戏
        """
        _round = None
        self.gen_ploy(bet, bet_type)
        _game_params = BuildGameParamsDc(game_handler=self.game_handler, **self.game_conf)
        _round_params = BuildRoundParamsDc(game_params=_game_params, game_handler=self.game_handler, **self.round_conf[0])
        while True:
            _round = Round(_round_params)
            self.rounds.append(_round)
            if _round.game_end:
                break
            _round_params = _round.get_next_round_params()
        self.message = Message(self.rounds)
        self.message.send()

    def gen_ploy(self, bet, bet_type) -> GameHandler:
        """
        生成策略
        """
        self._game_state = GameState(bet=bet, game_type=bet_type)
        self.game_handler.game_state = self._game_state
        _game_handler = self.game_handler
        return _game_handler


Slots('default').start(100)
