from dataclasses import dataclass
from typing import Union

import numpy as np
from numpy import ndarray


class BuildType:
    LIGATURE = 'LIGATURE'  # 连线
    RID_LIGATURE = 'RID_LIGATURE'  # 消除-连线


@dataclass
class BuildMatrixParams:
    build_type: str = BuildType.LIGATURE  # 生成类型
    row: int = 10  # 行数
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
        self.build()

    def build(self) -> 'Matrix':
        """
        生成矩阵
        """
        return self

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
