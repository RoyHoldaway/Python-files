import pygame
from pieces.rook import Rook
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
        self.has_moved = False

    def get_attack_squares(self, board):
        """Raw squares the king threatens — no check validation, avoids recursion."""
        moves = []
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for dr, dc in directions:
            r, c = self.position[0] + dr, self.position[1] + dc
            if 0 <= r < 8 and 0 <= c < 8:
                piece_there = board.get_piece_at((r, c))
                if piece_there is None or piece_there.color != self.color:
                    moves.append((r, c))
        return moves

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        direction_all = (
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1),                  (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        )
        for position in direction_all:
            r, c = position
            if not (0 <= r < 8 and 0 <= c < 8):
                continue
            piece_there = board.get_piece_at(position)
            if piece_there is None or piece_there.color != self.color:
                moves.append(position)
    
        # Castling
        if self.has_moved == False:
            for piece in board.pieces:
                if isinstance(piece, Rook) and piece.color == self.color and piece.has_moved == False:
                    if piece.starting_position == (7, 0) and board.get_piece_at((7,2)) is None:
                        moves.append((7, 2))
                    elif piece.starting_position == (7, 7) and board.get_piece_at((7,6)) is None:
                        moves.append((7, 6))
                    elif piece.starting_position == (0, 0) and board.get_piece_at((0,2)) is None:
                        moves.append((0, 2))
                    elif piece.starting_position == (0, 7) and board.get_piece_at((0,6)) is None:
                        moves.append((0, 6))
    
        # Remove squares attacked by the enemy king
        enemy_king = None
        for piece in board.pieces:
            if piece.type == "king" and piece.color != self.color:
                enemy_king = piece
                break
            
        if enemy_king is not None:
            enemy_king_attacks = enemy_king.get_attack_squares(board)
            moves = [m for m in moves if m not in enemy_king_attacks]
    
        return moves