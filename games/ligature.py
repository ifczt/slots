from games.game import Game, BuildGameParamsDc, GameDataDc
from handler.matrix import Matrix, BuildMatrixParamsDc
from utils.slots_pipe import SlotsPipe


class Ligature(Game):
    def __init__(self, params: BuildGameParamsDc, previous_game: Game = None):
        super().__init__(params, previous_game)

    def conduct(self) -> (GameDataDc, int):
        matrix_params = BuildMatrixParamsDc(rows=self.build_params.rows, cols=self.build_params.cols, mode=self.build_params.mode, prob=self.prob)
        matrix = Matrix(matrix_params)
        winnings, score = self.winnings.mate(matrix.matrix)
        self.spark.mate(matrix.matrix)
        return GameDataDc(matrix=matrix.matrix, winnings=winnings), score
