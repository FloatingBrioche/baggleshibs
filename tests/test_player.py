from pytest import fixture, mark, raises

from lib.player import Player, InvalidPlacement
from lib.board import Board, Position
from lib.ship import Ship
from lib.ship_placement import ShipPlacement


@fixture
def ships():
    return [
        Ship(2),
        Ship(3),
        Ship(3),
        Ship(4),
        Ship(5),
    ]


@fixture
def placements():
    return {
        "vert_9_9": ShipPlacement("v", 9, 9),
        "vert_5_5": ShipPlacement("v", 5, 5),
        "vert_4_4": ShipPlacement("v", 4, 4),
        "vert_3_4": ShipPlacement("v", 3, 4),
        "hori_9_9": ShipPlacement("h", 9, 9),
        "hori_5_5": ShipPlacement("h", 5, 5),
        "hori_2_2": ShipPlacement("h", 2, 2),
    }


@fixture
def board():
    return Board()


@fixture
def player(ships, board):
    return Player("Lil' chunky", ships, board)


@mark.describe(".__init__()")
class TestInit:
    @mark.it("Sets passed name string as .name attr")
    def test_name(self, player):
        assert player.name == "Lil' chunky"

    @mark.it("Creates .unplaced_ships attr of type list")
    def test_unplaced(self, player):
        assert isinstance(player.unplaced_ships, list)

    @mark.it(".unplaced_ships is equal to passed 'ships' list")
    def test_unplaced_eq(self, player, ships):
        assert player.unplaced_ships == ships

    @mark.it(".unplaced_ships is new deepcopied list of ships")
    def test_unplaced_copy(self, player, ships):
        assert player.unplaced_ships is not ships

    @mark.it("Creates .board attr of type Board")
    def test_board_type(self, player):
        assert isinstance(player.board, Board)

    @mark.it("Sets .board attr to passed Board object")
    def test_board_is(self, player, board):
        assert player.board is board

    @mark.it("Creates .ships attr as empty list")
    def test_empty_ships(self, player):
        assert player.ships == []

    @mark.it("Sets .shots_fired as 0")
    def test_shots(self, player):
        assert player.shots_fired == 0


@mark.describe(".place_ship()")
class TestPlaceShip:
    @mark.it("Removes ship from .unplaced_ships at passed index")
    def test_removes_ship(self, player, placements):
        ship_choice = 1
        chosen_ship = player.unplaced_ships[ship_choice]
        player.place_ship(ship_choice, placements['hori_2_2'])
        assert player.unplaced_ships[ship_choice] is not chosen_ship

    @mark.it("Appends ships to .ship")
    def test_appends_ship(self, player, placements):
        ship_choice = 1
        chosen_ship = player.unplaced_ships[ship_choice]
        player.place_ship(ship_choice, placements['hori_2_2'])
        assert player.ships[-1] is chosen_ship

    @mark.it("Updates .board.positions with ship details")
    def test_updates_positions(self, player, placements):
        player.place_ship(1, placements['hori_2_2'])
        pos_one = player.board.positions[2][2]
        pos_two = player.board.positions[2][3]
        expected_pos_one = Position(player.ships[0], 0)
        expected_pos_two = Position(player.ships[0], 1)
        assert pos_one == expected_pos_one
        assert pos_two == expected_pos_two

    @mark.it("Raises InvalidPlacement('Ship placement excedes bottom of board. Try placing the ship higher up.') exception if ship placement excedes bottom of board")
    def test_raises_excep_vertical(self, player, placements):
        with raises(
            InvalidPlacement, 
            match='Ship placement excedes bottom of board. Try placing the ship higher up.'
            ):
                player.place_ship(4, placements["vert_9_9"])
        
        with raises(
            InvalidPlacement, 
            match='Ship placement excedes bottom of board. Try placing the ship higher up.'
            ):
                player.place_ship(4, placements["vert_5_5"])

    @mark.it("Raises InvalidPlacement('Ship placement excedes right of board. Try placing the ship further left.') exception if ship placement excedes bottom of board")
    def test_raises_excep_horizontal(self, player, placements):
        with raises(
            InvalidPlacement, 
            match='Ship placement excedes right of board. Try placing the ship further left.'
            ):
                player.place_ship(4, placements["hori_9_9"])
        
        with raises(
            InvalidPlacement, 
            match='Ship placement excedes right of board. Try placing the ship further left.'
            ):
                player.place_ship(4, placements["hori_5_5"])

    @mark.it("Raises InvalidPlacement('Ships cannot overlap.') exception if ship placement overlaps previous placement")
    def test_raises_excep_overlap(self, player, placements):
        with raises(InvalidPlacement, match="Ships cannot overlap."):
                player.place_ship(0, placements["vert_4_4"])
                player.place_ship(0, placements["vert_3_4"])
        
