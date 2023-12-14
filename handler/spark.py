from games.game import BuildGameParamsDc
from handler.matrix import Matrix
from handler.round import BuildRoundParamsDc


class Spark:
    COUNT_SYMBOL = 'COUNT_SYMBOL'

    def __init__(self, conf: dict, game_cof: dict):
        if not conf:
            raise 'spark config is empty'
        self.conf = conf
        self.game_conf = game_cof
        self.game_handler = None
        self.HANDLER = {
            self.COUNT_SYMBOL: self.mate_count_symbol
        }

    def mate(self, matrix: list):
        """
        匹配特殊触发
        :param matrix:
        :return:
        """
        for item in self.conf:
            handler = self.HANDLER.get(item['mode'])
            if not handler:
                continue
            if handler(item, matrix):
                self.gen_execute_params(item)

    def gen_execute_params(self, item: dict):
        """
        执行参数
        :param item:
        :return:
        """
        if item.get('freespin'):
            game_params = BuildGameParamsDc(game_handler=self.game_handler, **self.game_conf)
            round_params = BuildRoundParamsDc(game_handler=self.game_handler, game_params=game_params)

    @staticmethod
    def mate_count_symbol(item: dict, matrix: list):
        """
        匹配数量
        :param item:
        :param matrix:
        :return:
        """
        _symbol = item['symbol']
        count, coords = Matrix.count_occurrences(matrix, _symbol)
        if count < item['min']:
            return False
        return True
