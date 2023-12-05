from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BuildGameParams:
    build_nums: int = 1  # 生成数量


class Game:
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
