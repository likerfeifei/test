import pygame
import random

pygame.init()

W, H, SIZE = 600, 400, 20
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

snake = [(100, 100)]
dx, dy = SIZE, 0
food = (random.randrange(0, W, SIZE), random.randrange(0, H, SIZE))
high_score = 0

font_large = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 28)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dy == 0: dx, dy = 0, -SIZE
            elif e.key == pygame.K_DOWN and dy == 0: dx, dy = 0, SIZE
            elif e.key == pygame.K_LEFT and dx == 0: dx, dy = -SIZE, 0
            elif e.key == pygame.K_RIGHT and dx == 0: dx, dy = SIZE, 0

    head = ((snake[0][0] + dx) % W, (snake[0][1] + dy) % H)
    if head in snake:
        score = 0
        snake = [(100, 100)]
        dx, dy = SIZE, 0
        continue
    
    snake.insert(0, head)
    if head == food:
        score += 10
        high_score = max(high_score, score)
        while food in snake:
            food = (random.randrange(0, W, SIZE), random.randrange(0, H, SIZE))
    else:
        snake.pop()

    screen.fill((20, 20, 30))
    
    pygame.draw.rect(screen, (40, 40, 60), (10, 10, 180, 70), border_radius=10)
    pygame.draw.rect(screen, (80, 200, 120), (10, 10, 180, 70), 2, border_radius=10)
    
    score_text = font_large.render(str(score), True, (80, 200, 120))
    label = font_small.render("SCORE", True, (150, 150, 170))
    screen.blit(label, (20, 15))
    screen.blit(score_text, (20, 38))
    
    high_text = font_small.render(f"BEST: {high_score}", True, (255, 200, 100))
    screen.blit(high_text, (100, 50))

    for i, (x, y) in enumerate(snake):
        color = (80, 200, 120) if i == 0 else (60, 160, 100)
        pygame.draw.rect(screen, color, (x+1, y+1, SIZE-2, SIZE-2), border_radius=4)
    
    pygame.draw.rect(screen, (220, 80, 80), (food[0]+2, food[1]+2, SIZE-4, SIZE-4), border_radius=6)
    pygame.draw.rect(screen, (255, 120, 120), (food[0]+4, food[1]+4, SIZE-8, SIZE-8), border_radius=4)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
