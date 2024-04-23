import pygame
import sys


pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Kill And Win")
background_image = pygame.image.load("one.jpeg")  
font = pygame.font.Font(None, 36)  


kill_text = font.render("Kill", True, WHITE)
win_text = font.render("Win", True, WHITE)
enter_text = font.render("Enter", True, BLACK)


kill_text_rect = kill_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
win_text_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
enter_text_rect = enter_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2.18 + 150))

enter_button_rect = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 100, 100, 50)

# Load sound
pygame.mixer.init()
button_sound = pygame.mixer.Sound("epic-logo-6906.mp3") 
pygame.mixer.Sound.play(button_sound, loops=-1)  

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if enter_button_rect.collidepoint(event.pos):
                   # Open new window
                    new_window = True
                    while new_window:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                new_window = False
                                running = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:  # Left mouse button
                                    # Check if Easy or Hard button is clicked
                                    if easy_button_rect.collidepoint(event.pos):
                                        print("Easy mode selected!")
                                    elif hard_button_rect.collidepoint(event.pos):
                                        print("Hard mode selected!")

                        # Clear the window
                        window.fill(WHITE)

                        # Draw text
                        lorem_text = font.render("Lorem Ipsum is simply dummy text...", True, BLACK)
                        lorem_text_rect = lorem_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
                        window.blit(lorem_text, lorem_text_rect)

                  
                        easy_button_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 50, 100, 50)
                        hard_button_rect = pygame.Rect(WINDOW_WIDTH // 2 + 10, WINDOW_HEIGHT // 2 + 50, 100, 50)
                        pygame.draw.rect(window, BLACK, easy_button_rect, 2)
                        pygame.draw.rect(window, BLACK, hard_button_rect, 2)

                        # Button text
                        easy_text = font.render("Easy", True, BLACK)
                        easy_text_rect = easy_text.get_rect(center=(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 75))
                        window.blit(easy_text, easy_text_rect)

                        hard_text = font.render("Hard", True, BLACK)
                        hard_text_rect = hard_text.get_rect(center=(WINDOW_WIDTH // 2 + 60, WINDOW_HEIGHT // 2 + 75))
                        window.blit(hard_text, hard_text_rect)

                        pygame.display.flip()

    window.blit(background_image, (0, 0))

    window.blit(kill_text, kill_text_rect)
    window.blit(win_text, win_text_rect)
    window.blit(enter_text, enter_text_rect)


    pygame.draw.rect(window, WHITE, enter_button_rect)
    pygame.draw.rect(window, BLACK, enter_button_rect, 2)
    window.blit(enter_text, enter_text_rect)

    pygame.display.flip()
pygame.quit()
sys.exit()
