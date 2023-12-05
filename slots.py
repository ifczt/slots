
from config.game_conf import GameConf
from handler.round import Round, BuildRoundParams


class Slots:
    def __init__(self, game_id: int):
        self.rounds = []
        self.game_conf = GameConf(game_id)

    def start(self):
        """
        开始游戏
        """
        _round = None
        while True:
            _round = Round(BuildRoundParams(game_params=self.game_conf.build_game_params), _round)
            self.rounds.append(_round)
            if _round.game_end:
                break


Slots(50).start()
