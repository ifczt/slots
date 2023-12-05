from games.game import Game, BuildGameParams
from handler.matrix import Matrix, BuildMatrixParams
from utils.slots_pipe import SlotsPipe


class Ligature(Game):
    def __init__(self, params: BuildGameParams, previous_game: 'Game' = None):
        super().__init__(params, previous_game)

    def build(self):
        for index in range(self.build_params.build_nums):
            self.conduct()

    def conduct(self):
        matrix_params = BuildMatrixParams(rows=self.build_params.rows, cols=self.build_params.cols, mode=self.build_params.mode,prob=self.build_params.prob)
        matrix = Matrix(matrix_params)
        winnings = self.build_params.winnings.mate(matrix.matrix)
        return self
