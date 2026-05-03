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
        self.captured_w_pieces = []
        self.captured_b_pieces = []
        #initialize variables for path detectoin and piece selection verification
        self.selected_piece = None
        self.selected_index = None
        self.selected_position = None
        self.selected_color = None
        self.path_clear = False

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

    #click mouse
    # the handle click checks if a piece is selected already, 
    # if it is not then we select it and draw its valid moves
    # this means it also only handles clicks and captures and not changing pieces
    # to change pieces and not change turns I will need to add some sort of different state between
    #capturing and selecting the first piece. 

    #if the selected piece is not none but new selected piece is not a different color, 
    # overwrite chosen piece and choose the new one now
    def handle_click(self, position, turn_value):
        if self.selected_piece is None:
            self.select_piece(position, turn_value)
        else:
            piece_at_clicked_position = self.get_piece_at(position)
            if piece_at_clicked_position is not None and piece_at_clicked_position.color == self.selected_piece.color:
                self.select_piece(position, turn_value)
            else:
                return self.try_move(position, piece_at_clicked_position)
            
    def select_piece(self, position, turn_value):
        piece = self.get_piece_at(position)
        if piece and self.is_correct_turn(piece, turn_value):
            self.selected_piece = piece
            

    def try_move(self, position, capture_piece):
        if position in self.selected_piece.get_valid_moves(self):
            self.move_piece(self.selected_piece, position, capture_piece)
            self.selected_piece = None
            return True
        return False

    def get_piece_at(self,position):
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def is_correct_turn(self, piece, turn_value):
        return piece.color == ("White" if turn_value % 2 == 1 else "Black")

    def move_piece(self, piece, position, capture_piece):
        piece.position = position
        if capture_piece is not None:
            self.capture_piece(capture_piece)

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

