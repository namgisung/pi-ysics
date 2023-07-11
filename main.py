import pygame

class box():
    def __init__(self,x,y,length,mass,vect,color) :
        self.x_y = (x,y)
        self.mass = mass
        self.length = length
        self.velocity = vect
        self.color = color

    


width = 800
height = 450
size = (width, height) # 게임창 크기 (window size)
screen = pygame.display.set_mode(size)
title = "Physics Simulator" # 창 제목 (window title)
pygame.display.set_caption(title)

black = (0,0,0)
white = (255, 255, 255)

box1_x = 100
box1_y = 200
box2_x = 500
box2_y = 200

box_length = 50

box1_dx = -5
box2_dx = 0




# 3. 게임 내 필요한 설정 (option for game)
clock = pygame.time.Clock() # 시계 (clock)

play = True
while play: 
    delta_time_ms = clock.get_time()
    # 4-2. 각종 입력 감지 (event detection)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    pygame.draw.line(screen,(255,255,255),(0,370),(800,370),3)
    pygame.draw.line(screen,(255,255,255),(100,370),(100,0),3)

    pygame.display.update()
    clock.tick()



pygame.quit()
print
