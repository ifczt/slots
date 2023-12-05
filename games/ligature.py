from games.game import Game, BuildGameParams
from handler.matrix import Matrix, BuildMatrixParams
from utils.slots_pipe import SlotsPipe


class Ligature(Game):
    def __init__(self, params: BuildGameParams, previous_game: 'Game' = None):
        super().__init__(params, previous_game)

    def build(self):
        for index in range(self.build_params.build_nums):
            pass

    def conduct(self):
        matrix = Matrix(BuildMatrixParams())
        return self
