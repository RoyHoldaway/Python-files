import pygame
from board import Board
from promotion import promotionMenu
from constraints import Constraints
from ai import AI


#Game logic
class Game:
    def __init__(self):
        self.board = Board()
        self.turn_value = 1
        self.promotion_menu = None
        self.constraints = Constraints()
        self.screen = self.constraints.screen
        self.clock = self.constraints.clock
        self.ai = AI()

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
                    #when the mouse is clicked if the pawn promotion menu is not none, so when it is true it will produce the promotion menu
                    if self.promotion_menu is not None:
                        #Then it will process the click inside the menu
                        if self.promotion_menu.handle_click(self.board, position):
                            self.promotion_menu = None
                            self.turn_value += 1

                    else:
                        if self.board.handle_click(position, self.turn_value):
                            if hasattr(self.board, 'pending_promotion') and self.board.pending_promotion:
                                pawn = self.board.pending_promotion
                                self.promotion_menu = promotionMenu(pawn.color, pawn.position)
                                self.board.pending_promotion = None
                            else:
                                print("turn value is:", self.turn_value)
                                best_move = self.ai.get_best_move(self.board, 1)
                                if best_move is not None:
                                    piece, move_position = best_move
                                    new_piece_at_clicked_position = self.board.get_piece_at(move_position)
                                    self.board.move_piece(piece, move_position, new_piece_at_clicked_position)
                                    self.turn_value += 1                                
                                self.turn_value += 1
                                print("turn value is:", self.turn_value)



            self.board.draw_board(self.screen)
            self.board.draw_pieces(self.screen)
            self.board.draw_valid_moves(self.screen)
            #draw promotion menu on top of the board if it is active
            if self.promotion_menu is not None:
                self.promotion_menu.promotionImages(self.screen, self.promotion_menu.color)


            pygame.display.flip()
            self.clock.tick(60)