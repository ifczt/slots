from rounds.round import Round, BuildRoundParams


class Slots:
    def __init__(self):
        self.rounds = []

    def start(self):
        """
        开始游戏
        """
        _round = None
        while True:
            _round = Round(BuildRoundParams(), _round)
            self.rounds.append(_round)
            if _round.game_end:
                break
