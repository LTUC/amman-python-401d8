from game_logic import GameLogic
from banker import Banker


class Game:

    def __init__(self, roller= None):
        self.round = 0
        self.total = 0
        self.banker = Banker()
        self.roller = roller or GameLogic.roller

    def play():
        pass

    # Playing the game
    # 1- print welcome message
    # 2- ask the user to choose to play or not (y/n)

    # Starting the game
    # 3- Rolling
    # 4- Ask the player to choose(dice or q) => this will be sent to be calculated
    # 5- update and show total score of the round
    # 6- Ask (r, b, q)
    # 7- if r : roller()
    #    if b: show total score --> bank
    #    if q: call the quit function(or just quit)
    # Quitting:
    #   Show the total score 
    #   print a thanks message
    # Banking:
    #   - save the current score total
    #   - show the banked points
    #   - clear the shelf
    #   - show the total
    #   - go back to step 3 (starting the game)


# game = Game()