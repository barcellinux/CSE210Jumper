import random
from game.terminal_service import TerminalService 
class Word_list:
    """
    A list of words from where the director randomly picks the secret word
    The responsibility of the word_list is to store and display the secret word, 
    check if the guesses from the user are in the secret word, and keep track of bad guesses.

    Attributes:        
        terminal_service: For getting and displaying information on the terminal.
        list_of_words: A list of words from where the director randomly picks the secret word
        current_secret: The word currently used as puzzle
    """
    def __init__(self, terminal_service):
        """Constructs a new Word_list.
        
        Args:
            self (Word_list): an instance of Word_list.            
        """
        self.terminal_service = terminal_service
        self._list_of_words = ['computer', 'laptop', 'python', 'mouse', 'keyboard']
        self.current_secret = self._get_secret_word()

    def draw_state(self, list_of_guesses):
        """Prints the secret word and replaces its letters with '_'.
        
        Args:
            self (Word_list): an instance of Word_list.    
            list_of_guesses: a list with current letters guessed        
        """
        output = ""
        for letter in self.current_secret:
            if letter.lower() in list_of_guesses: #Loops through each letter in the secret word and checks if they have been guessed
                output = output + letter + " " #If the letter was guessed, prints it in its correct place
            else:
                output = output + "_ " #If it wasn't guessed, prints the underscore
        self.terminal_service.write_text(output)

    def get_current_secret(self):
        """Returns the current secret word.
        
        Args:
            self (Word_list): an instance of Word_list.                
        """
        return self.current_secret

    def is_letter_in_secret(self, letter):
        """Checks if the letter guessed is in the current secret word.
        
        Args:
            self (Word_list): an instance of Word_list.                
            letter (str): the letter guessed
        """
        return letter.lower() in self.current_secret.lower()    

    def is_guessed(self, letters):
        """Checks if the secret word was guessed.
        
        Args:
            self (Word_list): an instance of Word_list.                
            letters (str): the letters guessed so far
        """
        result = True
        for letter in self.current_secret:
            if not letter.lower() in letters:
                result = False
        return result

    def too_many_guesses(self, letters):
        """Keeps track of how many bad guesses.
        
        Args:
            self (Word_list): an instance of Word_list.                
            letters (str): the letters guessed so far
        """
        badGuesses = 0
        for guess in letters:
            if not guess in self.current_secret.lower():
                badGuesses += 1
        return badGuesses > 4

    def _get_secret_word(self):
        """Gets a secret word for the puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A secret word
            ]        """
        index = random.randrange(0, len(self._list_of_words))
        secretWord = self._list_of_words[index].upper()
        return secretWord
