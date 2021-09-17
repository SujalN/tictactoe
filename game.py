NUM_SPOTS, NUM_COLS = 9, 3

class TicTacToe:
    def __init__(self):
        self.board = [' ' for spot in range(NUM_SPOTS)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*NUM_COLS:(i+1)*NUM_COLS] for i in range(NUM_COLS)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def  print_board_nums():
        number_board =  [[str(i) for i in range(j*NUM_COLS, (j+1)*NUM_COLS)] for j in range(NUM_COLS)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
 
    def available_moves(self):
        return []
        moves = []
        for (i, x) in enumerate(self.board):
            pass