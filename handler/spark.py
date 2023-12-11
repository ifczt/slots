from games.game import BuildGameParams
from handler.matrix import Matrix
from handler.round import BuildRoundParams


class Spark:
    COUNT_SYMBOL = 'COUNT_SYMBOL'

    def __init__(self, conf: dict, game_cof: dict):
        if not conf:
            raise 'spark config is empty'
        self.conf = conf
        self.game_conf = game_cof
        self.game_handler = None

    def mate(self, matrix: list):
        """
        匹配特殊触发
        :param matrix:
        :return:
        """
        for item in self.conf:
            if item['mode'] == self.COUNT_SYMBOL:
                if self.mate_count_symbol(item, matrix):
                    if item.get('freespin'):
                        game_params = BuildGameParams(game_handler=self.game_handler, **self.game_conf)
                        round_params = BuildRoundParams(game_handler=self.game_handler, game_params=game_params)
                        print(round_params)
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
