from board import Board
from decision import Decision
import copy
import time

class Game:

    def make_player_move(self, board):
        col = int(input('PLAYER input column: '))
        board.make_move(True, col)

    def make_ai_move(self, board):
        decision = Decision()
        best_col = 0
        min_eval = 10000
        for col in board.get_not_full_cols():
            board_clone = copy.deepcopy(board)
            board_clone.make_move(playerToMove=False, col=col)
            eval = decision.minimax(board_clone, 3, -10000, 10000, True)
            if eval < min_eval:
                min_eval = eval
                best_col = col
        time.sleep(2)
        board.make_move(False, best_col)

    def play(self):
        playerToMove = True
        board = Board()
        board.print_board()

        while board.get_winner() == 0:
            if playerToMove:
                game.make_player_move(board)
                playerToMove = False
            else:
                game.make_ai_move(board)
                playerToMove = True
            board.print_board()

        if board.get_winner() == 1:
            print('PLAYER wins')
        elif board.get_winner() == 2:
            print('AI wins')
        else:
            print('draw')

if __name__ == '__main__':
    game = Game()
    game.play()