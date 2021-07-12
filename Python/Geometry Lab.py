from tkinter import *
import turtle
import random
import pygame
import sys
import time
from time import perf_counter
from pygame.locals import *
# 主窗口
def mainWindow():
    mainWindow = Tk()
    mainWindow.title('Geometry Lab') # 主窗口title
    mainWindow.geometry('600x450') # 主窗口大小
    mainWindow.attributes('-alpha', 0.9) # 主窗口透明度
    mainWindow.resizable(0,0) # 主窗口大小不可更改
    mainWindowText1 = Text(mainWindow, width=20, height=1, font=('Comic Sans Ms', 40), fg='red', highlightbackground='white', highlightcolor='white')
    mainWindowText1.pack(anchor=CENTER)
    mainWindowText1.insert(INSERT, 'Welcome to Geometry Lab\n')
    mainWindowButton1 = Button(text='1.蒙特卡洛法估算圆周率', width=30, height=2, font=('Times', 35), fg='darkorange', command=inputDots)
    mainWindowButton1.pack(anchor=CENTER)
    mainWindowButton2 = Button(text='2.蒙特卡洛法估算定积分', width=30, height=2, font=('Times', 35), fg='limegreen', command=printTip)
    mainWindowButton2.pack(anchor=CENTER)
    mainWindowButton3 = Button(text='3.一个小彩蛋：贪吃蛇OvO', width=30, height=2, font=('Times', 35), fg='blue', command=snake)
    mainWindowButton3.pack(anchor=CENTER)
    mainWindowText2 = Text(mainWindow, width=20, height=2, font=('Comic Sans Ms', 40), fg='darkviolet', highlightbackground='white', highlightcolor='white')
    mainWindowText2.pack(anchor=CENTER)
    mainWindowText2.insert(INSERT, 'Developers:\n')
    mainWindowText2.insert(END, '  吴茂壮  &  陈金麟')
    mainWindow.mainloop()
# 输入模拟点数 在inputDots中调用monteCarloPI
def inputDots():
    inputDots = Tk()
    inputDots.title('Input Dots')
    inputDots.geometry('600x150')
    inputDots.attributes('-alpha', 0.9)
    inputDots.resizable(0,0)
    def getDots():
        str = inputDotsBox.get()
        num = int(str)
        monteCarloPI(num) # 一定要把monteCarloPI放在getDots中
    inputDotsText = Text(inputDots, width=20, height=1, font=('times', 40), fg='red', highlightbackground='white', highlightcolor='white')
    inputDotsText.pack(anchor=CENTER)
    inputDotsText.insert(INSERT, '请输入要模拟的点数：\n')
    inputDotsBox = Entry(inputDots, highlightcolor='blue', highlightthickness=5) # 输入框
    inputDotsBox.pack(anchor=CENTER)
    inputDotsButton = Button(inputDots, text='确定', font=('Times', 30), command=getDots)
    inputDotsButton.pack(side='right')
    inputDots.mainloop()

def printTip():
    inputDots = Tk()
    inputDots.title('Tip')
    inputDots.geometry('600x150')
    inputDots.attributes('-alpha', 0.9)
    inputDots.resizable(0,0)
    inputDotsText = Text(inputDots, width=10, height=2, font=('Times', 40), fg='red', highlightbackground='white', highlightcolor='white')
    inputDotsText.pack(anchor=CENTER)
    inputDotsText.insert(INSERT, '即将推出\n')
    inputDotsText.insert(END, '敬请期待')
    inputDots.mainloop()

def monteCarloPI(n):
    def D(x, y):
        return x-235, y-160

    def set_up():
        turtle.setup(width=0.5, height=0.8, startx=None, starty=0)
        turtle.ht()
    
    def title():
        turtle.penup()
        turtle.goto(D(230,470))
        turtle.write('蒙特卡洛法估算PI',False,'center',font=("Times",35))
    
    def x_y(pen, x_name='x', y_name='y'):
        pen.pensize(2)
        turtle.tracer(0)
        pen.up()
        pen.goto(D(0, 0))
        pen.down()
        pen.goto(D(500, 0));pen.goto(D(495, 5));pen.goto(D(500, 0));pen.goto(D(495, -5))
        pen.up();pen.goto(D(500, -26));pen.write(x_name,font=("Times",20))
        pen.goto(D(0, 0))
        pen.down()
        pen.goto(D(0, 500));pen.goto(D(-5, 495));pen.goto(D(0, 500));pen.goto(D(5, 495))
        pen.up();pen.goto(D(-16, 495));pen.write(y_name,font=("Times",20))
        pen.up();pen.goto(D(0, 450));pen.down();pen.goto(D(450, 450));pen.goto(D(450, 0))
        pen.up()
    
    def ready():
        turtle.pensize(2)
        turtle.pencolor('red')
        turtle.penup()
        turtle.goto(D(0,450))
        turtle.pendown()
        turtle.circle(-450, 90)
        turtle.speed(0)
        turtle.delay(0)
        turtle.tracer(False)
        turtle.pencolor('black')

    def show_count(count,DARTS):
        c=int((count/DARTS)*100)
        a,b='*'* (c//4),'.'*(25-(c//4))
        turtle.goto(D(235,-95))
        turtle.pencolor("black")
        turtle.write('{:3.0f} %[{}->{}] {:.0f} / {}'.format(c,a,b,count,DARTS),False,'center',font=("Times",20))
        turtle.undo()

    def hiiiiiit(count=0):
        for i in range(1, DARTS+1):
            x, y = random.random(), random.random()
            dist = pow(x ** 2 + y ** 2, 0.5)
            turtle.penup()
            if dist <=1.0:
                turtle.pencolor("green")
                turtle.goto(D(450*x,450*y))
                turtle.pendown()
            elif dist>1:
                turtle.pencolor("blue")
                turtle.goto(D(450*x,450*y))
                turtle.pendown()
            turtle.dot(4)
            turtle.penup()
            if dist <= 1.0:
                global hits
                hits = hits + 1
            count=count+1
            show_count(count,DARTS)
    
    def pi_formula(hits ,DARTS):
        pi = 4 * (hits/DARTS)
        return pi
    
    def text(hits ,DARTS):
        turtle.pencolor("black")
        turtle.goto(D(230,-60))
        turtle.write("{:.0f} 个点落入圆内".format(hits),False,'center',font=("Times",20))
        turtle.goto(D(230,-90))
        turtle.write("{:.0f} 个点落在圆外".format(DARTS - hits),False,'center',font=("Times",20))
        turtle.goto(D(230,-128))
        turtle.pencolor("red")
        turtle.write("PI = {:.4f}".format(pi_formula(hits ,DARTS)),False,'center',font=("Times",30))
        turtle.pencolor("black")
        turtle.goto(D(230,-160))
        turtle.write("运行时间： {:.4f}s".format(perf_counter() - start),False,'center',font=("Times",20))
        turtle.fd(50)
        turtle.done()

    DARTS = n
    t = turtle.Pen()
    set_up()
    title()
    t.ht()
    x_y(t)
    ready()
    start = perf_counter()
    hiiiiiit()
    text(hits ,DARTS)

def snake():
    redColour = pygame.Color(255,0,0)
    blackColour = pygame.Color(0,0,0)
    whiteColour = pygame.Color(255,255,255)
    greyColour = pygame.Color(150,150,150)

    def gameOver(playSurface):
        gameOverFont = pygame.font.Font('/System/Library/Fonts/Supplemental/Comic Sans MS.ttf',80)
        gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (320, 10)
        playSurface.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()

    def main():
        pygame.init()
        fpsClock = pygame.time.Clock()
        playSurface = pygame.display.set_mode((640,480))
        pygame.display.set_caption('Snake')
        snakePosition = [100,100]
        snakeSegments = [[100,100],[80,100],[60,100]]
        raspberryPosition = [300,300]
        raspberrySpawned = 1
        direction = 'right'
        changeDirection = direction
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT or event.key == ord('d'):
                        changeDirection = 'right'
                    if event.key == K_LEFT or event.key == ord('a'):
                        changeDirection = 'left'
                    if event.key == K_UP or event.key == ord('w'):
                        changeDirection = 'up'
                    if event.key == K_DOWN or event.key == ord('s'):
                        changeDirection = 'down'
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
            if changeDirection == 'right' and not direction == 'left':
                direction = changeDirection
            if changeDirection == 'left' and not direction == 'right':
                direction = changeDirection
            if changeDirection == 'up' and not direction == 'down':
                direction = changeDirection
            if changeDirection == 'down' and not direction == 'up':
                direction = changeDirection
            if direction == 'right':
                snakePosition[0] += 20
            if direction == 'left':
                snakePosition[0] -= 20
            if direction == 'up':
                snakePosition[1] -= 20
            if direction == 'down':
                snakePosition[1] += 20
            snakeSegments.insert(0,list(snakePosition))
            if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
                raspberrySpawned = 0
            else:
                snakeSegments.pop()
            if raspberrySpawned == 0:
                x = random.randrange(1,32)
                y = random.randrange(1,24)
                raspberryPosition = [int(x*20),int(y*20)]
                raspberrySpawned = 1
            playSurface.fill(blackColour)
            for position in snakeSegments:
                pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
                pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1],20,20))
            pygame.display.flip()
            if snakePosition[0] > 620 or snakePosition[0] < 0:
                gameOver(playSurface)
            if snakePosition[1] > 460 or snakePosition[1] < 0:
                for snakeBody in snakeSegments[1:]:
                    if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                        gameOver(playSurface)
            fpsClock.tick(10)

    if __name__ == "__main__":
        main()

hits = 0
mainWindow()