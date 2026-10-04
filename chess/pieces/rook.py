import pygame
from .piece import Piece


#Rook class
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "rook")
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wR.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bR.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        self.starting_position = position
<<<<<<< HEAD
=======
        self.has_moved = False
>>>>>>> 0b579cf289763983722f6f2329938947dac352fc

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        direction_all = ((-1, 0), 
                         (0, -1), (0, 1),
                         (1, 0) )

        for offset in direction_all:
            offset_row, offset_col = offset
            current_row, current_col = row + offset_row, col + offset_col        
            while current_col >= 0 and current_row >= 0 and current_row < 8 and current_col < 8:
                if board.get_piece_at((current_row, current_col)) is None:
                    moves.append((current_row, current_col))
                elif board.get_piece_at((current_row, current_col)).color != self.color:
                    moves.append((current_row, current_col))
                    break
                else:
                    break
                current_row += offset_row
                current_col += offset_col
<<<<<<< HEAD
=======

            if self.has_moved == False:
                pass

>>>>>>> 0b579cf289763983722f6f2329938947dac352fc
        return moves