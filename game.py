import pygame

print("CLARK rules OK")

pygame.init()
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # rita en rektangel på skärmen
    pygame.draw.rect(display, (128, 128, 255), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()
    clock.tick(60)