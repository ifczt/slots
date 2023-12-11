import bisect
import os
import toml
from dataclasses import dataclass, field
from typing import Union

from games.game import BuildGameParams
from handler.prob import Prob
from handler.round import BuildRoundParams
from handler.spark import Spark
from handler.winning import Winnings
from utils import convert_keys_to_numbers


@dataclass
class GameHandler:
    winnings: Winnings
    prob: Prob
    spark: Spark


class GameConf:
    """
    游戏配置
    """

    def __init__(self, game_id: int):
        # 获取toml配置文件
        self.spark = None
        self.winnings = None
        self.prob = None
        self.game_handler = None
        self.build_game_params = None
        self.build_round_params = None
        self.game_id = game_id
        path = f'config/{game_id}.toml'
        if not os.path.exists(path):
            raise '未找到配置文件'
        self.config = toml.load(path)
        self.setup()

    @property
    def spark_conf(self):
        return self.config.get('spark', {})

    @property
    def game_conf(self):
        return self.config.get('game', {})

    @property
    def round_conf(self):
        return self.config.get('round', {})

    @property
    def winnings_conf(self):
        return self.config.get('winnings', {})

    @property
    def prob_conf(self):
        return self.config.get('prob', {})

    def setup(self):
        """
        初始化配置
        """
        self.winnings = Winnings(self.winnings_conf, self.game_conf)
        self.prob = Prob(self.prob_conf)
        self.spark = Spark(self.spark_conf, self.game_conf) if self.spark_conf else None
        self.game_handler = GameHandler(winnings=self.winnings, prob=self.prob, spark=self.spark)
        self.spark.game_handler = self.game_handler
        self.build_game_params = BuildGameParams(game_handler=self.game_handler, **self.game_conf)
        round_conf = self.round_conf
        round_conf = round_conf[0] if round_conf else {}
        self.build_round_params = BuildRoundParams(game_params=self.build_game_params, game_handler=self.game_handler, **round_conf)
