import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        screen.blit(mole_image, mole_image.get_rect(topleft=(16, 16)))

        mole_x = 0
        mole_y = 0
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x //= 32
                    y //= 32
                    if x == mole_x and y == mole_y:
                        new_x = random.randrange(0, 20)
                        new_y = random.randrange(0, 16)
                        mole_x = new_x
                        mole_y = new_y

                        new_x *= 32
                        new_y *= 32
                        screen.fill("light green")
                        screen.blit(mole_image, mole_image.get_rect(topleft=(new_x, new_y)))
                        pygame.display.flip()




            for i in range(16):
                pygame.draw.line(screen, "dark green", (0, 32 + 32 * i), (640, 32 + 32 * i))


            for j in range(20):
                pygame.draw.line(screen, "dark green", (32 + 32 * j, 0), (32 + 32 * j, 512))



            pygame.display.flip()

            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()


