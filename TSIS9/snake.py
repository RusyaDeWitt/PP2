import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def first_snake_score(score):
    value = score_font.render("Snake 1: " + str(score), True, red)
    dis.blit(value, [0, 0])

def second_snake_score(score_2):
    value = score_font.render("Snake 2: " + str(score_2), True, yellow)
    dis.blit(value, [0, 350])

def snake_one(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def snake_two(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x2 = dis_width / 2
    y2 = dis_height / 2

    x1_change = 0
    y1_change = 0

    x2_change = 0
    y2_change = 0

    first_snake_List = []
    Length_of_first_snake = 1

    second_snake_List = []
    Length_of_second_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0


    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            snake_one(Length_of_first_snake - 1, first_snake_List)
            snake_two(Length_of_second_snake - 1, second_snake_List)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_a:
                    x2_change = -snake_block
                    y2_change = 0
                elif event.key == pygame.K_d:
                    x2_change = snake_block
                    y2_change = 0
                elif event.key == pygame.K_w:
                    y2_change = -snake_block
                    x2_change = 0
                elif event.key == pygame.K_s:
                    y2_change = snake_block
                    x2_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:         #1LEVEL
            game_close = True
        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            game_close = True
        if Length_of_first_snake - 1 == 5 or Length_of_second_snake - 1 % 5 == 5:       #2 LEVEL
            if x1 >= dis_width-20 or x1 < 0 or y1 >= dis_height-20 or y1 < 0:
                game_close = True
            if x2 >= dis_width-20 or x2 < 0 or y2 >= dis_height-20 or y2 < 0:
                game_close = True
        if Length_of_first_snake - 1 == 10 or Length_of_second_snake - 1 == 10:     #3 LEVEL
            if x1 >= dis_width-50 or x1 < 0 or y1 >= dis_height-50 or y1 < 0:
                game_close = True
            if x2 >= dis_width-50 or x2 < 0 or y2 >= dis_height-50 or y2 < 0:
                game_close = True

        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        first_snake_Head = []
        first_snake_Head.append(x1)
        first_snake_Head.append(y1)
        first_snake_List.append(first_snake_Head)
        if len(first_snake_List) > Length_of_first_snake:
            del first_snake_List[0]

        second_snake_Head = []
        second_snake_Head.append(x2)
        second_snake_Head.append(y2)
        second_snake_List.append(second_snake_Head)
        if len(second_snake_List) > Length_of_second_snake:
            del second_snake_List[0]

        for x in first_snake_List[:-1]:
            if x == first_snake_Head:
                game_close = True
        for x in second_snake_List[:-1]:
            if x == second_snake_Head:
                game_close = True

        snake_one(snake_block, first_snake_List)
        snake_two(snake_block, second_snake_List)
        first_snake_score(Length_of_first_snake - 1)
        second_snake_score(Length_of_second_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_first_snake += 1

        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_second_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()