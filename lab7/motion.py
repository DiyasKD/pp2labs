import pygame
pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

ball_color = (255, 0, 0)
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2

background_color = (255, 255, 255)

move_distance = 20

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_UP:
                if ball_y - move_distance >= ball_radius:
                    ball_y -= move_distance
            elif event.key == pygame.K_DOWN:
                if ball_y + move_distance <= screen_height - ball_radius:
                    ball_y += move_distance
            elif event.key == pygame.K_LEFT:
                if ball_x - move_distance >= ball_radius:
                    ball_x -= move_distance
            elif event.key == pygame.K_RIGHT:
                if ball_x + move_distance <= screen_width - ball_radius:
                    ball_x += move_distance

    screen.fill(background_color)
    
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

pygame.quit()
