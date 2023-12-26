from dataclasses import dataclass
from typing import List, Optional
from games.game import BuildGameParamsDc, Game
from games.ligature import Ligature


@dataclass
class HistoryDc:
    pass


@dataclass
class DataDc:
    current_plays: int = 0  # 当前动画播放次数
    total_plays: int = 0  # 动画总播放次数
    current_round: int = 0  # 当前回合
    total_rounds: int = 0  # 总回合数


@dataclass
class BuildRoundParamsDc:
    game_params: BuildGameParamsDc
    game_handler: 'GameHandler' = None  # 游戏处理器
    build_nums: int = 1  # 生成数量
    multiple: int = 1  # 倍数
    inherit: bool = False  # 是否继承上一轮倍数等数据


@dataclass
class RoundDc:
    """
    回合数据
    """
    game_lt: List[Game]
    multiple: int = 1
    prizes: float = 0
    score: float = 0
    size: int = 0
    current: int = 0


class Round:
    def __init__(self, params: BuildRoundParamsDc):
        """
        回合
        :param params: 回合参数
        :param game_handler: 游戏处理器
        """
        self.build_params: BuildRoundParamsDc = params
        self.game_handler: 'GameHandler' = params.game_handler
        self.HANDLER = {
            Game.LIGATURE: Ligature
        }
        self.game_lt: list = []
        self.multiple: int = 1
        self.prizes: float = 0
        self.score: float = 0
        self.round_dc: Optional[RoundDc] = None
        self.build()

    def get_next_round_params(self) -> BuildRoundParamsDc:
        """
        获取下一个回合参数
        :return:
        """
        params = {}
        if self.build_params.inherit:
            params['multiple'] = self.multiple
        build_params = BuildRoundParamsDc(game_params=self.build_params.game_params, **params)
        return build_params

    def build(self):
        """
        生成回合数据
        """
        for index in range(self.build_params.build_nums):
            game_params = self.build_params.game_params
            game = self.HANDLER[game_params.mode](game_params)
            self.prizes += (game.score * self.multiple) * self.game_handler.game_state.basic_bet
            self.score += game.score
            self.game_lt.append(game)  # 生成游戏
        self.round_dc = RoundDc(game_lt=self.game_lt, multiple=self.multiple, prizes=self.prizes, score=self.score,
                                size=len(self.game_lt), current=0)
        return self

    @property
    def game_end(self):
        """
        是否结束
        :return:
        """

        return True
