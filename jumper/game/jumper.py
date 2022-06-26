import random
import game.terminal_service

class Jumper:
    """The person falling from the sky 
    
    The responsibility of the jumper is to track the state of the parachute. 
    
    Attributes:
        terminal: an instance of TerminalService
        bad_guess_count (number): keeps track of the count of bad guesses and removes lines from the parachute
        parachute: draws the parachute
    """

    def __init__(self, terminal_service):
        """Constructs a new Jumper.

        Args:
            self (Hider): An instance of Hider.
        """
        self.terminal = terminal_service        
        self.bad_guess_count = 0
        self._parachute = [
            "  _____  ",
            " /_____\ ",
            " \     / ",
            "  \   /  ",
            "    O    ",
            "  / | \  ",
            "   / \   ",
            "         ",
            "^^^^^^^^^"
            ]
    def made_bad_guess(self):
        """Keeps track of the bad guesses' count and removes lines from the parachute.

        Args:
            self (Jumper): An instance of Jumper.
        """
        if self.bad_guess_count >= 5:
            return
        self.bad_guess_count += 1
        self._parachute.pop(0)

    def draw(self):
        """Draws the parachute.

        Args:
            self (Jumper): An instance of Jumper.
        """
        if self.bad_guess_count >= 5:
            self.terminal.write_text("    X    ") #When the bad_guess_count reaches the limit, the O for the head is replaced with an X
        for line in self._parachute:
            self.terminal.write_text(line)


