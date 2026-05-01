import pygame
from pieces import Rook, Knight, Bishop, Queen


#this will be called when pawns get to row 0 or 7
class promotionMenu:
    def __init__(self, color, position):
        self.position = position
        self.color = color


    def promotionImages(self, screen, piece_color):
        if piece_color == 'White':
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

        elif piece_color == 'Black':
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


    #it will handle clicks inside the square and associate it to the options
    def handle_click(self, board, position):
        print(position)
        piece_map = {
            (3,3): Queen,
            (3,4): Knight,
            (4,3): Rook,
            (4,4): Bishop,
        }
        if position in piece_map:
            pawn = board.get_piece_at(self.position)
            if pawn:
                board.pieces.remove(pawn)
                new_piece = piece_map[position](self.color, self.position)
                board.pieces.append(new_piece)
            return True
        return False

