import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox

# Define some colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class GameObject:
    def __init__(self, color, size, x, y, speed):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.sword_length = 50  # Length of the sword
        self.speed = speed  # Speed of movement
        self.direction = random.choice(["up", "down", "left", "right"])
        self.health = 100  # Initial health

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        # Draw the sword
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.sword_length, self.y), 5)

    def move(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed

        # Add some randomness to direction change
        if random.random() < 0.02:
            self.direction = random.choice(["up", "down", "left", "right"])

    def hit(self, other):
        # Check if this object hits the other
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        if distance <= self.sword_length + other.size:
            return True
        return False

def Start_Game():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sword Fight")

    # Create the red object controlled by the player
    red_object = GameObject(RED, 50, 100, 300, 0.1)

    # Create two yellow objects controlled by AI
    yellow_objects = []
    for _ in range(2):
        yellow_object = GameObject(YELLOW, 30, random.randint(500, 700), random.randint(100, 500), 0.1)
        yellow_objects.append(yellow_object)

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Display a dialog box asking the user if they want to exit the game
                root = tk.Tk()
                root.withdraw()
                response = messagebox.askyesno("Exit", "Do you want to exit the game?")
                if response:
                    running = False

        if not running:
            break

        # Clear the screen
        screen.fill((255, 255, 255))

        # Handle player input for the red object
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            # Move the red object up
            red_object.direction = "up"
        elif keys[pygame.K_DOWN]:
            # Move the red object down
            red_object.direction = "down"
        elif keys[pygame.K_LEFT]:
            # Move the red object left
            red_object.direction = "left"
        elif keys[pygame.K_RIGHT]:
            # Move the red object right
            red_object.direction = "right"

        # Move the red object
        red_object.move()

        # Move yellow objects
        for yellow_object in yellow_objects:
            yellow_object.move()

            # Check if yellow objects hit the red object
            if yellow_object.hit(red_object):
                red_object.health -= 10
                if red_object.health <= 0:
                    print("Red object is dead!")
                    # Implement your reaction when the red object dies here

        # Check for collisions between the red object and yellow objects
        for yellow_object in yellow_objects:
            if red_object.hit(yellow_object):
                yellow_object.health -= 10
                if yellow_object.health <= 0:
                    yellow_objects.remove(yellow_object)
                    print("Yellow object is dead!")
                    # Implement your reaction when a yellow object dies here

        # Draw the objects
        red_object.draw(screen)
        for yellow_object in yellow_objects:
            yellow_object.draw(screen)

        # Update the display
        pygame.display.flip()

    pygame.quit()

