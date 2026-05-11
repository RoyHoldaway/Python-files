import pygame
from pieces import Pawn, Rook, Bishop, Knight, Queen, King

#Build the board and display pieces on it
class Board:
    def __init__(self):
        #initialize board details
        self.rows = 8
        self.cols = 8
        self.cell_size = 80
        #initialie pieces and captured pieces
        self.pieces = []
        self.selected_piece = None
        self.captured_w_pieces = []
        self.captured_b_pieces = []
        self.en_passant_target = None

        #This now instead will make the self of the class for pieces to append a white rook at position 7,0
        #This will make our 2 long linees into multiple seperate lines but also establishes objects to each piece
        #Without having to create entities for them individually.
        self.pieces.append(Rook("White", (7, 0)))
        self.pieces.append(Knight("White", (7, 1)))
        self.pieces.append(Bishop("White", (7, 2)))
        self.pieces.append(Queen("White", (7, 3)))
        self.pieces.append(King("White", (7, 4)))
        self.pieces.append(Bishop("White", (7, 5)))
        self.pieces.append(Knight("White", (7, 6)))
        self.pieces.append(Rook("White", (7, 7)))
        #this for loop iterates through the range of columns which is 8 so it can add a pawn on row 6 for each column
        for cols in range(8):
            self.pieces.append(Pawn("White", (6, cols)))

        self.pieces.append(Rook("Black", (0, 0)))
        self.pieces.append(Knight("Black", (0, 1)))
        self.pieces.append(Bishop("Black", (0, 2)))
        self.pieces.append(Queen("Black", (0, 3)))
        self.pieces.append(King("Black", (0, 4)))
        self.pieces.append(Bishop("Black", (0, 5)))
        self.pieces.append(Knight("Black", (0, 6)))
        self.pieces.append(Rook("Black", (0, 7)))
        #this for loop iterates through the range of columns which is 8 so it can add a pawn on row 1 for each column
        for cols in range(8):
            self.pieces.append(Pawn("Black", (1, cols)))

    #reworked handle click to now follow this logic path
    # Has a piece been selected yet? yes?
    # select another position on the board to either capture a new piece
    # or to change pieces you want to move
        #if your second click is the same color it will change the valid moves
        #if the second click is another piece of the opposing color it will allow you to capture
    def handle_click(self, position, turn_value):
        if self.selected_piece is None:
            self.select_piece(position, turn_value)
        else:
            new_piece_at_clicked_position = self.get_piece_at(position)
            if  new_piece_at_clicked_position is not None and new_piece_at_clicked_position.color == self.selected_piece.color:
                self.select_piece(position, turn_value)
            else:
                return self.try_move(position, self.selected_piece, new_piece_at_clicked_position)
            
    def select_piece(self, position, turn_value):
        piece = self.get_piece_at(position)
        if piece and self.is_correct_turn(piece, turn_value):
            self.selected_piece = piece

    def try_move(self, position, piece, new_piece_at_clicked_position):
        if position in self.selected_piece.get_valid_moves(self):
            opposing_color = "Black" if self.selected_piece.color == "White" else "White"
            if self.check_valid_moves(position, piece.color, piece) == False:
                return False
            self.move_piece(self.selected_piece, position, new_piece_at_clicked_position, self.pieces)
            self.checkmate(opposing_color)
            self.selected_piece = None
            return True
        return False

    #This function checks for the king in the list of pieces
    def king_check_check(self, color):
        for king in self.pieces:
            if king.type == "king" and king.color == color:
                #Then lists every enemy piece by opposing color
                for enemy in self.pieces:
                    # if the enemy pieces color is opposing the king color and the kings positoin is inside any enemy moves
                    if enemy.color != king.color and enemy.type != "king" and king.position in enemy.get_valid_moves(self):
                        #If all are true the condition is true
                        return True
        return False


    def checkmate(self, color):
        print("in checkmate, king in check:", self.king_check_check(color))
        #if the king is found to be in check it will check all of the pieces on our board
        if self.king_check_check(color) == True:
            for piece in self.pieces:
                #We now select only the pieces who are on our team
                #and if they have a valid move that can protect the king from the piece putting him in check
                if piece.color == color:
                    for moves in piece.get_valid_moves(self):
                        #establish local variable for piece positions
                        original_position = piece.position
                        #associate positions with the possible moves
                        removed_piece = self.get_piece_at(moves)
                        # Simulate the move and check if the king is still in check
                        piece.position = moves
                        #if the move results in the king being out of check
                        if removed_piece is not None: 
                            self.pieces.remove(removed_piece)
                        still_in_check = self.king_check_check(color)
                        piece.position = original_position
                        if removed_piece is not None:
                            self.pieces.append(removed_piece)
                        if not still_in_check:
                            print("escape found:", piece.type, "to", moves)
                            return False
            print("Checkmate!")
            print("The game is over. " + color + " has lost.")
            pygame.quit()
            return True

    #King check check checks for the king, then checks if he is in valid opponent moves
    # to ensure the move the opponent can make is going to take king out of check via blocking
    # or moving the king, I will need to call a new function to check valid moves
    #  This function will be called after king check check and before check mate to 
    # ensure there are no valid moves for the king or other pieces to take to escape check
    def check_valid_moves(self, position, color, piece):
        #establish local variable for piece positions
        original_position = piece.position
          #associate positions with the possible moves
        removed_piece = self.get_piece_at(position)
          # Simulate the move and check if the king is still in check
        piece.position = position
            #if the move results in the king being out of check
        if removed_piece is not None:
            self.pieces.remove(removed_piece)
        still_in_check = self.king_check_check(color)
        piece.position = original_position
        if removed_piece is not None:
            self.pieces.append(removed_piece)
        if still_in_check:
            return False
        return True

    def get_piece_at(self,position):
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def is_correct_turn(self, piece, turn_value):
        return piece.color == ("White" if turn_value % 2 == 1 else "Black")

    def move_piece(self, piece, position, new_piece_at_clicked_position, pieces):
        original_position = piece.position
        stored_en_passant_target = self.en_passant_target

        piece.position = position
        if piece.type == "pawn" and abs(position[0] - original_position[0]) == 2:
            self.en_passant_target = (position[0] + 1 if piece.color == "White" else position[0] - 1, position[1])
            print("En passant target set to:", self.en_passant_target)
        else:
            self.en_passant_target = None

        if piece.type == "pawn" and position == stored_en_passant_target:
            capture_pawn = self.get_piece_at((original_position[0], position[1]))
            if capture_pawn is not None:
                self.capture_piece(capture_pawn)

        if piece.type == "pawn":
            #checks if the pawn should be promoted by checking position on the board
            promotion_row = 0 if piece.color == "White" else 7
            if piece.position[0] == promotion_row:
                self.pending_promotion = piece

        if new_piece_at_clicked_position is not None:
            self.capture_piece(new_piece_at_clicked_position)

        if piece.type == "king" or piece.type == "rook":
            piece.has_moved = True

        if piece.type == "king" and abs(position[1] - original_position[1]) == 2:
            king_color = piece.color
            king_piece = piece
            if position [1] > original_position[1]: 
                for piece in self.pieces:
                    if isinstance(piece, Rook) and piece.has_moved == False and piece.color == king_color and piece.starting_position == (7,7):
                        piece.position = (7,5)
                        piece.has_moved = True
                        king_piece.has_moved = True
                    elif isinstance(piece, Rook) and piece.has_moved == False and piece.color == king_color and piece.starting_position == (0,7):
                            piece.position = (0,5)
                            piece.has_moved = True
                            king_piece.has_moved = True
            else: 
                for piece in self.pieces:
                    if isinstance(piece, Rook) and piece.has_moved == False and piece.color == king_color and piece.starting_position == (7,0):
                        piece.position = (7,3)
                        piece.has_moved = True
                        king_piece.has_moved = True
        
                    else:
                        if isinstance(piece, Rook) and piece.has_moved == False and piece.color == king_color and piece.starting_position == (0,0):
                            piece.has_moved = True
                            king_piece.has_moved = True
                            piece.position = (0,3)



    def draw_board(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def draw_pieces(self, screen):
        for piece in self.pieces:
            x = piece.position[1] * self.cell_size
            y = piece.position[0] * self.cell_size
            if piece == self.selected_piece:
                pygame.draw.rect(screen, (0, 255, 0),
                    (x, y, self.cell_size, self.cell_size), 3)
            screen.blit(piece.image, (x, y))

    def draw_valid_moves(self, screen):
        if self.selected_piece:
            moves = self.selected_piece.get_valid_moves(self)
            for move in moves:
                x = move[1] * self.cell_size
                y = move[0] * self.cell_size
                pygame.draw.rect(screen, (0, 255, 0), (x, y, self.cell_size, self.cell_size), 3)

    def capture_piece(self, piece):
        if self.selected_piece.color == "White" and piece.color == "Black":
            self.captured_b_pieces.append(piece)
            self.pieces.remove(piece)
            return True
        else:
            self.captured_w_pieces.append(piece)
            self.pieces.remove(piece)
            return True