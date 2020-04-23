import datetime
import time
import os

import pygame


def timePro(t):
    str_time = str(t)
    min = str_time[2:4]
    sec = str_time[5:7]
    protime = "[" + min + ":" + sec + "]"
    return protime


pygame.init()
screen = pygame.display.set_mode((300, 360))
pygame.display.set_caption("Only For Lrc")  # 设置窗口标题
myfont = pygame.font.SysFont('arial', 20)
white = 255, 255, 255
textImage = myfont.render("Press Space to Start", True, white)
screen.blit(textImage, (50, 80))
pygame.display.update()

# How many lines are there in the origin lrc file?
f1 = open('lrc.txt', 'r', encoding='utf-8')
linenum = len(f1.readlines())
f1.close()
while True:
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        screen.fill((0, 0, 0))
        textImage = myfont.render("Press C to Cut, V to Finish :)", True, white)
        screen.blit(textImage, (20, 80))
        pygame.display.update()
        starttime = datetime.datetime.now()
        while True:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_c]:
                endtime = datetime.datetime.now()
                correnttime = endtime - starttime

                screen.fill((0, 0, 0))
                textImage = myfont.render("Press C to Cut, V to Finish :D", True, white)
                screen.blit(textImage, (20, 80))
                pygame.display.update()

                time.sleep(0.7)

                screen.fill((0, 0, 0))
                textImage = myfont.render("Press C to Cut, V to Finish :)", True, white)
                screen.blit(textImage, (20, 80))
                pygame.display.update()

                final = timePro(correnttime)
                print(final)
                with open('time.txt', 'a+') as f:
                    f.write(final + '\n')
            if keystate[pygame.K_v]:
                f1 = open('lrc.txt', 'r', encoding='utf-8')
                f2 = open('time.txt', 'r', encoding='utf-8')
                for i in range(linenum):
                    try:
                        lrc = f1.readline()
                        t1 = f2.readline()
                        line = t1.strip() + lrc
                        with open('output.lrc', 'a+') as f:
                            f.write(line)
                    except:
                        break
                f1.close()
                f2.close()
                f.close()
                os.remove('time.txt')
                for event in pygame.event.get():
                    screen.fill((0, 0, 0))
                    thisfont = pygame.font.SysFont('arial', 17)
                    textImage = thisfont.render("Check your output at output.lrc!", True, white)
                    screen.blit(textImage, (12, 80))
                    pygame.display.update()
                    time.sleep(4)
                    screen.fill((0, 0, 0))
                    textImage = myfont.render("Bye!", True, white)
                    screen.blit(textImage, (120, 80))
                    pygame.display.update()
                    time.sleep(0.2)
                    pygame.quit()

            # Exit this loop properly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    # Exit this loop properly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


