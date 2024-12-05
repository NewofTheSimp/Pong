import pygame
import pygame.math
class Slider:
    sliderTop = pygame.Vector2(1230, 100)
    sliderBottom = pygame.Vector2(1230, 50)
    def __init__(self, screen):
       self.screen = screen

    def Move(self, dt):
        move_up = False
        move_down = False
        keys = pygame.key.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            move_up = True
        if keys[pygame.K_DOWN]:
            move_down = True

        if move_up and self.sliderTop.y > 0:
            self.sliderBottom.y -= 300 * dt
            self.sliderTop.y = self.sliderBottom.y - 50
        if move_down and self.sliderBottom.y < self.screen.get_height():
            self.sliderTop.y += 300 * dt
            self.sliderBottom.y = self.sliderTop.y + 50

        pygame.draw.line(self.screen, "#FADFA1", self.sliderBottom, self.sliderTop)
        return (self.sliderBottom, self.sliderTop)