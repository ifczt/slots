from dataclasses import dataclass


@dataclass
class BuildMatrixParams:
    build_nums: int = 1  # 生成数量


class Matrix:
    def __init__(self, params: BuildMatrixParams, previous_matrix: 'Matrix' = None):
        """
        回合
        :param params: s参数
        :param previous_matrix: 上一个回合
        """
        self.build_params = params
        self.previous_matrix = previous_matrix
        self.build()

    def build(self):
        """
        生成回合数据
        """
        for index in range(self.build_params.build_nums):
            pass
