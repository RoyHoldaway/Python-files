#imports
import pygame

#establishing the game window and parameters
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess.py")
turn_value = 1
clock = pygame.time.Clock()

#chessboard
rows = 8
cols = 8
cell_size = width // cols
#This equation will take the width of the screen and divide it by the
#number of columns to get the size of each cell in the chessboard.

selected_piece = None
selected_index = None
selected_position = None
selected_color = None
path_clear = False
#definition of state for variables im creating for movement and path detection

#specify white pieces and their coordinates
white_pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]

white_locations = [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
                (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)]


#specify black pieces and their coordinates
black_pieces = ["Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn",
            "Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]

black_locations = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]

#This is where we will keep track of the pieces that have been captured during the game.
captured_w_pieces = []
captured_b_pieces = []

#loading in game piece images
#Black King image and sizing
Black_King = pygame.image.load('chessicons/bK.svg')
Black_King = pygame.transform.scale(Black_King, (80, 80))

#Black queen image and sizing
Black_Queen = pygame.image.load('chessicons/bQ.svg')
Black_Queen = pygame.transform.scale(Black_Queen, (80, 80))

#Black bishop image and sizing
Black_Bishop = pygame.image.load('chessicons/bB.svg')
Black_Bishop = pygame.transform.scale(Black_Bishop, (80, 80))

#Black knight image and sizing
Black_Knight = pygame.image.load('chessicons/bN.svg')
Black_Knight = pygame.transform.scale(Black_Knight, (80, 80))

#Black Rook image and sizing
Black_Rook = pygame.image.load('chessicons/bR.svg')
Black_Rook = pygame.transform.scale(Black_Rook, (80, 80))

#Black Pawn image and sizing
Black_Pawn = pygame.image.load('chessicons/bP.svg')
Black_Pawn = pygame.transform.scale(Black_Pawn, (80, 80))

#white king image and sizing
White_King = pygame.image.load('chessicons/wK.svg')
White_King = pygame.transform.scale(White_King, (80, 80))

#white queen image and sizing
White_Queen = pygame.image.load('chessicons/wQ.svg')
White_Queen = pygame.transform.scale(White_Queen, (80, 80))

#white bishop image and sizing
White_Bishop = pygame.image.load('chessicons/wB.svg')
White_Bishop = pygame.transform.scale(White_Bishop, (80, 80))

#white knight image and sizing
White_Knight = pygame.image.load('chessicons/wN.svg')
White_Knight = pygame.transform.scale(White_Knight, (80, 80))

#white rook image and sizing
White_Rook = pygame.image.load('chessicons/wR.svg')
White_Rook = pygame.transform.scale(White_Rook, (80, 80))

#white pawn image and sizing
White_Pawn = pygame.image.load('chessicons/wP.svg')
White_Pawn = pygame.transform.scale(White_Pawn, (80, 80))

#This function will handle the movement of the pieces on the board. 
#It will take in the current position of the piece, the desired position, and the type of piece being moved.
#It will then check if the move is valid for that piece and if it is, it will update the board accordingly.
def movement():
    pass


def is_path_clear(coordinates):
    selected_location = white_locations.index(coordinates)
    selected_piece = white_pieces[selected_location]


#This is where the game loop will go, which will keep the window open until the user decides to close it.
running = True
while running:    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            turn_value += 1
            mouse_pos = pygame.mouse.get_pos()
            col = mouse_pos[0] // cell_size
            row = mouse_pos[1] // cell_size
            coordinates = (row,col)
            if turn_value % 2 == 0 and coordinates in white_locations:
                selected_index = white_locations.index(coordinates)
                selected_piece = white_pieces[selected_index]
                selected_position = white_locations[selected_index]
                if selected_piece == "Pawn":                
                    print('this works')

                elif selected_piece == "Rook":
                    pass
                elif selected_piece == "Knight":
                    pass
                elif selected_piece == "Bishop":
                    pass
                elif selected_piece == "Queen":
                    pass
                elif selected_piece == "King":
                    pass



            elif turn_value % 2 == 1 and coordinates in black_locations:
                selected_location = black_locations.index(coordinates)
                selected_piece = black_pieces[selected_location]
                print(f"Selected piece: {selected_piece} at location: {coordinates} turn value: {turn_value}")




        if event.type == pygame.QUIT:
            running = False;

    # Draw the chessboard
    for row in range(rows):  # 0 to 7
        for col in range(cols):  # 0 to 7
            if (row + col) % 2 == 0:
                color = (255, 255, 255)  # white square
            else:
                color = (0, 0, 0)  # black square
            # Draw the rectangle for this square
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    #All pieces should populate the board in their respective locations once the game starts with respective images.
    for i in range(len(white_pieces)):
        piece = white_pieces[i]
        location = white_locations[i]
        if piece == "Rook":
            screen.blit(White_Rook, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Knight":
            screen.blit(White_Knight, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Bishop":
            screen.blit(White_Bishop, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Queen":
            screen.blit(White_Queen, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "King":
            screen.blit(White_King, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Pawn":
            screen.blit(White_Pawn, (location[1] * cell_size, location[0] * cell_size))

    for i in range(len(black_pieces)):
        piece = black_pieces[i]
        location = black_locations[i]
        if piece == "Rook":
            screen.blit(Black_Rook, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Knight":
            screen.blit(Black_Knight, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Bishop":
            screen.blit(Black_Bishop, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Queen":
            screen.blit(Black_Queen, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "King":
            screen.blit(Black_King, (location[1] * cell_size, location[0] * cell_size))
        elif piece == "Pawn":
            screen.blit(Black_Pawn, (location[1] * cell_size, location[0] * cell_size))

    # Update the display to show the drawings
    pygame.display.flip()

    movement()
    
pygame.quit()