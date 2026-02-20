from itertools import cycle

from lib.ship import Ship
from lib.player import Player
from lib.board import Board


class InvalidTurn(Exception):
    pass


class Game:
    def __init__(self):
        self.player_1 = None
        self.player_2 = None
        self.ship_lengths: list = [2, 3, 3, 4, 5]


    def add_player(self, player_num: int, name: str):
        ships = self._create_ships()
        board = Board()
        
        player = Player(name, ships, board)

        if player_num == 1:
            self.player_1 = player

        if player_num == 2:
            self.player_2 = player

        return player


    def get_turns(self):
        turn = 0
        player_iterator = cycle([(self.player_1, self.player_2), (self.player_2, self.player_1)])
        for p, opp in player_iterator:
            turn += 1
            yield {
                'turn': turn,
                'player': p,
                'opponent': opp
            }


    def take_turn(self, player: Player, opp_board: Board, row: int, col: int):
        target_position = opp_board.positions[row][col]

        if target_position.fired_at:
            raise InvalidTurn("You've already fired at this position.")
        
        target_position.fired_at = True
        
        if ship := target_position.ship:
            ship.health -= 1
            ship.body[target_position.ship_body_index] = 'X'
            return True
        
        return False


    def get_winner(self):
        if all(not ship.health for ship in self.player_1.ships):
            return self.player_2
        
        if all(not ship.health for ship in self.player_2.ships):
            return self.player_1      


    def _create_ships(self):
        return [Ship(x) for x in self.ship_lengths]