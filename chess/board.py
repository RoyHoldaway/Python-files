from operator import pos
import re

from numpy import append
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
                return self.try_move(position, new_piece_at_clicked_position)
            
    def select_piece(self, position, turn_value):
        piece = self.get_piece_at(position)
        if piece and self.is_correct_turn(piece, turn_value):
            self.selected_piece = piece

    def try_move(self, position, new_piece_at_clicked_position):
        if position in self.selected_piece.get_valid_moves(self):
            opposing_color = "Black" if self.selected_piece.color == "White" else "White"
            self.move_piece(self.selected_piece, position, new_piece_at_clicked_position)
            self.king_check_check(opposing_color)
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
                    if enemy.color != king.color and king.position in enemy.get_valid_moves(self):
                        #This print statement is just for unit testing
                        print("I am the " + king.color + " king and I'm in check, it is now my turn")
                        #If all are true the condition is true
                        return True
        return False

    #stepping away from the task while the king check check is functional. now we are going to be working on 
    # a checkmate function where we will have the pieces iterate through possiblities to move and evaluate 
    # if it keeps the king in check. if the move keep the king in check the move will not be a valid option. 
    # If it does take the king out of check it will keep the move as a valid option 
    def checkmate(self, color):
        #if the king is found to be in check it will check all of the pieces on our board
        if self.king_check_check(color) == True:
            for piece in self.pieces:
                #We now select only the pieces who are on our team
                #and if they have a valid move that can protect the king from the piece putting him in check
                if piece.color == color and piece.type != "king":
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
                            print("Move found that gets king out of check")
                            return False
            return True

        

    def get_piece_at(self,position):
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def is_correct_turn(self, piece, turn_value):
        return piece.color == ("White" if turn_value % 2 == 1 else "Black")

    def move_piece(self, piece, position, new_piece_at_clicked_position):
        piece.position = position
        if new_piece_at_clicked_position is not None:
            self.capture_piece(new_piece_at_clicked_position)

        if piece.type == "pawn":
            #checks if the pawn should be promoted by checking position on the board
            promotion_row = 0 if piece.color == "White" else 7
            if piece.position[0] == promotion_row:
                self.pending_promotion = piece
            
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