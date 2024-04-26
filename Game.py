import pygame
import sys
import math
import fighting
def Start_Game(Time):
    pygame.init()

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    window = pygame.display.set_mode(WINDOW_SIZE)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)
    ORANGE = (255, 165, 0)

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Kill And Win")

    background_image = pygame.image.load("floor_black.jpg")
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    frame_width = 600
    frame_height = 400

    frame_x = (WINDOW_WIDTH - frame_width) // 2
    frame_y = (WINDOW_HEIGHT - frame_height) // 2

    frame_rect = pygame.Rect(frame_x, frame_y, frame_width, frame_height)
    font = pygame.font.Font(None, 36)
    room_width = 100
    room_height = 100
    room_colors = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]

    room_positions = [
        (frame_x + 50, frame_y + 50),
        (frame_x + 200, frame_y + 50),
        (frame_x + 350, frame_y + 50),
        (frame_x + 50, frame_y + 200),
        (frame_x + 200, frame_y + 200),
        (frame_x + 350, frame_y + 200)
    ]

    time_limit = 10
    current_time = 0

    player_speed = 1  # Adjust the player's speed as needed
    player_rect = pygame.Rect(frame_rect.centerx - 10, 0, 20, 20)  # Start at the top center

    clock = pygame.time.Clock()

    def distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time += clock.get_rawtime() / 1000
        clock.tick()

        screen.blit(background_image, (0, 0))

        

        for i, (x, y) in enumerate(room_positions):
            room_rect = pygame.Rect(x, y, room_width, room_height)
            if room_rect.collidepoint(player_rect.center):
                fighting.Start_Game()
            pygame.draw.rect(screen, room_colors[i], room_rect)

        pygame.draw.rect(screen, ORANGE, player_rect)

        closest_room = min(room_positions, key=lambda pos: distance(pos, player_rect.center))

        dx = closest_room[0] + room_width // 2 - player_rect.centerx
        dy = closest_room[1] + room_height // 2 - player_rect.centery
        distance_to_room = math.sqrt(dx ** 2 + dy ** 2)
        if distance_to_room > player_speed:
            ratio = player_speed / distance_to_room
            dx *= ratio
            dy *= ratio
        player_rect.centerx += dx
        player_rect.centery += dy

        for i, (x, y) in enumerate(room_positions):
            room_rect = pygame.Rect(x, y, room_width, room_height)
            if room_rect.collidepoint(player_rect.center):
                print("Player is inside room", i + 1)

        timer_font = pygame.font.Font(None, 36)
        timer_text = timer_font.render(f"Time: {int(time_limit - current_time)}", True, WHITE)
        screen.blit(timer_text, (20, 20))

        if current_time >= time_limit:
            game_over_font = pygame.font.Font(None, 72)
            game_over_text = game_over_font.render("Game Over!", True, RED)
            screen.blit(game_over_text, ((WINDOW_WIDTH - game_over_text.get_width()) // 2, (WINDOW_HEIGHT - game_over_text.get_height()) // 2))
            Restart = font.render("Restart", True, BLACK)
            Restart_rect = Restart.get_rect(center=(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 75))
            window.blit(Restart, Restart_rect)

        pygame.display.flip()
