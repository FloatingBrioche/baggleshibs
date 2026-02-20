import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import mock_io_p1_wins, mock_io_invalid_moves


class TestUserInterface(unittest.TestCase):
    def test_setup_and_p1_winner_scenario(self):
        interface = UserInterface(mock_io_p1_wins, Game())
        interface.set_up_game()
        interface.run()

    def test_exception_handling_scenarios(self):
        interface = UserInterface(mock_io_invalid_moves, Game())
        interface.set_up_game()
        interface.run()

# Old test case using TerminalInterfaceHelperMock
"""
       io.expect_print("Welcome to the game!")
        
        # ---------------------------------------- PLayer 1
        io.expect_print("First, we'll get things set up, starting with player 1")
        io.expect_print("So, player 1, what's your name?")
        io.provide("Eggbog")
        io.expect_print("Okay, Eggbog, let's get your ships set up.")
        

        # Set up ships
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")
        io.expect_print("  3: 3")
        io.expect_print("  4: 4")
        io.expect_print("  5: 5")
        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")
        io.expect_print("  3: 3")
        io.expect_print("  4: 4")

        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")
        io.expect_print("  3: 3")


        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            "S S S . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")


        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("4")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")


        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            "S S S . . . . . . .",
            "S S S . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")

        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("1")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            "S S S . . . . . . .",
            "S S S . . . . . . .",
            "S S . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))

        # ---------------------------------------- Player 2
        io.expect_print("Now it's your turn, player 2.")
        io.expect_print("So, player 2, what's your name?")
        io.provide("Eggbog")
        io.expect_print("Okay, Eggbog, let's get your ships set up.")
        
        # Set up ships
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")
        io.expect_print("  3: 3")
        io.expect_print("  4: 4")
        io.expect_print("  5: 5")
        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")
        io.expect_print("  3: 3")
        io.expect_print("  4: 4")

        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")
        io.expect_print("  3: 3")


        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            "S S S . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")
        io.expect_print("  2: 3")


        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("4")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")


        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            "S S S . . . . . . .",
            "S S S . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))
        io.expect_print("You have these ships remaining:")
        io.expect_print("  1: 2")

        # Prompt for ship placement 
        io.expect_print("Which ship do you wish to place?")
        io.provide("1")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.\n")

        # Set up ships
        io.expect_print("This is your board now:\n")
        io.expect_print("\n".join([
            "S S S S S . . . . .",
            "S S S S . . . . . .",
            "S S S . . . . . . .",
            "S S S . . . . . . .",
            "S S . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
            ". . . . . . . . . .",
        ]))

        io.expect_print("Alright! Now let's get down to business!")
"""