import pygame
from .piece import Piece

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

    def get_valid_moves(self, board):
        moves = [] #sets an empty array for all possible moves to be stored
        #fills the position variable which is now the self.position variable as the row and col of the piece
        row, col = self.position
        #fills all possible directions the king could go, tried listing in a line but formatted like this made readability wildly easier
        direction_all = ((row-1, col-1), (row-1, col), (row-1, col + 1),
                         (row, col-1), (row, col + 1),
                         (row+1, col-1), (row+1, col), (row+1, col + 1) )
        #for all the positions in the directions list, if the board has no pieces on that space the king will have that space added to valid move list

        #Had to rework kings valid moves function to enable him to properly have his moves be added and removed from the list of options.
        #to dot his the pieces had to be simulated like the checkmate function but be done to the valid moves list 
        #to shrink the amount of moves allowed for the king to escape checkmate.
        for position in direction_all:
            piece_at_position = board.get_piece_at(position)
            if piece_at_position is None:
                original_position = self.position
                self.position = position
                still_in_check = board.king_check_check(self.color)
                self.position = original_position
                if not still_in_check:
                    moves.append(position)

            elif piece_at_position.color != self.color:
                original_position = self.position
                self.position = position
                board.pieces.remove(piece_at_position)      # temporarily remove enemy
                still_in_check = board.king_check_check(self.color)
                self.position = original_position
                board.pieces.append(piece_at_position)      # restore enemy
                if not still_in_check:
                    moves.append(position)
        
        return moves