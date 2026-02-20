from pytest import fixture, mark
from lib.board import Board, Position

@fixture
def default_board():
    return Board()

@fixture
def nine_by_nine_board():
    return Board(9, 9)

class TestPosition:
    @mark.it("Inits with .ship attr as None")
    def test_inits_with_ship_attr_as_none(self):
        assert Position().ship is None

    @mark.it("Inits with .ship_body_index attr as None")
    def test_inits_with_ship_index_attr_as_none(self):
        assert Position().ship_body_index is None

    @mark.it("Inits with .fired_at attr as False")
    def test_inits_with_shot_at_attr_as_false(self):
        assert Position().fired_at is False

    @mark.it(".show_to_self() returns '.' if .ship is None")
    def test_show_to_self_returns_dot_if_no_ship(self):
        assert Position().show_to_self() == '.'

    @mark.it(".show_to_opp() returns '.' if .shot_at is False")
    def test_show_to_opp_returns_dot_if__shot_at(self):
        assert Position().show_to_opp() == '.'


class TestBoard:
    @mark.it("Inits with .positions attr of type list")
    def test_inits_with_positions_list(self, default_board):
        assert isinstance(default_board.positions, list)

    @mark.it(".positions is a matrix of Position objects")
    def test_positions_is_matrix_of_positions(self, default_board):
        positions = default_board.positions
        assert all(isinstance(x, Position) for row in positions for x in row)

    @mark.it(".positions default matrix size is 10 * 10 is Board not passed args")
    def test_inits_default_10_by_10_board_if_no_args_passed(self, default_board):
        positions = default_board.positions
        assert len(positions) == 10
        assert all(len(row) == 10 for row in positions)

    @mark.it(".positions matrix size set by passed 'rows' and 'columns' args")
    def test_inits_with_board_size_if_passed_rows_and_columns(self, nine_by_nine_board):
        positions = nine_by_nine_board.positions
        assert len(positions) == 9
        assert all(len(row) == 9 for row in positions)

    @mark.it("Inits with .rows attr equal to passed rows arg")
    def test_rows(self, default_board, nine_by_nine_board):
        assert default_board.rows == 10
        assert nine_by_nine_board.rows == 9

    @mark.it("Inits with .rows attr equal to passed rows arg")
    def test_cols(self, default_board, nine_by_nine_board):
        assert default_board.columns == 10
        assert nine_by_nine_board.columns == 9

    @mark.it(".show_to_self() returns 'empty' board if no ships placed")
    def test_show_to_self_returns_str_of_board(self, default_board):
        output = default_board.show_to_self()
        assert output == '. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .'

    @mark.it(".show_to_opp() returns 'empty' board if no shots fired")
    def test_show_to_opp_returns_str_of_board(self, default_board):
        output = default_board.show_to_opp()
        assert output == '. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .\n. . . . . . . . . .'