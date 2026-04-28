#imports
import pygame

pygame.init()
width = 640
height = 640
cell_size = 80
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess.py")
clock = pygame.time.Clock()

#Build the board and display pieces on
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
    def handle_click(self, position, turn_value):
        if self.selected_piece is None:
            self.select_piece(position, turn_value)
        else:
            capture_piece = self.get_piece_at(position)
            return self.try_move(position, capture_piece)


            
    def select_piece(self, position, turn_value):
        piece = self.get_piece_at(position)
        if piece and self.is_correct_turn(piece, turn_value):
            self.selected_piece = piece
            print('selected: ', piece.type, piece.position)

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
        
        if piece.type == "Pawn" and position[0] == 0:
            promotionMenu(piece.color, position)
        elif piece.type == "Pawn" and position[0] == 7:
            promotionMenu(piece.color, position)
        
            

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
        else:
            self.captured_w_pieces.append(piece)
            self.pieces.remove(piece)




#this will be called when pawns get to row 0 or 7
class promotionMenu:
    def __init__(self, color, position):
        self.position = position
        self.color = color
        overlay = pygame.Surface((160, 160))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.drawMenu


    def promotionImages(self, screen):
        if self.color == 'White':
            #display image for Queen
            self.imagewQ = pygame.image.load('chessicons/wQ.svg')
            self.imagewQ = pygame.transform.scale(self.imagewQ, (80, 80))
            self.imagewQ = screen.blit(self.imagewQ, (240,240))
            #display image for Knight
            self.imagewN = pygame.image.load('chessicons/wN.svg')
            self.imagewN = pygame.transform.scale(self.imagewN, (80, 80))
            self.imagewN = screen.blit(self.imagewN, (320,240))
            #display image for Rook
            self.imagewR = pygame.image.load('chessicons/wR.svg')
            self.imagewR = pygame.transform.scale(self.imagewR, (80, 80))
            self.imagewR = screen.blit(self.imagewR, (240,320))
            #display image for Bishop
            self.imagewB = pygame.image.load('chessicons/wB.svg')
            self.imagewB = pygame.transform.scale(self.imagewB, (80, 80))
            self.imagewB = screen.blit(self.imagewB, (320,320))

        elif self.color == 'Black':
            #display image for Queen
            self.imagebQ = pygame.image.load('chessicons/bQ.svg')
            self.imagebQ = pygame.transform.scale(self.imagebQ, (80, 80))
            self.imagebQ = screen.blit(self.imagebQ, (240,240))
            #display image for Knight
            self.imagebN = pygame.image.load('chessicons/bN.svg')
            self.imagebN = pygame.transform.scale(self.imagebN, (80, 80))
            self.imagebN = screen.blit(self.imagebN, (320,240))
            #display image for Rook
            self.imagebR = pygame.image.load('chessicons/bR.svg')
            self.imagebR = pygame.transform.scale(self.imagebR, (80, 80))
            self.imagebR = screen.blit(self.imagebR, (240,320))
            #display image for Bishop
            self.imagebB = pygame.image.load('chessicons/bB.svg')
            self.imagebB = pygame.transform.scale(self.imagebB, (80, 80))
            self.imagebB = screen.blit(self.imagebB, (320,320))


    #it will draw the transparent menu screen
    def drawMenu(self, screen):
        pygame.draw.rect(screen, (0, 0, 160, 160), 0)
        self.promotionImages()

    #it will handle clicks inside the square and associate it to the options
    def handle_click(self, screen):
        pass


    

#Piece Classes
class Piece:
    def __init__(self, type, color, position):
        self.type = type
        self.color = color
        self.position = position

    def get_valid_moves(self,board):
        return[]

#Pawn class
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__("pawn", color, position)
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
        diag_pos = (row + direction, col + 1) and (row + direction, col - 1)
        if board.get_piece_at(forward_pos) is None:
            moves.append(forward_pos)
            #2 double forward if on first move 
            if (self.color == "White") or (self.color == "Black"):
                double_forward_pos = (row + 2 * direction, col)
                if self.position == self.starting_position:
                    if board.get_piece_at(double_forward_pos) is None:
                        moves.append(double_forward_pos)
        elif board.get_piece_at(diag_pos) is not None and board.get_piece_at(diag_pos).color != self.color:
            moves.append(diag_pos)
        return moves

    #checks if the pawn should be promoted by checking position on the board
    def should_promote(self, position):
        if self.color == "White" and position[0] == 0:
            promotionMenu(self.color)
            return True
        elif self.color == "Black" and position[0] == 7:
            promotionMenu(self.color)
            return True
        return False
    



#Rook class
class Rook(Piece):
    def __init__(self, color, position):
        super().__init__("rook", color, position)
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wR.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bR.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        self.starting_position = position

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        direction_all = ((-1, 0), 
                         (0, -1), (0, 1),
                         (1, 0) )

        for offset in direction_all:
            offset_row, offset_col = offset
            current_row, current_col = row + offset_row, col + offset_col            
            while current_col >= 0 and current_row >= 0 and current_row < 8 and current_col < 8:
                if board.get_piece_at((current_row, current_col)) is None:
                    moves.append((current_row, current_col))
                else:
                    break
                current_row += offset_row
                current_col += offset_col
        return moves


#Bishop class
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__("bishop", color, position)
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wB.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bB.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        direction_all = ((-1, -1), (-1, 1),
                         (1, -1), (1, 1) )

        for offset in direction_all:
            offset_row, offset_col = offset
            current_row, current_col = row + offset_row, col + offset_col            
            while current_col >= 0 and current_row >= 0 and current_row < 8 and current_col < 8:
                if board.get_piece_at((current_row, current_col)) is None:
                    moves.append((current_row, current_col))
                else:
                    break
                current_row += offset_row
                current_col += offset_col
        return moves

#Knight class
class Knight(Piece):
    def __init__(self, color, position):
        super().__init__("knight", color, position)
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
        return moves

#Queen class
class Queen(Piece):
    def __init__(self, color, position):
        super().__init__("queen", color, position)
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wQ.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bQ.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position
        direction_all = ((-1, -1), (-1, 0), (-1, 1),
                         (0, -1), (0, 1),
                         (1, -1), (1, 0), (1, 1) )

        for offset in direction_all:
            offset_row, offset_col = offset
            current_row, current_col = row + offset_row, col + offset_col
            while current_col >= 0 and current_row >= 0 and current_row < 8 and current_col < 8:
                if board.get_piece_at((current_row, current_col)) is None:
                    moves.append((current_row, current_col))
                else:
                    break
                current_row += offset_row
                current_col += offset_col
        return moves


#King class
class King(Piece):
    def __init__(self, color, position):
        super().__init__("king", color, position)
        if self.color == "White":
            self.image = pygame.image.load('chessicons/wK.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            self.image = pygame.image.load('chessicons/bK.svg')
            self.image = pygame.transform.scale(self.image, (80, 80))
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
        for position in direction_all:
            if board.get_piece_at(position) is None:
                moves.append(position)
        return moves


#Game logic
class Game:
    def __init__(self):
        self.board = Board()
        self.promotion_menu = None
        self.turn_value = 1

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    col = mouse_pos[0] // self.board.cell_size
                    row = mouse_pos[1] // self.board.cell_size
                    position = (row, col)
                    
                    if self.board.handle_click(position, self.turn_value):
                        self.turn_value += 1
                        print(self.turn_value)
                    

            self.board.draw_board(screen)
            self.board.draw_pieces(screen)
            self.board.draw_valid_moves(screen)
            pygame.display.flip()
            clock.tick(60)

# Run the game
if __name__ == "__main__":
    game = Game() 
    game.run(
        
    )
    pygame.quit()
