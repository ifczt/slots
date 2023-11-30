from dataclasses import dataclass

from rounds.matrix import BuildMatrixParams, Matrix


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
    build_nums: int = 1  # 生成数量


class Round:
    def __init__(self, params: BuildRoundParams, previous_round: 'Round' = None):
        """
        回合
        :param params: 回合参数
        :param previous_round: 上一个回合
        """
        self.build_params = params
        self.previous_round = previous_round
        self.build()

    def get_next_round_params(self):
        """
        获取下一个回合参数
        :return:
        """
        return self.build_params

    def build(self):
        """
        生成回合数据
        """
        _matrix = None
        for index in range(self.build_params.build_nums):
            _matrix = Matrix(BuildMatrixParams(), _matrix)

    @property
    def game_end(self):
        """
        是否结束
        :return:
        """
        return True
