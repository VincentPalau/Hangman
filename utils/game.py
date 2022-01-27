class Hangman:

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']

        import random
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5
        self.word_to_find = random.choice(self.possible_words)
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = []

    def play(self):

        guessed = False

        while guessed == False and self.lives > 0:

            self.turn_count += 1

            print(f"Turn : {self.turn_count}")
            print(f"Errors : {self.error_count}")
            print(f"Remaining lives : {self.lives}")
            print(f"Correctly guessed letters : {self.correctly_guessed_letters}")
            print(f"Wrongly guessed letters : {self.wrongly_guessed_letters}")

            guess = input("Enter a letter : ")
            while len(guess) != 1:
                guess = input("Enter only a letter and only one : ")

            if guess in self.word_to_find:        
                position = []
                for i, letter in enumerate(self.word_to_find):
                    if letter == guess:
                        position.append(i)
                for index in position:
                    self.correctly_guessed_letters[index] = guess

            else:
                self.wrongly_guessed_letters += guess
                self.error_count += 1
                self.lives -= 1

            if "_" not in self.correctly_guessed_letters:
                guessed = True
                self.correctly_guessed_letters == self.word_to_find

    def start_game(self):
        self.play()
        if self.lives == 0:
            self.game_over()
        elif self.correctly_guessed_letters == list(self.word_to_find):
            self.well_played()

    def game_over(self):
        print("Game over...")

    def well_played(self):
        print(f"Good job, you found the word '{self.word_to_find}' in {self.turn_count} turns with {self.error_count} errors.")
