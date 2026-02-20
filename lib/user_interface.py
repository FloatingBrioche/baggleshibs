from lib.ship_placement import ShipPlacement, InvalidPlacement
from lib.game import InvalidTurn


class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game

    def set_up_game(self):
        self.io.console.clear()
        self._bar("Welcome to the Baggleshibs!")
        self._slow_write("First, we'll get things set up, starting with player 1.")
        self._set_up_player(1)
        self.io.console.clear()
        self._slow_write("Now it's your turn, player 2.")
        self._set_up_player(2)
        self._slow_write("Alright! Now let's get down to business!")
        setattr(self.game, "turns", self.game.get_turns())

    def run(self):
        while not (winner := self.game.get_winner()):
            turn = next(self.game.turns)
            opponent = turn['opponent']
            self.io.console.clear()
            self._bar(f"Turn {turn['turn']} – Current player: {turn['player'].name}")
            self._slow_write(f"{opponent.name}'s board:\n")
            opp_board = opponent.board
            self._show_board(opp_board.show_to_opp())
            self._prompt_take_turn(turn['player'], opp_board)
            self._prompt("Ready for the next player?")
        
        self._show(f"Congratulations, {winner.name}! You won!")


    def _set_up_player(self, player_num):
        name = self._prompt(f"So, player {player_num}, what's your name?")
        player = self.game.add_player(player_num, name)
        self._bar(f"Player {player_num}: {name}")
        self._slow_write(f"Okay, {name}, let's get your ships set up.")
        while player.unplaced_ships:
            self._set_up_ships(player)
        self._prompt("Ready for next player?")


    def _set_up_ships(self, player):
        ships = player.unplaced_ships
        self._slow_write("These are your unplaced ships:")
        self._show_unplaced_ships(ships)
        self._prompt_for_ship_placement(player)
        self._slow_write("This is your board now:\n")
        self._show_board(player.board.show_to_self())   

    def _show(self, message):
        self.io.write(message + "\n")

    def _slow_write(self, message):
        self.io.slow_write(message)

    def _bar(self, message):
        self.io.write_bar(message)

    def _show_board(self, board):
        self.io.show_board(board)

    def _show_unplaced_ships(self, ships):
        ship_strs = [str(ship.length) for ship in ships]
        ship_nums = [str(num) for num in range(1, len(ships) + 1)]
        self.io.show_ships(ship_strs, ship_nums)

    def _prompt(self, message, expected_input=None):
        while True:
            input = self.io.get_input(message)
            if not expected_input:
                break
            if input not in expected_input:
                self.io.write(f"Your input must be one of the following {expected_input}" + "\n")
                self.io.write("Let's try again." + "\n")
                continue
            break
        return input
    
    def _prompt_int(self, message, min, max):
        while True:
            input = self.io.get_input(message)
            try:
                input_int = int(input)
                if min < input_int < max:
                    break
                self.io.write(f"Input must be greater than {min} and less than {max}. Let's try again" + "\n")
            except:
                self.io.write("You need to input an integer here. Let's try again" + "\n")
        
        return input_int


    def _prompt_for_ship_placement(self, player):
        ships_left: int = len(player.unplaced_ships)
        max_row = player.board.rows + 1 # not inclusive
        max_col = player.board.columns + 1 # not inclusive
        chosen_ship: int = self._prompt_int("\nWhich ship do you wish to place?", 0, ships_left + 1)

        while True:
            try:
                
                orientation: str = self._prompt("Vertical (v) or horizontal (h)?", ("v", "h"))
                row: int = self._prompt_int("Which row?", 0, max_row) # not zero-indexed
                col: int = self._prompt_int("Which column?", 0, max_col) # not zero-indexed
                placement = ShipPlacement(orientation, row - 1, col - 1) # adjust for zero-indexing
                player.place_ship(chosen_ship - 1,  placement)
                break
            except InvalidPlacement as e:
                msg = e.args[0]
                self._show(f"Hmm. {msg}\n")
                self._show(f"Let's try again.\n")
        
    
    def _prompt_take_turn(self, player, opp_board):
        max_row = opp_board.rows + 1
        max_col = opp_board.columns + 1
        
        while True:
            try:
                row: int = self._prompt_int("Which row do you want to fire at?", 0, max_row)
                col: int = self._prompt_int("Which column do you want to fire at?", 0, max_col)   
                ship_hit = self.game.take_turn(player, opp_board, row - 1, col-1)
                if ship_hit:
                    self._show("\nWell done! You got 'em!\n")
                break
            except InvalidTurn as e:
                msg = e.args[0]
                self._show(f"Hmm. {msg}\n")
                self._show(f"Let's try somewhere else.\n")


