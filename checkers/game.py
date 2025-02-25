import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board
from copy import deepcopy

class Game:
    def __init__(self, win, ai_color, player_color):
        self._init()
        self.ai_color = ai_color
        self.player_color = player_color
        self.turn = RED
        self.win = win
        self.last_moved = None
        self.history = [] 

    def save_state(self):
        # Lưu trạng thái hiện tại của bàn cờ và lượt chơi vào lịch sử
        state = {'board': deepcopy(self.board), 'turn': self.turn}
        self.history.append(state)

    def undo(self, steps=1):
        for _ in range(steps):
            if self.history:
                state = self.history.pop()  # Lấy và loại bỏ trạng thái cuối cùng khỏi lịch sử
                self.board = state['board']  # Phục hồi trạng thái bàn cờ
                self.turn = state['turn']  # Phục hồi lượt chơi
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.history = [] # Khởi tạo lại lịch sử khi bắt đầu mới
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        # Vẽ chấm màu vàng ở vị trí khởi hành của quân cờ sau khi nó di chuyển
        if self.last_moved:
            row, col = self.last_moved
            pygame.draw.circle(self.win, (255, 255, 0), 
                            (col * SQUARE_SIZE + SQUARE_SIZE // 2, 
                                row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col) 
        
        piece = self.board.get_piece(row, col)
        if piece and not isinstance(piece, int) and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.save_state()  # Lưu trạng thái trước khi di chuyển
            # Cập nhật vị trí khởi hành trước khi quân cờ di chuyển
            self.last_moved = (self.selected.row, self.selected.col)
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()