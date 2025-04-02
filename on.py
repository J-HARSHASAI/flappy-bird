import pygame  # provides functionalities for graphics, sound, and user input.
from pygame.locals import *  # noqa # user inputs like clicks handle user input.
import sys    # Used to exit the program gracefully using sys
import random
import os  # Allows for file operations, like checking if a high score file exists.

class FlappyBird:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Initialize the pygame mixer for sound

        self.screen = pygame.display.set_mode((600, 650))
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("D:\\harsha\\bg final.png").convert()
        self.birdSprites = [pygame.image.load("D:\\harsha\\1.png").convert_alpha(),
                            pygame.image.load("D:\\harsha\\2.png").convert_alpha(),
                            pygame.image.load("D:\\harsha\\dead.png")]
        self.wallUp = pygame.image.load("D:\\harsha\\bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("D:\\harsha\\top.png").convert_alpha()
        self.gap = 160
        self.wallx = 400
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110) 
        self.menu_active = True
        self.high_score = self.load_high_score()  # Stores the high score loaded from a file.

        # Load sound effects
        self.flap_sound = pygame.mixer.Sound("D:\harsha\WhatsApp Audio 2024-11-20 at 5.06.34 PM (1).mpeg")
        self.death_sound = pygame.mixer.Sound("D:\\harsha\\WhatsApp Audio 2024-11-20 at 5.06.34 PM.mpeg")
        self.score_sound = pygame.mixer.Sound("D:\harsha\WhatsApp Audio 2024-11-20 at 5.10.36 PM.mpeg")
        

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as f:
                return int(f.read())
        return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))

    def reset_game(self):
        self.dead = False
        self.counter = 0
        self.wallx = 400
        self.offset = random.randint(-110, 110)
        self.gravity = 5
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)
            self.score_sound.play()  # Play score sound when passing a wall

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
        if upRect.colliderect(self.bird) or downRect.colliderect(self.bird) or not 0 < self.bird[1] < 720:
            self.dead = True
            self.death_sound.play()  # Play death sound when bird collides

    def display_menu(self, font):
        title_surface = font.render("Flappy Bird", True, (255, 0, 0))
        start_surface = font.render("Press S to Start", True, (0, 0, 0))
        exit_surface = font.render("Press E to Exit", True, (0, 0, 0))
        self.screen.blit(title_surface, (100, 200))
        self.screen.blit(start_surface, (100, 300))
        self.screen.blit(exit_surface, (100, 400))

    def display_game_over(self, font):
        game_over_surface = font.render("Game Over!", True, (255, 0, 0))
        restart_surface = font.render("Press R to Restart", True, (0, 0, 0))
        exit_surface = font.render("Press E to Exit", True, (0, 0, 0))
        high_score_surface = font.render(f"High Score: {self.high_score}", True, (0, 0, 0))
        current_score_surface = font.render(f"CurrentScore: {self.counter}", True, (0, 0, 0))

        self.screen.blit(game_over_surface, (100, 200))
        self.screen.blit(restart_surface, (100, 300))
        self.screen.blit(exit_surface, (100, 380))
        self.screen.blit(high_score_surface, (100, 460))
        self.screen.blit(current_score_surface, (100, 530))

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if self.menu_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:  # Start game
                            self.reset_game()
                            self.menu_active = False
                        elif event.key == pygame.K_e:  # Exit game
                            sys.exit()
                else:  # In-game state
                    if not self.dead:
                        if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
                            if event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                                self.jump = 17
                                self.gravity = 5
                                self.jumpSpeed = 10
                                self.flap_sound.play()  # Play flap sound when bird jumps
                    elif event.type == pygame.KEYDOWN:  # Handle game over options
                        if event.key == pygame.K_r:  # Restart the game
                            if self.counter > self.high_score:
                                self.high_score = self.counter
                                self.save_high_score()
                            self.reset_game()
                            self.menu_active = False
                        elif event.key == pygame.K_e:  # Exit game
                            sys.exit()

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))

            if self.menu_active:
                self.display_menu(font)  # Display the menu
            else:
                if self.dead:
                    self.display_game_over(font)  # Display game over
                else:
                    # Game logic and rendering
                    self.screen.blit(self.wallUp,
                                     (self.wallx, 360 + self.gap - self.offset))
                    self.screen.blit(self.wallDown,
                                     (self.wallx, 0 - self.gap - self.offset))
                    self.screen.blit(font.render(str(self.counter),
                                                 -1,
                                                 (255, 255, 255)),
                                     (200, 50))
                    self.sprite = 2 if self.dead else 0
                    self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
                    self.updateWalls()
                    self.birdUpdate()

            pygame.display.update()


if __name__ == "__main__":
    FlappyBird().run()
