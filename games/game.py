from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BuildGameParams:
    rows: int  # 行数
    cols: int  # 列数
    mode: str  # 模式
    game_handler: 'GameHandler' = None  # 游戏处理器
    wild_id: int = None  # 万能符号id
    jackpot_id: int = None  # 大奖符号id
    build_nums: int = 1  # 生成数量


@dataclass
class GameData:
    matrix: list = None  # 矩阵
    winnings: list = None  # 中奖数据
    spark: list = None  # 特殊触发数据


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
        self.gamedata_lt = []
        self.score = 0
        self.winnings = params.game_handler.winnings
        self.prob = params.game_handler.prob
        self.spark = params.game_handler.spark
        self.build()

    def build(self):
        self.gamedata_lt = []
        for index in range(self.build_params.build_nums):
            gamedata, score = self.conduct()
            self.gamedata_lt.append(gamedata)
            self.score += score

    @abstractmethod
    def conduct(self) -> (GameData, int):
        """
        执行程序
        """
        pass
