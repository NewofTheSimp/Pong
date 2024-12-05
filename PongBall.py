import pygame
import pygame.math
import random
class Ball:
    SCREEN_WIDTH = 1280 
    SCREEN_HEIGHT = 720
    # Ball properties
    ball_radius = 10
    ball_x = SCREEN_WIDTH // 2
    ball_y = SCREEN_HEIGHT // 2
    ball_dx = 4  # Ball velocity in X direction
    ball_dy = 4  # Ball velocity in Y direction
 
    def __init__ (self, screen):
        self.screen = screen


    def Move(self, Vector1, Vector2):   
        self.Vector1 = Vector1
        self.Vector2 = Vector2
        (LeftBottom, LeftTop) = self.Vector1
        (RightBottom, RightTop) = self.Vector2 
        # Move the ball
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        if self.ball_x  <= 0 or self.ball_x >= self.SCREEN_WIDTH:
            # Reset the ball to the center
            self.ball_x = self.SCREEN_WIDTH // 2
            self.ball_y = self.SCREEN_HEIGHT // 2
            self.ball_dx = -self.ball_dx  # Reverse direction
            print("# Ball collision with left or right walls (scoring)")

        elif self.ball_y <= 0 or self.ball_y  >= self.SCREEN_HEIGHT:
            self.ball_dy = -self.ball_dy  # Reverse Y direction
            print(" # Ball collision with top and bottom walls")
  
        elif (LeftBottom.x - 10 <= self.ball_x  <= LeftBottom.x + 10 and LeftTop.y <= self.ball_y <= LeftBottom.y):
            self.ball_dx = -self.ball_dx
            print(LeftBottom.x)
            print("# Ball collision with paddles")

        elif (RightBottom.x -10 <= self.ball_x  <= RightBottom.x + 10 and RightTop.y <= self.ball_y <= RightBottom.y):
            self.ball_dx = -self.ball_dx  # Reverse X direction
            print("# Ball collision with paddles")

 

        pygame.draw.circle(self.screen, "#C96868", (self.ball_x, self.ball_y), self.ball_radius)
        