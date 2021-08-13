"""
author: SAYAN SARKAR
My Github id : @sayanznito

"""


import pygame
import random
import os

pygame.mixer.init()

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)

screen_height = 600
screen_width = 900
#Game Background
bg2=pygame.image.load("img2.jpg")
#bg2=pygame.transform.scale(bg2,(screen_width,screen_height)).convert_alpha()
bg1=pygame.image.load("img1.jpg")
intro=pygame.image.load("screen1.jpg")


# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TOM THE SNAKE ")
pygame.display.update()

pygame.mixer.music.load('start.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.6)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
# Game specific variables




def text_screen(text,colour,x,y):
    screen_text=font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x,y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(intro,(0,0))
        #text_screen("Welcome to TOM the Snake ",black,240,250)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3.mp3')
                    pygame.mixer.music.play(100)
                    gameloop()
        pygame.display.update()
        clock.tick(30)


#Creating a game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 25
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(15, screen_width / 2)
    food_y = random.randint(16, screen_height / 2)
    init_velocity = 8
    score = 0
    fps = 30

    snake_list = []
    snake_len = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()


    #with open("highscore.txt", "r") as f:
        #hiscore = f.read()


    while not exit_game:
        if game_over:
           with open("highscore.txt", "w") as f:
               f.write(str(highscore))
           gameWindow.fill(white)
           gameWindow.blit(bg2, (0, 0))
           text_screen("Score: " + str(score), red, 385, 410)
           #text_screen("Game Over ! Press Enter To Continue",red,100,200)


           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:


            for event in pygame.event.get():

                 if event.type == pygame.QUIT:
                    exit_game =True
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    if event.key == pygame.K_a:
                        score+=10

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x - food_x)< 10 and abs(snake_y-food_y)<10:
                score+=10
                #print("Senor Score  :",score*10)

                food_x = random.randint(15, screen_width / 2)
                food_y = random.randint(16, screen_height / 2)
                snake_len=snake_len+5
                if score>int(highscore):
                    highscore=score



            gameWindow.fill(white)
            gameWindow.blit(bg1,(0,0))
            text_screen("Senor Score :" + str(score) + "   Your High Score : " +str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('start.mp3')
                pygame.mixer.music.play(100)
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over= True
                pygame.mixer.music.load('start.mp3')
                pygame.mixer.music.play(100)


            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snake_list,snake_size)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()
