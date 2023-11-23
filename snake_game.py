#Akshat Rajvanshi - 23/11/23
#Please Like Share & subscrinbe


import pygame
import sys
import random
from enum import Enum
import time


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class SnakeGame:
    def __init__(self) -> None:
        pygame.init()

        #Declaring colors
        self.BLACK = pygame.Color(0, 0, 0)
        self.RED = pygame.Color(255, 0, 0)
        self.GREEN = pygame.Color(0, 255, 0)
        self.BROWN = pygame.Color(139, 69, 19)
        self.YELLOW = pygame.Color(255, 255, 0)

        #Declaring game settings
        self.speed = 20
        self.frame_size_x = 800
        self.frame_size_y = 600
        self.square_size = 60

        #Initializing the game window
        pygame.display.set_caption("Snake Game")
        self.gwindow_size = pygame.display.set_mode((self.frame_size_x, self.frame_size_y))

        #Initializing the game variables
        self.position_head = [120, 60]
        self.snake_body = [[120, 60]]
        self.position_food = [
            random.randrange(1, (self.frame_size_x // self.square_size)) * self.square_size,
            random.randrange(1, (self.frame_size_y // self.square_size)) * self.square_size,
        ]
        self.food_spawn = True
        self.score = 0
        self.direction = Direction.RIGHT

        #Initializing the game clock
        self.fps_controller = pygame.time.Clock()


    def reset_game(self):
        self.direction = Direction.RIGHT
        self.position_head = [120, 60]
        self.snake_body = [[120, 60]]
        self.position_food = [
            random.randrange(1, (self.frame_size_x // self.square_size)) * self.square_size,
            random.randrange(1, (self.frame_size_y // self.square_size)) * self.square_size,
        ]
        self.food_spawn = True
        self.score = 0

    def score_display(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score " + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.frame_size_x / 10, 15)
        else:
            score_rect.midtop = (self.frame_size_x / 2, self.frame_size_y / 1.25)
        self.gwindow_size.blit(score_surface, score_rect)

    def has_collision(self):
        return any(block == self.position_head for block in self.snake_body[1:])
    
    def game_over(self):
        font = pygame.font.SysFont("consolas", 50)
        game_over_text = font.render("Game Over", True, self.RED)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.midtop = (self.frame_size_x / 2, self.frame_size_y / 4)
        self.gwindow_size.blit(game_over_text, game_over_rect)

        self.score_display(2, self.BLACK, "consolas", 30)
        pygame.display.flip()

        time.sleep(5)
        self.reset_game()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == ord("w")) and self.direction != Direction.DOWN:
                        self.direction = Direction.UP
                    elif (event.key == pygame.K_DOWN or event.key == ord("s")) and self.direction != Direction.UP:
                        self.direction = Direction.DOWN
                    elif (event.key == pygame.K_LEFT or event.key == ord("a")) and self.direction != Direction.RIGHT:
                        self.direction = Direction.LEFT
                    elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and self.direction != Direction.LEFT:
                        self.direction = Direction.RIGHT

            if self.direction == Direction.UP:
                self.position_head[1] -= self.square_size
            elif self.direction == Direction.DOWN:
                self.position_head[1] += self.square_size
            elif self.direction == Direction.LEFT:
                self.position_head[0] -= self.square_size
            else:
                self.position_head[0] += self.square_size

            self.position_head[0] %= self.frame_size_x
            self.position_head[1] %= self.frame_size_y

            #Eating Food
            self.snake_body.insert(0, list(self.position_head))
            if (
                self.position_head[0] <= self.position_food[0] < self.position_head[0] + self.square_size
                and self.position_head[1] <= self.position_food[1] < self.position_head[1] + self.square_size
            ):
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_body.pop()

            #Spawn Food
            if not self.food_spawn:
                self.position_food = [
                    random.randrange(1, (self.frame_size_x // self.square_size)) * self.square_size,
                    random.randrange(1, (self.frame_size_y // self.square_size)) * self.square_size,
                ]
                self.food_spawn = True

            #Drawintg the game
            self.gwindow_size.fill(self.GREEN)
            for i, pos in enumerate(self.snake_body):
                if i == 0: #first pixel of the snake -- head
                    pygame.draw.rect(
                        self.gwindow_size,
                        self.YELLOW,
                        pygame.Rect(pos[0] + 2, pos[1] + 2, self.square_size - 2, self.square_size - 2)
                    )
                else:
                    pygame.draw.rect(
                        self.gwindow_size,
                        self.BROWN,
                        pygame.Rect(pos[0] + 2, pos[1] + 2, self.square_size - 2, self.square_size - 2)
                    )


            pygame.draw.rect(
                self.gwindow_size,
                self.RED,
                pygame.Rect(self.position_food[0] + 2, self.position_food[1] + 2, self.square_size -2, self.square_size -2),
            )

            #Game over condition
            if self.has_collision():
                self.game_over()

            #Displaying score
            self.score_display(1, self.RED, "consolas", 20)
            pygame.display.update()

            #Control the game speed
            self.fps_controller.tick(self.speed)





if __name__ == "__main__":
    snake_game = SnakeGame()
    snake_game.run()
    
#Please Like Share & Subscribe 
#Comment down the names of the game you will like see next
#Thanks - Cheers Peace