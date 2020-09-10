import copy

class Decision:

    def minimax(self, board, depth, alpha, beta, playerToMove):
        if depth == 0 or board.get_winner() != 0:
            return board.get_static_evaluation()

        if playerToMove:
            maxEval = -10000
            for col in board.get_not_full_cols():
                board_clone = copy.deepcopy(board)
                board_clone.make_move(playerToMove=True, col=col)
                eval = self.minimax(board_clone, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval

        else:
            minEval = 10000
            for col in board.get_not_full_cols():
                board_clone = copy.deepcopy(board)
                board_clone.make_move(playerToMove=False, col=col)
                eval = self.minimax(board_clone, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval