import bisect
import os
import toml
from dataclasses import dataclass, field
from typing import Union

from handler.round import BuildRoundParams
from handler.winning import Winnings
from utils import convert_keys_to_numbers


class GameConf:
    """
    游戏配置
    """

    def __init__(self, game_id: int):
        # 获取toml配置文件
        self.winning = None
        self.game_id = game_id
        path = f'config/{game_id}.toml'
        if not os.path.exists(path):
            raise '未找到配置文件'
        self.config = toml.load(path)
        print(self.config)
        self.setup()

    def setup(self):
        """
        初始化配置
        """
        self.winning = Winnings(self.config.get('winnings'), self.config.get('game'))
        print(self.winning.mate([[3, 3, 3, 5, 3], [4, 5, 6, 6, 6], [7, 8, 9, 9, 9]]))
