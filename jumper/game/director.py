from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.wordList import Word_list

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:        
        terminal_service: For getting and displaying information on the terminal.
        jumper (Jumper): The person falling from the sky
        is_playing (boolean): Whether or not to keep playing.
        word_list (Str): The word used as puzzle
        current_guesses (list): Keeps track of the letters guessed
        recent_letter (str): Stores the letter guessed
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.            
        """
        self._terminal_service = TerminalService()
        self._jumper = Jumper(self._terminal_service)
        self._is_playing = True
        self._word_list = Word_list(self._terminal_service)
        self.current_guesses = []
        self.recent_letter = ''
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()        


    def _do_outputs(self):
        """Prints the jumper and other messages on the terminal.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text('\033c')#Erases previous terminal text and keeps just the most recent text
        self._word_list.draw_state(self.current_guesses)
        self._terminal_service.write_text("")
        self._terminal_service.write_text(self.current_guesses)
        self._terminal_service.write_text("")
        self._jumper.draw()
        self._terminal_service.write_text("")        
        if self._word_list.too_many_guesses(self.current_guesses):
            self._is_playing = False
            self._terminal_service.write_text(f"Game over... The secret word was {self._word_list.current_secret}")    
        elif self._word_list.is_guessed(self.current_guesses):
            self._terminal_service.write_text("You won!")

    def _get_inputs(self):
        """Get inputs from the player

        Args:
            self (Director): An instance of Director.
        """
        #while self.recent_letter.lower() not in self.current_guesses:
        self.recent_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self.current_guesses.append(self.recent_letter.lower())  

    def _do_updates(self):
        """Checks if the player's guess was right and if the secret word has been discovered

        Args:
            self (Director): An instance of Director.
        """
        if self._word_list.is_letter_in_secret(self.recent_letter) == False:
            self._jumper.made_bad_guess()

        if self._word_list.is_guessed(self.current_guesses):            
            self._is_playing = False
            
