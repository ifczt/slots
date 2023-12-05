import random
from copy import copy
from typing import Union


class Prob:
    def __init__(self, conf: dict):
        if not conf:
            raise 'prob config is empty'
        self.conf = conf

    def gen_symbol(self, row: int = None, col: int = None, weight_name: str = None, exclude: list = None):
        """
        生成元素
        :param row: 行
        :param col: 列
        :param weight_name: 指定权重名称
        :param exclude: 排除元素
        :return:
        """
        weight = self.gen_weight(row, col, weight_name)
        if exclude:
            for item in exclude:
                weight.pop(item, None)
        symbol = self.choice_weighted(weight)
        return symbol

    def gen_weight(self, row: int = None, col: int = None, weight_name: str = None) -> dict:
        """
        生成权重
        :param row: 行
        :param col: 列
        :param weight_name: 指定权重名称
        :return: weight dict
        """

        def __rec_get_dict(_weight: Union[dict, list]):
            if isinstance(_weight, dict):
                return _weight
            elif isinstance(_weight, list):
                return __rec_get_dict(_weight[0])
            else:
                raise 'weight type error'

        if weight_name:
            weight = self.conf.get(weight_name)
            if not weight:
                raise f"weight_name:{weight_name} not found"
        else:
            weight = self.conf.get('symbol')

        if (row is not None) and (col is not None):
            weight = weight[row]
            if isinstance(weight, list):
                weight = weight[col]
        elif (row is not None) or (col is not None):
            weight = weight[row if row is not None else col]
        else:
            weight = __rec_get_dict(weight)

        return copy(weight)

    @staticmethod
    def choice_weighted(d):
        """根据权重字典随机选择一个key"""
        keys = list(d.keys())
        weights = list(d.values())
        return random.choices(keys, weights=weights, k=1)[0]
