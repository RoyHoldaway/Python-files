import pygame
from pieces.piece import piece


#Queen class
class Queen(piece):
    def __init__(self, color, position):
        super().__init__("queen", color, position, "Queen")
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wQ.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bQ.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        direction_all = ((-1, -1), (-1, 0), (-1, 1),
                         (0, -1), (0, 1),
                         (1, -1), (1, 0), (1, 1) )

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
        return moves
