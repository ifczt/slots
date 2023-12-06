from dataclasses import dataclass

from games.game import BuildGameParams, Game
from games.ligature import Ligature


@dataclass
class History:
    pass


@dataclass
class Data:
    current_plays: int = 0  # 当前动画播放次数
    total_plays: int = 0  # 动画总播放次数
    current_round: int = 0  # 当前回合
    total_rounds: int = 0  # 总回合数


@dataclass
class BuildRoundParams:
    game_params: BuildGameParams
    build_nums: int = 1  # 生成数量
    multiple: int = 1  # 倍数
    inherit: bool = False  # 是否继承上一轮倍数等数据


class Round:
    def __init__(self, params: BuildRoundParams):
        """
        回合
        :param params: 回合参数
        :param previous_round: 上一个回合
        """
        self.build_params = params
        self.HANDLER = {
            Game.LIGATURE: Ligature
        }
        self.game_lt = []
        self.game = None
        self.multiple = 1
        self.prizes = 0
        self.build()

    def get_next_round_params(self) -> BuildRoundParams:
        """
        获取下一个回合参数
        :return:
        """
        params = {}
        if self.build_params.inherit:
            params['multiple'] = self.multiple
        build_params = BuildRoundParams(game_params=self.build_params.game_params, **params)
        return build_params

    def build(self):
        """
        生成回合数据
        """
        for index in range(self.build_params.build_nums):
            game_params = self.build_params.game_params
            self.game = self.HANDLER[game_params.mode](game_params)
            self.prizes += (self.game.score * self.multiple)
            self.game_lt.append(self.game)  # 生成游戏
        return self

    @property
    def game_end(self):
        """
        是否结束
        :return:
        """

        return True
