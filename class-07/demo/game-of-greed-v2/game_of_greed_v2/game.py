

class Game:

    def __init__(self, roller = None):
        self.roller = roller

    def play(self):
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            print("Starting round 1")
            print("Rolling 6 dice...")
            rolled_dice = self.roller(6)
            nums = []
            for i in rolled_dice:
                nums.append(str(i))
            print(','.join(nums))
            # print(*rolled_dice, sep=',')
            decision = input("Enter dice to keep (no spaces), or (q)uit: ")
            print("Thanks for playing. You earned 0 points")


if __name__ == "__main__":
    from game_logic import GameLogic
    game = Game(GameLogic.roll_dice)
    game.play()