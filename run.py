import sys
from time import sleep

from rich.console import Console
from rich.table import Table, Column

from lib.game import Game
from lib.user_interface import UserInterface

console = Console()

class TerminalIO:
    def __init__(self, console):
        self.console = console
    
    def get_input(self, prompt):
        return self.console.input(prompt+' ')

    def write(self, message):
        self.console.print(message)

    def write_bar(self, message):
        self.console.rule(f"[bold blue]{message}")
    
    def slow_write(self, message):
        words = message.split()
        for word in words[:-1]:
            self.console.print(word, end=' ')
            sleep(0.13)

        self.console.print(words[-1])

    def show_board(self, board):
        console.clear()

        table = Table()
        table.add_row(board)

        console.print(table)


io = TerminalIO(console)
game = Game()
user_interface = UserInterface(io, game)
user_interface.set_up_game()
user_interface.run()
