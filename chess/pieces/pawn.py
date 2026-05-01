import pygame
from .piece import Piece

#Pawn class
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "pawn")
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wP.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bP.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        self.starting_position = position


    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        #declare direction so the pawns can only go forward with forward being dependend on their side of the board repsectively
        direction = -1 if self.color == "White" else 1

        #1 forward movement 1 space
        forward_pos = (row + direction, col)
        diag_pos = [(row + direction, col + 1), (row + direction, col - 1)]
        if board.get_piece_at(forward_pos) is None:
            moves.append(forward_pos)
            #2 double forward if on first move 
            if (self.color == "White") or (self.color == "Black"):
                double_forward_pos = (row + 2 * direction, col)
                if self.position == self.starting_position:
                    if board.get_piece_at(double_forward_pos) is None:
                        moves.append(double_forward_pos)
        for pos in diag_pos:
            if board.get_piece_at(pos) is not None and board.get_piece_at(pos).color != self.color:
                moves.append(pos)

        return moves

    