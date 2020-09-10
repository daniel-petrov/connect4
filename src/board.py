import pandas as pd

class Board:

    def __init__(self, rows=6, cols=7):
        if rows <= 0 or cols <= 0:
            raise Exception('Both dimensions must be greater than zero')
        self.num_rows = rows
        self.num_cols = cols
        self.player = '*'
        self.ai = 'o'
        self.none = '-'
        self.pair_value = 2
        self.triple_value = 5
        self.board_positions = [[self.none for i in range(self.num_cols)] for j in range(self.num_rows)]

    def print_board(self):
        print('   ', end='')    # 3 spaces
        for i in range(self.num_cols):
            print(i, end=' ')
        print('\n')
        for i in range(self.num_rows):
            print(i, end='  ')    # 2 spaces
            for j in range(self.num_cols):
                print(self.board_positions[i][j], end=' ')
            print()
        print()

    def make_move(self, playerToMove, col, row=0):
        if playerToMove:
            symbol = self.player
        else:
            symbol = self.ai

        if row == self.num_rows - 1:
            self.board_positions[row][col] = symbol
            return
        if self.board_positions[row + 1][col] == self.none:
            self.make_move(playerToMove, col, row+1)
        else:
            self.board_positions[row][col] = symbol

    # returns 1 if player won
    # returns 2 if ai won
    # returns 3 if draw
    # returns 0 if game is still going
    def get_winner(self):
        if self.contains_winning_combination(self.get_player_pieces()):
            return 1
        elif self.contains_winning_combination(self.get_ai_pieces()):
            return 2
        elif self.is_board_full():
            return 3
        else:
            return 0

    def get_player_pieces(self):
        player_pieces = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board_positions[row][col] == self.player:
                    player_pieces.append([row, col])
        return player_pieces

    def get_ai_pieces(self):
        ai_pieces = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board_positions[row][col] == self.ai:
                    ai_pieces.append([row, col])
        return ai_pieces

    def is_board_full(self):
        for col in range(self.num_cols):
            if self.board_positions[0][col] == self.none:
                return False
        return True

    def contains_winning_combination(self, piece_positions):
        for piece in piece_positions:
            row = piece[0]
            col = piece[1]
            horiztonal = [[row, col], [row, col+1], [row, col+2], [row, col+3]]
            result1 = all(elem in piece_positions for elem in horiztonal)

            vertical = [[row, col], [row+1, col], [row+2, col], [row+3, col]]
            result2 = all(elem in piece_positions for elem in vertical)

            right_diagonal = [[row, col], [row-1, col+1], [row-2, col+2], [row-3, col+3]]
            result3 = all(elem in piece_positions for elem in right_diagonal)

            left_diagonal = [[row, col], [row+1, col+1], [row+2, col+2], [row+3, col+3]]
            result4 = all(elem in piece_positions for elem in left_diagonal)

            if result1 or result2 or result3 or result4:
                return True
        return False

    def get_number_of_pairs(self, piece_positions):
        number_of_pairs = 0
        for piece in piece_positions:
            row = piece[0]
            col = piece[1]
            horizontal = [[row, col], [row, col+1]]
            result1 = all(elem in piece_positions for elem in horizontal)

            vertical = [[row, col], [row+1, col]]
            result2 = all(elem in piece_positions for elem in vertical)

            right_diagonal = [[row, col], [row-1, col+1]]
            result3 = all(elem in piece_positions for elem in right_diagonal)

            left_diagonal = [[row, col], [row+1, col+1]]
            reuslt4 = all(elem in piece_positions for elem in left_diagonal)

            if result1 or result2 or result3 or reuslt4:
                number_of_pairs += 1
        return number_of_pairs

    def get_number_of_triples(self, piece_positions):
        number_of_triples = 0
        for piece in piece_positions:
            row = piece[0]
            col = piece[1]
            horizontal = [[row, col], [row, col + 1], [row, col+2]]
            result1 = all(elem in piece_positions for elem in horizontal)

            vertical = [[row, col], [row + 1, col], [row+2, col]]
            result2 = all(elem in piece_positions for elem in vertical)

            right_diagonal = [[row, col], [row - 1, col + 1], [row-2, col+2]]
            result3 = all(elem in piece_positions for elem in right_diagonal)

            left_diagonal = [[row, col], [row + 1, col + 1], [row+2, col+2]]
            reuslt4 = all(elem in piece_positions for elem in left_diagonal)

            if result1 or result2 or result3 or reuslt4:
                number_of_triples += 1
        return number_of_triples

    def get_static_evaluation(self):
        player_pieces = self.get_player_pieces()
        player_score = 0
        if self.get_winner() == 1:
            player_score += 1000
        player_score += (self.get_number_of_pairs(player_pieces) * self.pair_value)
        player_score += (self.get_number_of_triples(player_pieces) * self.triple_value)

        ai_pieces = self.get_ai_pieces()
        ai_score = 0
        if self.get_winner() == 2:
            ai_score += 1000
        ai_score += (self.get_number_of_pairs(ai_pieces) * self.pair_value)
        ai_score += (self.get_number_of_triples(ai_pieces) + self.triple_value)

        return (player_score - ai_score)

    def get_board_positions(self):
        return self.board_positions

    def get_not_full_cols(self):
        return [i for i in range(self.num_cols) if self.board_positions[0][i] == self.none]