from copy import deepcopy

from lib.board import Board
from lib.ship import Ship
from lib.ship_placement import ShipPlacement, InvalidPlacement


class Player:
    def __init__(self, name: str, ships: list, board: Board):
        self.name: str = name
        self.unplaced_ships: list[Ship] = deepcopy(ships)
        self.board: Board = board
        self.ships: list = []
        self.shots_fired: int = 0

    def place_ship(self, ship_index: int, placement: ShipPlacement):
        chosen_ship = self.unplaced_ships.pop(ship_index)
        board = self.board.positions
        
        if placement.orientation == "v":
            end_index = placement.row + chosen_ship.length

            if end_index > self.board.rows - 1:
                self.unplaced_ships.insert(ship_index, chosen_ship)
                raise InvalidPlacement("Ship placement excedes bottom of board. Try placing the ship higher up.")
            
            positions = [board[placement.row + x][placement.col] for x in range(chosen_ship.length)]

        if placement.orientation == "h":
            end_index = placement.col + chosen_ship.length
            if end_index > self.board.columns - 1: 
                self.unplaced_ships.insert(ship_index, chosen_ship)
                raise InvalidPlacement("Ship placement excedes right of board. Try placing the ship further left.")
            
            positions = [board[placement.row][placement.col + x] for x in range(chosen_ship.length)]

        if any(pos.ship for pos in positions):
            self.unplaced_ships.insert(ship_index, chosen_ship)
            raise InvalidPlacement("Ships cannot overlap.")
            
        for x in range(chosen_ship.length):
            positions[x].ship = chosen_ship
            positions[x].ship_body_index = x
            
        self.ships.append(chosen_ship)
