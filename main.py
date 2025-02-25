import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACK
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def draw_mode_selection(win):
    WIN = pygame.display.set_mode(size)
    pygame.font.init()
    win.fill((0,0,0))
    im = pygame.transform.scale(pygame.image.load("Backgrounds/bg.png"),pygame.display.get_surface().get_size())
    win.blit(im,(0,0))
    background = pygame.transform.scale(pygame.image.load("Backgrounds/Menu.png"), pygame.display.get_surface().get_size())
    button1 = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b1.png"), pygame.display.get_surface().get_size())
    button2 = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b2.png"), pygame.display.get_surface().get_size())
    button3 = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b3.png"), pygame.display.get_surface().get_size())

    current_background = background
    win.blit(current_background, (0, 0))
    pygame.display.update()

    while True:
        p0, p1 = pygame.mouse.get_pos()
        b0, b1, b2 = pygame.mouse.get_pressed()
        k1, k2 = pygame.display.get_surface().get_size()
        d1 = float(p0) / k1
        d2 = float(p1) / k2
        
        # Kiểm tra vị trí con trỏ và xử lý animation
        if 0.37 < d1 < 0.561 and 0.33 < d2 < 0.467:
            if current_background != button1:
                current_background = button1
                win.blit(current_background, (0, 0))
                pygame.display.update()
        elif 0.37 < d1 < 0.561 and 0.51 < d2 < 0.647:
            if current_background != button2:
                current_background = button2
                win.blit(current_background, (0, 0))
                pygame.display.update()
        elif 0.37 < d1 < 0.561 and 0.703 < d2 < 0.837:
            if current_background != button3:
                current_background = button3
                win.blit(current_background, (0, 0))
                pygame.display.update()
        else:
            # Quay trở lại bg gốc nếu con trỏ không chỉ vào btn nào
            if current_background != background:
                current_background = background
                win.blit(current_background, (0, 0))
                pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_background == button1:
                    return "pvp"
                elif current_background == button2:
                    return "pvc"
                elif current_background == button3:
                    pygame.quit()
                    # return "quit" 

def draw_pause_menu(win):
    WIN = pygame.display.set_mode(size)
    pygame.font.init()
    win.fill((0,0,0))
    im = pygame.transform.scale(pygame.image.load("Backgrounds/bg.png"),pygame.display.get_surface().get_size())
    win.blit(im,(0,0))
    # Load các hình ảnh nền và hình ảnh cho từng tùy chọn
    background = pygame.transform.scale(pygame.image.load("Backgrounds/PAUSE.png"), pygame.display.get_surface().get_size())
    resume_button = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b1.png"), pygame.display.get_surface().get_size())
    menu_button = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b2.png"), pygame.display.get_surface().get_size())
    replay_button = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b3.png"), pygame.display.get_surface().get_size())

    current_background = background

    # Vẽ lần đầu để màn hình không trống
    win.blit(current_background, (0, 0))
    pygame.display.update()

    while True:
        p0, p1 = pygame.mouse.get_pos()
        k1, k2 = pygame.display.get_surface().get_size()
        d1 = float(p0) / k1
        d2 = float(p1) / k2
        
        # Kiểm tra vị trí chuột và thay đổi hình nền nếu cần thiết
        if 0.37 < d1 < 0.561 and 0.33 < d2 < 0.467:
            if current_background != resume_button:
                current_background = resume_button
                win.blit(current_background, (0, 0))
                pygame.display.update()
        elif 0.37 < d1 < 0.561 and 0.51 < d2 < 0.647:
            if current_background != menu_button:
                current_background = menu_button
                win.blit(current_background, (0, 0))
                pygame.display.update()
        elif 0.37 < d1 < 0.561 and 0.703 < d2 < 0.837:
            if current_background != replay_button:
                current_background = replay_button
                win.blit(current_background, (0, 0))
                pygame.display.update()
        else:
            if current_background != background:
                current_background = background
                win.blit(current_background, (0, 0))
                pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_background == resume_button:
                    return "resume"
                elif current_background == replay_button:
                    return "back_to_menu"
                elif current_background == menu_button:
                    return "replay"
                
def draw_winner(win, winner):
    pygame.font.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    if winner == RED:
        congrats_image_path = r"Backgrounds\RED.png"
    elif winner == WHITE:
        congrats_image_path = r"Backgrounds\WHITE.png"
    elif winner == "DRAW":
        congrats_image_path = r"Backgrounds\hoa.png"

    congrats_image = pygame.image.load(congrats_image_path)
    congrats_image = pygame.transform.scale(congrats_image, (WIDTH, HEIGHT))
    win.blit(congrats_image, (0, 0))

    pygame.display.update()
    pygame.time.delay(2000)  # Hiển thị trong 2 giây
    

def draw_ai_color_selection(win):
    WIN = pygame.display.set_mode(size)
    pygame.font.init()
    win.fill((0,0,0))
    im = pygame.transform.scale(pygame.image.load("Backgrounds/bg.png"),pygame.display.get_surface().get_size())
    win.blit(im,(0,0))
    background = pygame.transform.scale(pygame.image.load("Backgrounds/AI_MOVE.png"), pygame.display.get_surface().get_size())
    red_choice = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b1.png"), pygame.display.get_surface().get_size())
    white_choice = pygame.transform.scale(pygame.image.load("Backgrounds/Menu-b2.png"), pygame.display.get_surface().get_size())

    current_background = background
    
    win.blit(current_background, (0, 0))
    pygame.display.update()
    
    while True:
        p0, p1 = pygame.mouse.get_pos()
        k1, k2 = pygame.display.get_surface().get_size()
        d1 = float(p0) / k1
        d2 = float(p1) / k2
        
        if 0.37 < d1 < 0.561 and 0.33 < d2 < 0.467:
            if current_background != red_choice:
                current_background = red_choice
                win.blit(current_background, (0, 0))
                pygame.display.update()
        elif 0.37 < d1 < 0.561 and 0.51 < d2 < 0.647:
            if current_background != white_choice:
                current_background = white_choice
                win.blit(current_background, (0, 0))
                pygame.display.update()
        else:
            if current_background != background:
                current_background = background
                win.blit(current_background, (0, 0))
                pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_background == red_choice:
                    return RED
                elif current_background == white_choice:
                    return WHITE

def main(win):
    mode = draw_mode_selection(win)
    if mode is None:
        return False

    ai_color = None
    player_color = None
    if mode == "pvc":
        ai_color = draw_ai_color_selection(win)
        if ai_color is None:
            return False  
        player_color = WHITE if ai_color == RED else RED
    elif mode == "pvp":
        ai_color = None 
        player_color = RED
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(win, ai_color, player_color)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        if mode == "pvc" and game.turn == ai_color:
            value, new_board = minimax(game.get_board(), 4, ai_color == WHITE, game)
            if new_board:
                game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.board.back_button_rect and game.board.back_button_rect.collidepoint(pos):
                    if mode == "pvc":
                        game.undo(1)  # Chỉ cần gọi với '1' nhưng phương thức 'undo' đã được điều chỉnh để nhân đôi số lượng này
                    else:
                        game.undo()  # Gọi với giá trị mặc định, sẽ lùi một nước
                elif game.board.settings_button_rect and game.board.settings_button_rect.collidepoint(pos):
                    pause_response = draw_pause_menu(win)
                    if pause_response == "resume":
                        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                        continue
                    elif pause_response == "back_to_menu":
                        return True
                    elif pause_response == "replay":
                        game.reset()
                        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                        continue
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pause_response = draw_pause_menu(win)
                    if pause_response == "resume":
                        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                        continue
                    elif pause_response == "back_to_menu":
                        return True
                    elif pause_response == "replay":
                        game.reset()
                        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                        continue
                
                
        game.update()
        
        winner = game.winner()
        if winner:
            draw_winner(win, winner)
            pygame.time.delay(2000)  
            return draw_mode_selection(win)

    return True

pygame.init()
size = (1200, 800)
WIN = pygame.display.set_mode(size)

pygame.display.set_caption('Checkers Game')

keep_running = True
while keep_running:
    keep_running = main(WIN)

pygame.quit()