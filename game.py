import pygame

image_path= '/data/data/com.org.test.ulykpan/files/app/'

clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((600 , 360))
pygame.display.set_caption('newline')
running=True
bg=pygame.image.load( 'venv/share/man/man1/360_F_88981880_YjJManMJ6hJmKr5CZteFJAkEzXIh8mxW.jpg').convert_alpha()
walk=[
    pygame.image.load( 'venv/share/man/player/x1670754087.png.pagespeed.ic.Mm-kzS5ir9.png').convert_alpha() ,
    pygame.image.load( 'venv/share/man/player/x1670754090.png.pagespeed.ic.EH9Ha_DKYl.png').convert_alpha() ,
    pygame.image.load( 'venv/share/man/player/x1670754092.png.pagespeed.ic.Mm-kzS5ir9.png').convert_alpha() ,
    pygame.image.load( 'venv/share/man/player/x1670754094.png.pagespeed.ic.z7wU1JdYm-.png').convert_alpha()
]


animated=0
bg_count = 0
sound=pygame.mixer.Sound( 'venv/share/man/player/Peggy Gou - (It Goes Like) Nanana (Edit).mp3')
sound.play()
player_speed = 5
player_x = 100
player_y = 215
is_jump = False
jump_count = 9
moster=pygame.image.load( 'venv/share/man/player/imgonline-com-ua-Resize-oLec3HVKlhC6e.png').convert_alpha()

moster_time = pygame.USEREVENT + 1
pygame.time.set_timer(moster_time , 3500)
moster_in_game = []
gameplay=True

label= pygame.font.Font('venv/share/man/man1/RubikScribble-Regular.ttf', 40)
lose_label= label.render('You are loser!' , False , (15 ,15 ,15))
restart_label= label.render('RESTART' , False , (15 ,15 ,15))
restart_label_rect=restart_label.get_rect(topleft=(160 , 150))

bullet=pygame.image.load( 'venv/share/man/man1/right-arrow.png').convert_alpha()
bullets=[]
count=0

while running:

    screen.blit(bg ,(bg_count,0))
    screen.blit(bg , (bg_count + 600 , 0))

    if gameplay:
        player_rect = walk[0].get_rect(topleft = (player_x , player_y ))

        if moster_in_game:
            for (i, el) in enumerate(moster_in_game):
                screen.blit(moster , el)
                el.x -= 10

                if el.x < -10:
                    moster_in_game.pop(i)


                if player_rect.colliderect(el ):
                    gameplay = False

        screen.blit(walk[animated] , (player_x , player_y))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -9:
                if jump_count  > 0:
                    player_y -= (jump_count ** 2 ) / 2
                else:
                    player_y += (jump_count ** 2 ) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9


        if animated == 3:
            animated = 0
        else:
            animated += 1

        bg_count -= 2
        if bg_count == -618:
            bg_count = 0



        if bullets:
            for (i , el) in enumerate(bullets):
                screen.blit(bullet , (el.x ,el.y))
                el.x += 4

                if el.x > 600:
                    bullets.pop(i)
                if moster_in_game:
                    for(index , moster_num) in enumerate(moster_in_game):
                        if el.colliderect(moster_num):
                            moster_in_game.pop(index)
                            bullets.pop(i)
                            count += 1
                            if count == 5:
                                pygame.time.set_timer(moster_time , 3000)
                            elif count == 10:
                                pygame.time.set_timer(moster_time , 2000)
                            elif count == 15:
                                pygame.time.set_timer(moster_time , 1000)

    else:
        screen.fill((237 , 219 , 218))
        screen.blit(lose_label , (160 , 100))
        screen.blit(restart_label , restart_label_rect)

        mouse=pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x= 100
            moster_in_game.clear()
            bullets.clear()





    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type == moster_time:
            moster_in_game.append(moster.get_rect(topleft = (620 , 215)))
        if gameplay and event.type == pygame.KEYUP and event.key ==pygame.K_w:
            bullets.append(bullet.get_rect(topleft=(player_x + 20 , player_y + 5)))



    clock.tick(13)
