from dataclasses import dataclass
from typing import Union

import numpy as np
from numpy import ndarray

from games.game import Game
from handler.prob import Prob


@dataclass
class BuildMatrixParams:
    prob: Prob
    mode: str = Game.LIGATURE  # 生成类型
    rows: int = 10  # 行数
    cols: int = 10  # 列数


class Matrix:
    def __init__(self, params: BuildMatrixParams, previous_matrix: 'Matrix' = None):
        """
        回合
        :param params: 生成矩阵参数
        :param previous_matrix: 上一轮矩阵数据
        """
        self.build_params = params
        self.previous_matrix = previous_matrix
        self.HANDLER = {
            Game.LIGATURE: self.build_ligature
        }
        self.matrix = []
        self.build()

    def build(self) -> 'Matrix':
        """
        生成矩阵
        """
        self.HANDLER[self.build_params.mode]()
        return self

    def build_ligature(self):
        _mx = np.zeros((self.build_params.rows, self.build_params.cols), dtype=int)
        for row in range(self.build_params.rows):
            for col in range(self.build_params.cols):
                _mx[row, col] = self.build_params.prob.gen_symbol()
        self.matrix = _mx

    @staticmethod
    def find_vals(coords: list, matrix: list) -> ndarray:
        """
        查找坐标对应的值
        """
        _coords = Matrix.to_ndarray(coords)
        _matrix = Matrix.to_ndarray(matrix)
        result = _matrix[_coords[:, 0], _coords[:, 1]]
        return result

    @staticmethod
    def find_continuous_repeated(arr, n=None) -> Union[int, None]:
        """找出n的连续重复数量,如果n为None，返回第一个元素的连续数量"""
        arr = Matrix.to_ndarray(arr)
        if n is not None and arr[0] != n:
            return None
        # 找到第一个和第一个元素不同的元素的索引
        first_different_index = np.argmax(arr != arr[0])
        # 如果整个数组都由相同的元素组成，返回该元素和它在数组中的数量
        return first_different_index or len(arr)

    @staticmethod
    def to_ndarray(arr) -> ndarray:
        # 如果不是numpy数组，转换为numpy数组
        if not isinstance(arr, ndarray):
            arr = np.array(arr)
        return arr

    @staticmethod
    def count_occurrences(arr, n) -> (int, list):
        """统计n在arr中出现的次数"""
        arr = Matrix.to_ndarray(arr)
        mask = arr == n
        count = np.count_nonzero(arr == n) or 0
        coords = np.argwhere(mask)
        return count, coords.tolist()
