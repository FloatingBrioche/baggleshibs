from dataclasses import dataclass
from lib.ship import Ship


@dataclass
class Position:
    ship: None | Ship = None
    ship_body_index: None | int = None
    fired_at: bool = False

    def show_to_self(self):
        return '.' if not self.ship else self.ship.body[self.ship_body_index]
    
    def show_to_opp(self):
        if not self.fired_at:
            return '.'
        return 'X' if self.ship else '~'
    

class Board:
    def __init__(self, rows=10, columns=10):
        self.rows: int = rows
        self.columns: int = columns
        self.positions = [
            [Position() for _ in range(columns)] for _ in range(rows)
            ]

    def show_to_self(self):
        str_positions = [
            " ".join([pos.show_to_self() for pos in row]) for row in self.positions
            ]
        return "\n".join(str_positions)
    
    def show_to_opp(self):
        str_positions = [
            " ".join([pos.show_to_opp() for pos in row]) for row in self.positions
            ]
        return "\n".join(str_positions)



