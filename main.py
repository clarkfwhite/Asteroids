import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick()/1000
        #print(f"{dt}")
    
    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print("Screen width: 1280")
    #print("Screen height: 720")


if __name__ == "__main__":
    main()
