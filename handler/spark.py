from games.game import BuildGameParams
from handler.matrix import Matrix


class Spark:
    COUNT_SYMBOL = 'COUNT_SYMBOL'

    def __init__(self, conf: dict):
        if not conf:
            raise 'spark config is empty'
        self.conf = conf
        print(self.conf)

    def mate(self, matrix: list):
        """
        匹配特殊触发
        :param matrix:
        :return:
        """
        for item in self.conf:
            if item['mode'] == self.COUNT_SYMBOL:
                if self.mate_count_symbol(item, matrix):
                    game_params = BuildGameParams(rows=self.build_params.rows, cols=self.build_params.cols)
                    return True

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
