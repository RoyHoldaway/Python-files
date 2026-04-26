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
        for cols in range(8):
            self.pieces.append(Pawn("Black", (1, cols)))

    #click mouse
    def handle_click(self, position, turn_value):
        if self.selected_piece is None:
            self.select_piece(position, turn_value)
        else:
            self.try_move(position)
            
    def select_piece(self, position, turn_value):
        piece = self.get_piece_at(position)
        if piece and self.is_correct_turn(piece, turn_value):
            self.selected_piece = piece
            print('selected: ', piece.type, piece.position)

    def try_move(self, position):
        if position in self.selected_piece.get_valid_moves(self):
            self.move_piece(self.selected_piece, position)
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
        
    def move_piece(self, piece, position):
        piece.position = position

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

        direction = -1 if self.color == "White" else 1

        #1 forward movement 1 space
        forward_pos = (row + direction, col)
        if board.get_piece_at(forward_pos) is None:
            moves.append(forward_pos)
            #2 double forward if on first move 
            if (self.color == "White") or (self.color == "Black"):
                double_forward_pos = (row + 2 * direction, col)
                if board.get_piece_at(double_forward_pos) is None:
                    moves.append(double_forward_pos)

                    if self.position == self.starting_position:
                        if board.get_piece_at(double_forward_pos) is None:
                            moves.append(double_forward_pos)

        return moves



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


    def get_valid_moves(self, board):
            moves = []
            row, col = self.position

            direction = -1 if self.color == "White" else 1

            forward_pos = (row + direction, col)
            if board.get_piece_at(forward_pos) is None:
                moves.append(forward_pos)
    
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

        self.starting_position = position

    def get_valid_moves(self, board):
        moves = []
        row, col = self.position

        direction = -1 if self.color == "White" else 1

        direction_all = ([row-1, col-1], [row-1, col], [row-1, col + 1],
                         [row, col-1], [row, col + 1],
                         [row+1, col-1], [row+1, col], [row+1, col + 1] )
        for pos in direction_all:
            if board.get_piece_at(pos) is None:
                moves.append(pos)

        return moves


#Game logic
class Game:
    def __init__(self):
        self.board = Board()
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
                    self.board.handle_click(position, self.turn_value)
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