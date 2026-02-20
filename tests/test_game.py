from pytest import mark, fixture, raises
from collections.abc import Iterable
from unittest.mock import Mock, patch

from lib.game import Game, InvalidTurn
from lib.player import Player
from lib.ship import Ship


@fixture
def new_game():
    return Game()

@fixture
def game_with_players():
    game = Game()
    game.add_player(1, "Fred")
    game.add_player(2, "Egg")
    return game

@fixture
def mock_ship_0_health():
    ship = Mock()
    ship.health = 0
    return ship

@fixture
def mock_ship_2_health():
    ship = Mock()
    ship.health = 2
    return ship

@fixture
def mock_board():
    mock_board = Mock()
    mock_position = Mock()
    mock_position.ship = Ship(3)
    mock_position.ship_body_index = 0            
    mock_position.fired_at = False
    mock_row = [mock_position]
    mock_board.positions = [mock_row]
    return mock_board

@fixture
def patched_player():
    with patch("lib.game.Player") as p:
        yield p


# --------------------- Tests -------------------- #

@mark.describe("__init__()")
class TestInit:
    @mark.it("Sets .player_1 and .player_2 as None")
    def test_p1(self, new_game):
        assert new_game.player_1 is None
        assert new_game.player_2 is None


@mark.describe("add_player()")
class TestAddPlayer:
    @mark.it("If 'player_num' arg is 1, sets .player_1 to new Player object")
    def test_add_p1(self, new_game):
        new_game.add_player(1, "Fred")
        assert isinstance(new_game.player_1, Player)

    @mark.it("If 'player_num' arg is 2, sets .player_2 to new Player object")
    def test_add_p2(self, new_game):
        new_game.add_player(2, "Fred")
        assert isinstance(new_game.player_2, Player)

    @mark.it("Creates players with passed 'name' arg as name attribute")
    def test_names(self, game_with_players):
        assert game_with_players.player_1.name == "Fred"
        assert game_with_players.player_2.name == "Egg"

    @mark.it("Creates players with .unplaced_ships attribute of type list")
    def test_players_have_ships(self, game_with_players):
        assert isinstance(game_with_players.player_1.unplaced_ships, list)
        assert isinstance(game_with_players.player_2.unplaced_ships, list)

    @mark.it("Returns player that has been created and added")
    def test_returns_player(self, new_game):
        output_p1 = new_game.add_player(1, "Fred")
        output_p2 = new_game.add_player(2, "Fred")
        assert output_p1 is new_game.player_1
        assert output_p2 is new_game.player_2


@mark.describe("get_turns()")
class TestGetNextPlayer:
    @mark.it("Returns iterable")
    def test_returns_iterable(self, game_with_players):
        output = game_with_players.get_turns()
        assert isinstance(output, Iterable)

    @mark.it("Iterable returns dict with 'turn', 'player' and 'opponent' keys")
    def test_iterable_returns_dict(self, game_with_players):
        turns = game_with_players.get_turns()
        first = next(turns)
        assert set(first.keys()) == set(['turn', 'player', 'opponent'])

    @mark.it("'turn' increments by one in each iteration")
    def test_turn_increments(self, game_with_players):
        turns = game_with_players.get_turns()
        first = next(turns)
        second = next(turns)
        assert first['turn'] == 1
        assert second['turn'] == 2

    @mark.it("'player and 'opponent' switch in each iteration, starting with player_1 as player")
    def test_iterable_loops(self, game_with_players):
        turns = game_with_players.get_turns()
        p1 = game_with_players.player_1
        p2 = game_with_players.player_2
        expected_players = [p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2]
        expected_opps = [p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1, p2, p1]
        first_20_turns = [next(turns) for _ in range(20)]
        tests = zip(first_20_turns, expected_players, expected_opps)
        for turn, expected_player, expected_opponent in tests:
            assert turn['player']  == expected_player
            assert turn['opponent']  == expected_opponent



@mark.describe("get_winner()")
class TestGetWinner:
    @mark.it("Returns None if neither player has destroyed all opp. ships")
    def test_no_winner(self, patched_player, new_game, mock_ship_0_health, mock_ship_2_health):
        mock_p1 = Mock()
        mock_p2 = Mock()

        mock_p1.ships = [mock_ship_2_health for _ in range(5)]
        mock_p2.ships = [mock_ship_2_health for _ in range(5)]
        patched_player.side_effect = [mock_p1, mock_p2]

        new_game.add_player(1, "Fred")
        new_game.add_player(2, "Egg")

        winner = new_game.get_winner()
        assert winner is None

    @mark.it("Returns player_1 if all of player_2's ship have 0 health")
    def test_player_1_wins(self, patched_player, new_game, mock_ship_0_health, mock_ship_2_health):
        mock_p1 = Mock()
        mock_p2 = Mock()

        mock_p1.ships = [mock_ship_2_health for _ in range(5)]
        mock_p2.ships = [mock_ship_0_health for _ in range(5)]
        patched_player.side_effect = [mock_p1, mock_p2]

        new_game.add_player(1, "Fred")
        new_game.add_player(2, "Egg")

        winner = new_game.get_winner()
        assert winner == new_game.player_1

    @mark.it("Returns player_2 if all of player_1's ship have 0 health")
    def test_player_2_wins(self, patched_player, new_game, mock_ship_0_health, mock_ship_2_health):
        mock_p1 = Mock()
        mock_p2 = Mock()

        mock_p1.ships = [mock_ship_0_health for _ in range(5)]
        mock_p2.ships = [mock_ship_2_health for _ in range(5)]
        patched_player.side_effect = [mock_p1, mock_p2]

        new_game.add_player(1, "Fred")
        new_game.add_player(2, "Egg")

        winner = new_game.get_winner()
        assert winner == new_game.player_2


@mark.describe("take_turn()")
class TestTakeTurn:
    @mark.it("Raises InvalidTurn exception if position has already been fired on")
    def test_invalid_turn(self, game_with_players):
        mock_board = Mock()
        mock_position = Mock()
        mock_position.fired_at = True
        mock_row = [mock_position]
        mock_board.positions = [mock_row]
        
        with raises(InvalidTurn, match="You've already fired at this position."):
            game_with_players.take_turn(game_with_players.player_1, mock_board, 0, 0)


    @mark.it("Returns False if no ship at target position")
    def test_returns_true_if_miss(self, game_with_players):
        mock_board = Mock()
        mock_position = Mock()
        mock_position.ship = None
        mock_position.fired_at = False
        mock_row = [mock_position]
        mock_board.positions = [mock_row]
        ship_hit = game_with_players.take_turn(game_with_players.player_1, mock_board, 0, 0)
        assert ship_hit == False

    @mark.it("Returns True if Ship at target position")
    def test_returns_true_if_hit(self, game_with_players, mock_board):
        ship_hit = game_with_players.take_turn(game_with_players.player_1, mock_board, 0, 0)
        assert ship_hit == True

    @mark.it("If ship at target position, descreases ship.health by 1")
    def test_reduce_ship_health(self, game_with_players, mock_board):
        ship = mock_board.positions[0][0].ship
        health_before = ship.health
        ship_hit = game_with_players.take_turn(game_with_players.player_1, mock_board, 0, 0)
        health_after = ship.health
        assert health_after == health_before - 1

    @mark.it("If ship at target position, sets ship.body at index to 'X'")
    def test_update_ship_body(self, game_with_players, mock_board):
        ship = mock_board.positions[0][0].ship
        ship_hit = game_with_players.take_turn(game_with_players.player_1, mock_board, 0, 0)
        assert ship.body == ['X', 'S', 'S']