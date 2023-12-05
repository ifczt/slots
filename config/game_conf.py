import bisect
import os
import toml
from dataclasses import dataclass, field
from typing import Union

from games.game import BuildGameParams
from handler.prob import Prob
from handler.round import BuildRoundParams
from handler.winning import Winnings
from utils import convert_keys_to_numbers


class GameConf:
    """
    游戏配置
    """

    def __init__(self, game_id: int):
        # 获取toml配置文件
        self.winnings = None
        self.prob = None
        self.build_game_params = None
        self.game_id = game_id
        path = f'config/{game_id}.toml'
        if not os.path.exists(path):
            raise '未找到配置文件'
        self.config = toml.load(path)
        self.setup()

    def setup(self):
        """
        初始化配置
        """
        self.winnings = Winnings(self.config.get('winnings'), self.config.get('game'))
        self.prob = Prob(self.config.get('prob'))
        self.build_game_params = BuildGameParams(**self.config.get('game'), prob=self.prob, winnings=self.winnings)
        print(self.build_game_params)
