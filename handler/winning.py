import bisect
from dataclasses import dataclass, field
from typing import Union, List, Tuple

from handler.matrix import Matrix
from utils import convert_keys_to_numbers


@dataclass
class Winning:
    symbol: Union[int, str] = None  # 中奖元素
    count: int = 0  # 中奖数量
    score: float = 0  # 中奖分数
    coords: list = field(default_factory=list)  # 中奖坐标
    multiple: int = 1  # 倍数


class Odds:
    COUNT = 'COUNT'

    def __init__(self, conf: list):
        if not conf:
            raise 'odds config is empty'
        self.conf = conf
        self.odds_dc: dict = {}
        self.setup()

    def setup(self):
        for item in self.conf:
            item = convert_keys_to_numbers(item)
            if 'symbol' in item:
                __symbol = item.pop('symbol')
                self.odds_dc[__symbol] = item

    def mate_win(self, tp=COUNT, **kwargs):
        """
        检查是否中奖
        :param tp: 中奖类型
        :return: score 分数
        """
        match tp:
            case COUNT:
                return self.mate_count(**kwargs)

    def mate_count(self, symbol_id, count):
        """
        匹配数量
        :param symbol_id:
        :param count:
        :return:score 分数
        """
        score_dc = self.odds_dc.get(symbol_id)
        if not score_dc:
            return False

        if count not in score_dc:
            if score_dc.get('abs_match', False):
                return False
            # 向下匹配
            __keys = sorted(score_dc.keys())
            index = __keys[bisect.bisect_right(__keys, count) - 1]
            return score_dc[index] if index >= 0 else False

        return score_dc[count]


class Winnings:
    """
    中奖配置
    """
    LIGATURE = 'LIGATURE'

    def __init__(self, conf: dict, game_conf: dict = None):
        if not conf:
            raise 'winning config is empty'
        self.conf = conf
        self.game_conf = game_conf
        self.wild_id = None
        self.jackpot_id = None
        self.min = 0
        self.max = 0
        self.winning_rule: list = []
        self.group_symbols: list = []  # 群组元素
        self.wild_symbols: list = []  # 多癞子集合
        self.multiple_symbol: dict = {}
        odds_conf = conf.get('odds')
        self.odds: Odds = Odds(odds_conf)
        self.HANDLER = {
            Winnings.LIGATURE: self.mate_ligature
        }
        self.setup()

    def setup(self):
        self.winning_rule = self.conf.get('winning_rule', [])
        default = self.conf.get('default', {})
        if default:
            self.min = default.get('min', 0)
            self.max = default.get('max', 0)
            self.wild_symbols = default.get('wild_symbols', [])
            self.group_symbols = default.get('group_symbols', [])
            self.multiple_symbol = default.get('multiple_symbol', {})

        if self.game_conf:
            self.wild_id = self.game_conf.get('wild_id')
            self.jackpot_id = self.game_conf.get('jackpot_id')

    def mate(self, matrix) -> (List[Winning], float):
        """
        检查是否中奖
        :param matrix: 验证矩阵
        :return: winnings list score 分数
        """
        _winnings = []
        score = 0
        for rule in self.winning_rule:
            tp = rule.get('type', Winnings.LIGATURE)
            if tp not in self.HANDLER:
                continue
            func = self.HANDLER[tp]
            winning = func(matrix, rule)
            score += (winning.score * winning.multiple) if winning else 0
            winning and _winnings.append(winning)
        return _winnings, score

    def mate_ligature(self, matrix: list, rule: dict) -> Winning | None:
        """
        匹配线路
        :param matrix: 矩阵
        :param rule: 规则
        :return:ligature_symbol:连线元素(计算中奖元素), ligature_len:连线长度
        """
        coords = rule.get('coords')
        result = Matrix.find_vals(coords, matrix).tolist()
        ligature = []
        for symbol_id in result:
            if self.in_ligature(ligature, symbol_id):
                ligature.append(symbol_id)
            else:
                break
        ligature_len = len(ligature)
        if ligature_len < self.min:
            return None
        remove_wild_set = set(ligature) - {self.wild_id} - set(self.wild_symbols)
        ligature_symbol = list(remove_wild_set)[0] if remove_wild_set else self.wild_id
        # 判断wild的连线分数是否大于连线元素的分数
        count_wild = Matrix.find_continuous_repeated(ligature, self.wild_id) or 0
        multiple = self.clac_multiple(ligature)
        wild_odds = self.odds.mate_win(symbol_id=self.wild_id, count=count_wild) if count_wild >= self.min else 0
        odds = self.odds.mate_win(symbol_id=ligature_symbol, count=ligature_len)
        params = (self.wild_id, count_wild, wild_odds, coords[:count_wild], multiple) if wild_odds > odds else (ligature_symbol, ligature_len, odds, coords[:ligature_len], multiple)
        winning = Winning(*params)

        return winning

    def in_ligature(self, arr: list, symbol_id: int) -> bool:
        """
        判断元素是否在连线中
        :param arr:
        :param symbol_id:
        :return: bool
        """
        if not arr or symbol_id in arr:
            # 数组为空或者元素在数组中
            return True
        if symbol_id == self.wild_id or symbol_id in self.wild_symbols:
            # 元素为wild 且jackpot不在数组中
            return self.jackpot_id not in arr
        if symbol_id is not self.jackpot_id:
            # 元素不为jackpot 且数组全为wild
            return len(set(arr) - {self.wild_id} - set(self.wild_symbols)) == 0
        return False

    def clac_multiple(self, ligature: list) -> int:
        """
        计算倍数
        :param ligature:
        :return:
        """
        multiple = sum(self.multiple_symbol.get(symbol, 0) for symbol in ligature if symbol in self.multiple_symbol)
        return multiple or 1
