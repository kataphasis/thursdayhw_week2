import random
# About 50% of this came from one source and 50% from another, but I made sure to spend a lot of time understanding what is going on in the code
words = ['aggravate', 'incomprehensible', 'zygote', 'frazzled', 'luxury', 'voyeurism', 'voodoo', 'phlegm', 'haphazard', 'syndrome', 'thrifty', 'buffalo', 'walkway', 'transgress', 'wellspring', 'youthful', 'disavow', 'disavow', 'jukebox', 'quixotic', 'galvanize', 'nightclub', 'zipper', 'knapsack', 'sphinx', 'zilch', 'puzzling', 'wizard', 'zigzag', 'jackpot', 'rhythm']

class hangman:
    def __init__(self, word):
        self.word = word
        self.letters = ""
    
    def main(self):
        attempts = 7
        game = hangman(random.choice(words))
        for attempt in range(1, attempts + 1):
            game.showboard()
            result = game.ask()
            if result == "Congratulations!":
                break
            print("{0} attempts used. ".format(attempt))
        print("The mans is hanged! The word was " + game.word)
    
    @property
    def grid(self):
        grid = ""
        for l in self.word:
            if l in self.letters:
                grid += l
            else:
                grid += "_"
        return grid
    
    def showboard(self):
        print("Choose: " + self.letters)
        print("Board: " + self.grid)
    
    def ask(self):
        while True:
            letter = input("Guess a letter: ")
            if letter in self.letters:
                print("You already guessed that letter!")
                continue
            

            self.letters += letter
            if letter in self.word:
                self.showboard()
                continue
            self.letters += letter
            if "_" in self.grid:
                return "nope, guess again!"
            else:
                print("Congratulations!")
                break
play = hangman(words)
play.main()