import pygame

from pieces.rook import Rook
from .piece import Piece
from pieces import piece

#King class
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, "king")
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wK.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bK.svg')
            self.image = pygame.transform.scale(self.image, (78, 78))
        #Applies the variable of starting position for this piece object to the position variable in all uses in this object
        self.starting_position = position
        self.has_moved = False

    def get_valid_moves(self, board):
        moves = [] #sets an empty array for all possible moves to be stored
        #fills the position variable which is now the self.position variable as the row and col of the piece
        row, col = self.position
        #fills all possible directions the king could go, tried listing in a line but formatted like this made readability wildly easier
        direction_all = ((row-1, col-1), (row-1, col), (row-1, col + 1),
                         (row, col-1), (row, col + 1),
                         (row+1, col-1), (row+1, col), (row+1, col + 1) )
        #for all the positions in the directions list, if the board has no pieces on that space the king will have that space added to valid move list
        for position in direction_all:
            r, c = position
            if not (0 <= r <= 7 and 0 <= c <= 7):
                continue
            if board.get_piece_at(position) is None:
                moves.append(position)
            elif board.get_piece_at(position).color != self.color:
                moves.append(position)

            if self.has_moved == False:
                for piece in board.pieces:
                    if isinstance(piece, Rook) and piece.color == self.color and piece.has_moved == False and board.get_piece_at(position) is None:
                        if piece.starting_position == (7, 0):
                            moves.append((7, 2))
                        elif piece.starting_position == (7, 7):
                            moves.append((7, 6))
                        elif piece.starting_position == (0, 0):
                            moves.append((0, 2))
                        elif piece.starting_position == (0, 7):
                            moves.append((0, 6))

        return moves