import pygame
from board import Board
from promotion import promotionMenu
from constraints import Constraints
from pieces import Pawn, Rook, Bishop, Knight, Queen, King

class AI:
    def __init__(self):
        
        piece_values = {
            "King": 99999,
            "Queen": 900,
            "Bishop": 300,
            "Rook": 500,
            "Knight": 300,
            "Pawn": 100
        }
        self.piece_values = piece_values

    def evaluate_board(self, board):
        cpu_value = 0
        enemy_value = 0
        for piece in board.pieces:
            if piece:
                if piece.color == "Black":
                    cpu_value += self.piece_values.get(piece.type, 0)
                else:
                    enemy_value += self.piece_values.get(piece.type, 0)
        return cpu_value - enemy_value
    
    def minimax(self, board, depth, maximizing, alpha, beta):
        if depth == 0:
            return self.evaluate_board(board)
        if maximizing:
            bestValue = float('-inf')
            for piece in board.pieces:
                if piece.color == "Black":
                    for moves in piece.get_valid_moves(board):
                        #establish local variable for piece positions
                        original_position = piece.position
                        #associate positions with the possible moves
                        removed_piece = board.get_piece_at(moves)
                        #Simulate the move and check the boards score
                        piece.position = moves
                        if removed_piece is not None: 
                            board.pieces.remove(removed_piece)
                        #insert recursive function here
                        value = self.minimax(board, depth-1, False, alpha, beta)
                        bestValue = max(bestValue, value)
                        alpha = max(alpha, bestValue)
                        if beta <= alpha:
                            break
                        #return piecese to their original location after testing has completed
                        piece.position = original_position
                        if removed_piece is not None:
                            board.pieces.append(removed_piece)
                    return bestValue
        else:
            bestValue = float('inf')
            for piece in board.pieces:
                if piece.color == "White":
                    for moves in piece.get_valid_moves(board):
                        #establish local variable for piece positions
                        original_position = piece.position
                        #associate positions with the possible moves
                        removed_piece = board.get_piece_at(moves)
                        #Simulate the move and check the boards score
                        piece.position = moves
                        if removed_piece is not None: 
                            board.pieces.remove(removed_piece)
                        #insert recursive function here
                        value = self.minimax(board, depth-1, True, alpha, beta)
                        bestValue = min(bestValue, value)
                        beta = min(beta, bestValue)
                        if beta <= alpha:
                            break
                        #return piecese to their original location after testing has completed
                        piece.position = original_position
                        if removed_piece is not None:
                            board.pieces.append(removed_piece)
                    return bestValue
                
    def get_best_move(self, board, depth):
        best_move = None
        best_score = float('-inf')
        for piece in board.pieces:
            if piece.color == "Black":
                for moves in piece.get_valid_moves(board):
                    #store original piece positoins
                    original_position = piece.position
                    #store removed pieces
                    removed_piece = board.get_piece_at(moves)
                    #iterate through moves
                    piece.position = moves
                    #temporarily remove stored removed piece
                    if removed_piece is not None:
                        board.pieces.remove(removed_piece)

                    score = self.minimax(board, depth, False, float('-inf'), float('inf'))
                    if score > best_score:
                        best_score = score
                        best_move = (piece, moves)

                    piece.position = original_position


                    if removed_piece is not None:
                        board.pieces.append(removed_piece)

        return best_move