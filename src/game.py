from board import Board
from decision import Decision
import copy
import timeit

class Game:

    def get_col(self):
        valid = False
        col = 0
        while not valid:
            try:
                col = int(input('PLAYER input column: '))
            except:
                print('Only integers allowed')
            else:
                if col > 6:
                    print('Pick valid column (0-6)')
                else:
                    valid = True
        return col

    def get_depth(self):
        valid = False
        depth = 0
        while not valid:
            try:
                depth = int(input('depth: '))
            except:
                print('Only integers allowed')
            else:
                valid = True
        return depth

    def make_player_move(self, board):
        col = self.get_col()
        board.make_move(True, col)

    def make_ai_move(self, board, depth):
        decision = Decision()
        best_col = 0
        min_eval = 10000
        for col in board.get_not_full_cols():
            board_clone = copy.deepcopy(board)
            board_clone.make_move(playerToMove=False, col=col)
            eval = decision.minimax(board=board_clone, depth=depth, alpha=-10000, beta=10000, playerToMove=True)
            if eval < min_eval:
                min_eval = eval
                best_col = col
        # time.sleep(2)
        board.make_move(False, best_col)

    def get_first_mover(self):
        player_to_move = None
        valid = False
        while not valid:
            reply = str(input('PLAYER to move first? [y/n]'))
            valid = True
            if reply.lower() == 'y':
                player_to_move = True
            elif reply.lower() == 'n':
                player_to_move = False
            else:
                valid = False
        return player_to_move

    def play(self):
        playerToMove = self.get_first_mover()
        depth = self.get_depth()
        board = Board()
        board.print_board()
        times = []

        while board.get_winner() == 0:
            if playerToMove:
                game.make_player_move(board)
                playerToMove = False
            else:
                start = timeit.default_timer()
                game.make_ai_move(board, depth)
                stop = timeit.default_timer()
                print('Time spent thinking: {}'.format(stop - start))
                times.append(stop - start)
                playerToMove = True
            board.print_board()

        if board.get_winner() == 1:
            print('PLAYER wins')
        elif board.get_winner() == 2:
            print('AI wins')
        else:
            print('draw')
        times_reformatted = [float('%.4f' % i) for i in times]
        print(times_reformatted)

if __name__ == '__main__':
    game = Game()
    game.play()