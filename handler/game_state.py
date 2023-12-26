from dataclasses import dataclass


class GameType:
    NORMAL = 'NORMAL'  # 普通游戏


@dataclass
class GameState:
    total_rounds: int = 0  # 总回合数
    current_round: int = 0  # 当前回合
    bet: int = 0  # 投注
    deduct_bet: bool = False  # 是否扣除投注
    game_type: str = GameType.NORMAL  # 游戏类型
    bet_multiple: int = 1  # 投注倍数

    @property
    def basic_bet(self):
        return round(self.bet / self.bet_multiple)
