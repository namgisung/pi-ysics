import pygame

width = 800
height = 450
size = (width, height) # 게임창 크기 (window size)
screen = pygame.display.set_mode(size)
title = "Physics Simulator" # 창 제목 (window title)
pygame.display.set_caption(title)
pygame.init()


black = (0,0,0)
white = (255, 255, 255)

box1_x = 300
box1_y = 320
box2_x = 370
box2_y = 250

box1_length = 50
box2_length = 120

box1_velocity = 0
box2_velocity = -50

box1_mass = 1
box2_mass = 10000

clock = pygame.time.Clock() 
collision_num = 0

font1 = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 30)

time_step = 1000

play = True
while play: 
    delta_time_ms = clock.get_time()
    clock.tick(1000)
    dt1, dt2 = clock.tick(1000) / 1000 , clock.tick(time_step) / 1000
    dt = dt1 * dt2
    print(dt,dt1,dt2)
    # 4-2. 각종 입력 감지 (event detection)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
    for i in range(time_step):

        box2_x += box2_velocity * dt
        box1_x += box1_velocity * dt
        
        #벽 충돌
        if box1_x <= 100 and box1_velocity < 0:
            box1_velocity *= -1
            collision_num += 1
            print(collision_num)
    

        if box2_x <= box1_x + 50:
            # 완전 탄성 충돌 계산
            total_mass = box1_mass + box2_mass
            box1_velocity_final = (box1_mass - box2_mass) / total_mass * box1_velocity + (2 * box2_mass) / total_mass * box2_velocity
            box2_velocity_final = 2 * box1_mass / total_mass * box1_velocity + (box2_mass - box1_mass) / total_mass * box2_velocity

            box1_velocity = box1_velocity_final
            box2_velocity = box2_velocity_final

            collision_num += 1
            print(collision_num)
    

    screen.fill((0, 0, 0))

      # 시스템 글꼴 로드
    text1 = font1.render('collision_num : {}'.format(collision_num), True, white)
    screen.blit(text1, (110, 10))
    
    
    text2 = font2.render('blue object mass : {}'.format(box2_mass), True, white)
    screen.blit(text2, (110, 40))

    pygame.draw.line(screen,(255,255,255),(0,370),(800,370),1)
    pygame.draw.line(screen,(255,255,255),(100,370),(100,0),1)
    pygame.draw.rect(screen,(255, 0, 0),(box1_x,box1_y,box1_length,box1_length))
    pygame.draw.rect(screen,(0, 0, 255),(box2_x,box2_y,box2_length,box2_length))
    

    pygame.display.update()
    



pygame.quit()
