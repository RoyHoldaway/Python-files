import pygame
from pieces.piece import piece

#Knight class
class Knight(piece):
    def __init__(self, color, position):
        super().__init__("knight", color, position, "Knight")
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wN.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bN.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        self.starting_position = position

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        #declared all possible directions the knight could go
        #Since the knight moves by going up down left or right by 2 and then up or down or left or right an additional 1 spot i had to declare all options for
        #these possibilities.
        direction_all = ((row+2, col+1), (row+2, col-1), 
                         (row+1, col+2), (row+1, col-2), 
                         (row-1, col+2), (row-1, col-2), 
                         (row-2, col+1), (row-2, col-1) )
        for position in direction_all:
            if board.get_piece_at(position) is None:
                moves.append(position)
            elif board.get_piece_at(position).color != self.color:
                moves.append(position)
        return moves
