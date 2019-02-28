class ScoreBoard:
    """Fixed-length sequence of high scores in nondecreasing order"""
    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity
        
        ALL entries are initially None
        """
        self._board = [None]* capacity      #reserve space for future scores
        self._n = 0
    
    def __getitem__(self, k):
        """return entry at index k"""
        return self._board[k]
    
    def __str__(self):
        """return string representation of the high score list"""
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    
    def add(self, entry):
        """Consider adding entry to high scores"""
        score = entry.get_score()

        #Does new entry qualify as a high score?
        #answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):      #no score drops from list
                self._n += 1                    #so overall number increases

        #shift lower scores rightward to make room for new entry
        j = self._n - 1
        while j > 0 and self._board[j-1].get_score() < score:
            self._board[j] > self._board[j-1]   #shift entry from j-1 to j
            j -= 1                              #and decrement j
        self._board[j] = entry                  #when done and new entry
        