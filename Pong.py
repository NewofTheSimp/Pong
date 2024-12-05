import pygame
import SliderFriend
import SliderEnemy
import PongBall
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
SliderFriend = SliderFriend.Slider(screen)
SliderEnemy = SliderEnemy.Slider(screen)
PongBall = PongBall.Ball(screen)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#FFF4EA")
    Vector1 = SliderFriend.Move(dt)
    Vector2 = SliderEnemy.Move(dt)
    PongBall.Move(Vector1 ,Vector2)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()