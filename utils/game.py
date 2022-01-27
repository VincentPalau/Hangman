class Hangman: # creating the nHangman class


    def __init__(self): # initializing the Hangman class
        '''Initialises the Hangman class. Sets up all the variables.'''
        
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions'] # creating a short list of words to play with
        import random # importing the random class
        self.turn_count = 0 # setting the count of turns to 0
        self.error_count = 0 # setting the count of errors to 0
        self.lives = 5 # setting the number of lives to 5
        self.word_to_find = random.choice(self.possible_words) # using the "choice" method to randomly select a word in the "possible_words" list
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find) # setting a list of strings where each element will be a letter guessed by the player
        # the number of elements must always be equal to the number of letter in the word to find
        self.wrongly_guessed_letters = [] # setting a list of strings where each element will be a letter wrongly guessed by the player


    def play(self): # Creating a new method called "play"
        '''Runs the logic of the Hangman game :
        - Asks an input from the user
        - Updates the variables of the class accordingly

        '''

        guessed = False # setting "guessed" as "False" to start the game (will be set to "True" if the player finds the word)

        while guessed == False and self.lives > 0: # as long as the word is not yet found and lives are remaining the game goes on

            self.turn_count += 1 # adding 1 to the number of turns everytime the player will guess a letter plays

            print(f"Turn : {self.turn_count}")
            print(f"Errors : {self.error_count}")
            print(f"Remaining lives : {self.lives}")
            print(f"Correctly guessed letters : {self.correctly_guessed_letters}")
            print(f"Wrongly guessed letters : {self.wrongly_guessed_letters}")
            # displaying information about the current game to the player

            guess = input("Enter a letter : ") # asks the player to type a letter
            while len(guess) != 1:
                guess = input("Enter only a letter and only one : ")
            # the player has to enter a single charachter to move on otherwise the game keeps on asking for a new input

            if guess in self.word_to_find:
            # if the player's input ("guess") is actually in the word to find
            # we enumerate over the word to find to know the position ("i") of the guessed letters
            # and store them in a list ("position")
                position = []
                for i, letter in enumerate(self.word_to_find):
                    if letter == guess:
                        position.append(i)
                for index in position:
                    self.correctly_guessed_letters[index] = guess
            # then we can replace the elements in "correctly_guessed_letters" by the player's input using their indexes according to the list "position"

            # if the input is not corresponding to any of the letters of the word to find
            # we add the input in the wrongly_guessed_letters, add 1 to the count of erros and substract 1 to the counter of lives
            else:
                self.wrongly_guessed_letters += guess
                self.error_count += 1
                self.lives -= 1
                # if the counter of lives gets to 0, the "While" loop stops

            # we check if there are remaining letters for the player to find
            # if not, the "guessed" variable is set to True which will end the "While" loop
            if "_" not in self.correctly_guessed_letters:
                guessed = True


    def start_game(self):
        '''Initializes the game by calling the "play" method than call "game_over" or "well_played" according to the output of "play".'''

        self.play()
        # once the loop in the "play" method is over the code moves on the next conditions :
        # if the number of lives is equal to 0, the "game_over" method is called
        # otherwise the "well_played" method is called
        if self.lives == 0:
            self.game_over()
        
        else:
            self.well_played()


    def game_over(self):
        '''Prints the result after what the game is ended.'''

        print("Game over...") # displays "Game over..." if called


    def well_played(self):
        '''Prints the result after what the game is ended.'''
        
        print(f"Good job, you found the word '{self.word_to_find}' in {self.turn_count} turns with {self.error_count} errors.") # displays "Good job..." if called
