from abc import ABC, abstractmethod
from dataclasses import dataclass

from handler.prob import Prob



@dataclass
class BuildGameParams:
    rows: int  # 行数
    cols: int  # 列数
    mode: str  # 模式
    prob: Prob  # 概率/随机数生成器
    winnings: 'Winnings'  # 中奖生成判定器
    wild_id: int = None  # 万能符号id
    jackpot_id: int = None  # 大奖符号id
    build_nums: int = 1  # 生成数量


class Game:
    LIGATURE = 'LIGATURE'  # 连线

    def __init__(self, params: BuildGameParams, previous_game: 'Game' = None):
        """
        游戏
        :param params: 游戏参数
        :param previous_game: 上一个游戏
        """
        self.build_params = params
        self.previous_game = previous_game
        self.build()

    @abstractmethod
    def build(self):
        """
        生成游戏数据
        """
        pass
