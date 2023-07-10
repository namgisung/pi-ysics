import pygame, pymunk, pymunk.pygame_util
import math
from pygame.math import Vector2
# pip install pygame으로 pygame 설치, pip install pymunk로 pymunk 설치

import pygame, pymunk, pymunk.pygame_util
# pip install pygame으로 pygame 설치, pip install pymunk로 pymunk 설치


class Ball():
    def __init__(self,x,y,velocity,box_length):
        self.body = pymunk.Body()
        self.body.position = (x,y)
        self.body.velocity = velocity
        self.body_box_length = box_length
        self.shape = pymunk.Poly.create_box(self.body, (box_length,box_length))
        self.shape.elasticity = 1
        self.shape.friction = 0
        space.add(self.body, self.shape)
        self.shape.collision_type = 1
    
    def draw(self):
        box_length = self.body_box_length
        x, y = self.body.position
        pygame.draw.rect(screen, (255, 255, 255), (int(x),int(y),box_length,box_length))

class Wall():
    def __init__(self,p1,p2,collision_number=None):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1, p2, 1)
        self.shape.elasticity = 1
        space.add(self.body)
        if collision_number:
            self.shape.collision_type = collision_number

    def draw(self):
        pygame.draw.line(screen, (255,255,255), self.shape.a, self.shape.b, 10)

# 1. 게임 초기화 (game initialize)
pygame.init()

# 2. 게임창 옵션 설정 (window option)
width = 800
height = 450
size = (width, height) # 게임창 크기 (window size)
screen = pygame.display.set_mode(size)
title = "Physics Simulator" # 창 제목 (window title)
pygame.display.set_caption(title)

black = (0,0,0)
white = (255, 255, 255)

# 3. 게임 내 필요한 설정 (option for game)
clock = pygame.time.Clock() # 시계 (clock)
# 공간 만들기 (space)
space = pymunk.Space()
space.gravity = (0, 50)
draw_options = pymunk.pygame_util.DrawOptions(screen)

box1_velocity = (0,0)
box1_length = 40
box2_velocity = (3,0)
box2_length = 100



fbox = Ball(size[0]/2,size[1]-75,box1_velocity,box1_length)
sbox = Ball(2*size[0]/3,size[1]-100,box2_velocity,box2_length)
sfloor = Wall((0,0),(size[0],0),2)
swall = Wall((0,0), (0,-400),2)
# 4. 메인 이벤트 (main event)
running = True
while running:

    # 4-1. FPS 설정 (frame per second)
    clock.tick(60) # 메인 이벤트 반복이 1초에 60회 (60 frames per 1 second)
    space.step(1/60) # 시뮬레이션 주기 (Simulation cycle)
    # 4-2. 각종 입력 감지 (event detection)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    fbox.draw()
    sbox.draw()
    sfloor.draw()
    swall.draw()

    dt = 1.0 / 60
    space.step(dt)

        # Check for collisions with other balls
    

    # 4-3. 입력, 시간에 따른 변화 (change with event or time)
    
    # 4-4. 그리기 (drawing)
    screen.fill((0,0,0))
    space.debug_draw(draw_options)
    # 4-5. 업데이트 (update)
    
    pygame.display.flip()

    clock.tick(60)

# 5. 게임 종료 (quit)
pygame.quit()
