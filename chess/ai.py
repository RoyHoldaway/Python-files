from pieces import piece


class AI:
    def __init__(self):
        
        self.piece_values = {
            "king": 99999,
            "queen": 900,
            "bishop": 300,
            "rook": 500,
            "knight": 300,
            "pawn": 100
        }
        
    def evaluate_board(self, board):
        cpu_value = 0
        enemy_value = 0
        for piece in board.pieces:
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
                        try:
                            value = self.minimax(board, depth - 1, False, alpha, beta)
                        finally:
                         # this ALWAYS runs, even if minimax crashes
                            piece.position = original_position
                            if removed_piece is not None:
                                board.pieces.append(removed_piece)
                        #insert recursive function here
                        bestValue = max(bestValue, value)
                        alpha = max(alpha, bestValue)
                        if beta <= alpha:
                            break
            return bestValue
        else:
            bestValue = float('inf')
            for piece in list(board.pieces):
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
                        try:
                            value = self.minimax(board, depth - 1, False, alpha, beta)
                        finally:
                            # this ALWAYS runs, even if minimax crashes
                            piece.position = original_position
                            if removed_piece is not None:
                                board.pieces.append(removed_piece)
                        bestValue = min(bestValue, value)
                        beta = min(beta, bestValue)
                        if beta <= alpha:
                            break
            return bestValue
                
    def get_best_move(self, board, depth):
        best_move = None
        best_score = float('-inf')
        for piece in list(board.pieces):
            if piece.color == "Black":
                for moves in piece.get_valid_moves(board):
                    #store original piece positoins
                    original_position = piece.position
                    #store removed pieces
                    removed_piece = board.get_piece_at(moves)
                    #iterate through moves
                    piece.position = moves
                    if removed_piece is not None:
                        board.pieces.remove(removed_piece)
                    try:
                        score = self.minimax(board, depth - 1, False, float('-inf'), float('inf'))
                    finally:
                        # this ALWAYS runs, even if minimax crashes
                        piece.position = original_position
                        if removed_piece is not None:
                            board.pieces.append(removed_piece)

                    if score > best_score:
                        best_score = score
                        best_move = (piece, moves)
        print("Best move: ", best_move, " with score: ", best_score)
        return best_move