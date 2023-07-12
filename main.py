import pygame

width = 800
height = 450
size = (width, height) # 게임창 크기 (window size)
screen = pygame.display.set_mode(size)
title = "Physics Simulator" # 창 제목 (window title)
pygame.display.set_caption(title)

black = (0,0,0)
white = (255, 255, 255)

box1_x = 300
box1_y = 320
box2_x = 550
box2_y = 250

box1_width = 50
box2_width = 120

box1_dx = 0
box2_dx = -0.025

box1_mass = 1
box2_mass = 1000000

# 3. 게임 내 필요한 설정 (option for game)
clock = pygame.time.Clock() # 시계 (clock)
collision_num = 0

play = True
while play: 
    delta_time_ms = clock.get_time()
    # 4-2. 각종 입력 감지 (event detection)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    box2_x += box2_dx
    box1_x += box1_dx

    if box1_x <= 100:
        box1_dx *= -1
        collision_num += 1
        print(collision_num)
    if box2_x <= 100:
        box2_dx *= -1
        collision_num += 1
        print(collision_num)

    if box1_x < box2_x + box2_width and box1_x + box1_width > box2_x and box1_y < box2_y + box2_width and box1_y + box1_width > box2_y:
        # 완전 탄성 충돌 계산
        total_mass = box1_mass + box2_mass
        box1_dx_final = (box1_mass - box2_mass) / total_mass * box1_dx + 2 * box2_mass / total_mass * box2_dx
        box2_dx_final = 2 * box1_mass / total_mass * box1_dx + (box2_mass - box1_mass) / total_mass * box2_dx

        box1_dx = box1_dx_final
        box2_dx = box2_dx_final

        collision_num += 1
        print(collision_num)
    

    screen.fill((0, 0, 0))

    pygame.draw.line(screen,(255,255,255),(0,370),(800,370),1)
    pygame.draw.line(screen,(255,255,255),(100,370),(100,0),1)
    pygame.draw.rect(screen,(255, 0, 0),(box1_x,box1_y,box1_width,box1_width))
    pygame.draw.rect(screen,(0, 0, 255),(box2_x,box2_y,box2_width,box2_width))
    

    pygame.display.update()
    clock.tick(1440)



pygame.quit()
