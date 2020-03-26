try:
    import pygame
    import random
    from math import sqrt as sqrt
    import simpleaudio as sa

    # Initialize Game
    pygame.init()

    # Create Screen
    screen = pygame.display.set_mode((1600, 900))

    screen.fill((30, 0, 0))

    # Title And Logo
    pygame.display.set_caption("Python's Corona")
    icon = pygame.image.load('moment/bat_right.png')
    pygame.display.set_icon(icon)

    easy_button = pygame.image.load('moment/easy.png')
    screen.blit(easy_button, (1000, 450))

    normal_button = pygame.image.load('moment/normal.png')
    screen.blit(normal_button, (1000, 550))

    hard_button = pygame.image.load('moment/hard.png')
    screen.blit(hard_button, (1000, 650))

    bat_image = pygame.image.load('moment/bat.png')
    screen.blit(bat_image, (1000, 100))

    font = pygame.font.Font('moment/Painter-LxXg.ttf', 190)
    pythons_text = font.render("Python's", True, (255, 0, 0), (30, 0, 0))
    pythons_textRect = pythons_text.get_rect()
    pythons_textRect.center = (399, 239)
    screen.blit(pythons_text, pythons_textRect)
    corona_text = font.render("Corona", False, (255, 0, 0), (30, 0, 0))
    corona_textRect = corona_text.get_rect()
    corona_textRect.center = (423, 423)
    screen.blit(corona_text, corona_textRect)
    font_1 = pygame.font.Font('moment/NightmarePills-BV2w.ttf', 50)
    caution_text = font_1.render("CAUTION:No Horror", False, (255, 0, 0), (30, 0, 0))
    caution_textRect = caution_text.get_rect()
    caution_textRect.center = (270, 830)
    screen.blit(caution_text, caution_textRect)
    pygame.display.update()

    cure_bottles_picked = 0
    bottles_need = 30

    bool_run = True
    def atStart():
        global bool_run
        global bottles_need
        while bool_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
##                elif event.type == pygame.KEYDOWN:
##                    print(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > 1000 and event.pos[0] < 1227 and event.pos[1] > 450 and event.pos[1] < 500:
                        # print("Clicked Easy")
                        bool_run = False
                    elif event.pos[0] > 1000 and event.pos[0] < 1227 and event.pos[1] > 550 and event.pos[1] < 600:
                        bottles_need = 60
##                        print("Clicked Normal")
                        bool_run = False
                    elif event.pos[0] > 1000 and event.pos[0] < 1227 and event.pos[1] > 650 and event.pos[1] < 700:
                        bottles_need = 90
##                        print("Clicked Hard")
                        bool_run = False
    atStart()

    global player
    player = pygame.image.load('moment/mini_player_right.png')
    global player_x, player_y, x_front_move, x_back_move, y_front_move, y_back_move
    player_x, player_y = 200, 500
    x_front_move = False
    y_front_move = False
    x_back_move = False
    y_back_move = False

    cure = pygame.image.load('moment/cure.png')
    cure_pos = [(100, 100)]

    global stop_move
    stop_move = False

    corona = [pygame.image.load('moment/corona.png')]
    number_of_corona = bottles_need/30
    corona_pos = [100, 300]

    def playerMoment(x, y):
        screen.blit(player, (x, y))

    def cureUpdate():
        global cure_bottles_picked, bool_run
        screen.blit(cure, cure_pos[0])
        if abs(player_x - cure_pos[0][0]) < 20 and abs(player_y - cure_pos[0][1]) < 20:
            cure_pos[0] = (random.randint(50, 1600), random.randint(50, 900))
            filename = 'moment/collect.wav'
            wave_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wave_obj.play()
            if cure_bottles_picked == bottles_need:
##                print("You Win")
                bool_run = False
            cure_bottles_picked +=1
        else:
            distance = pow((player_x - cure_pos[0][0]) * (player_x - cure_pos[0][0]) + (player_y - cure_pos[0][1]) * (player_y - cure_pos[0][1]), 0.5)
            if distance < 5:
                cure_pos[0] = (random.randint(50, 1530), random.randint(50, 830))
                filename = 'moment/collect.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                if cure_bottles_picked == bottles_need:
##                    print("You Win")
                    bool_run = False
                cure_bottles_picked +=1

    def coronaMoment(x, y):
        # Corona need to move to players position
        dir_x = player_x - corona_pos[0]
        dir_y = player_y - corona_pos[1];

        hyp = sqrt(dir_x*dir_x + dir_y*dir_y)

        speed = number_of_corona/10 + 0.3

        dir_x /= hyp
        dir_y /= hyp

        corona_pos[0] += dir_x*speed
        corona_pos[1] += dir_y*speed

        screen.blit(corona[0], (corona_pos[0], corona_pos[1]))

    def moveUpdate():
        global player, bool_playing
        if stop_move:
##            print("should stop")
            pass
        else:
            global player_x, player_y
            if x_front_move:
                if player_x < 1530:
                    player = pygame.image.load('moment/mini_player_right.png')
                    player_x += 0.7
                    if not bool_playing:
                        pygame.mixer.music.play(-1)
                        bool_playing = True
                else:
                    pygame.mixer.music.stop()
                    bool_playing = False
            elif x_back_move:
                if player_x > 0:
                    player = pygame.image.load('moment/mini_player_left.png')
                    player_x -= 0.7
                    if not bool_playing:
                        pygame.mixer.music.play(-1)
                        bool_playing = True
                else:
                    pygame.mixer.music.stop()
                    bool_playing = False
            elif y_front_move:
                if player_y > 0:
                    player = pygame.image.load('moment/mini_player_up.png')
                    player_y -= 0.7
                    if not bool_playing:
                        pygame.mixer.music.play(-1)
                        bool_playing = True
                else:
                    pygame.mixer.music.stop()
                    bool_playing = False
            elif y_back_move:
                if player_y < 830:
                    player = pygame.image.load('moment/mini_player_down.png')
                    player_y += 0.7
                    if not bool_playing:
                        pygame.mixer.music.play(-1)
                        bool_playing = True
                else:
                    pygame.mixer.music.stop()
                    bool_playing = False

    global bool_playing
    bool_playing = False
    bool_run = True
    pygame.mixer.music.load('moment/running.wav')
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.stop()
    while bool_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_front_move = True
                    stop_move = False
                elif event.key == pygame.K_LEFT:
                    x_back_move = True
                    x_front_move = False
                    stop_move = False
                elif event.key == pygame.K_UP:
                    y_front_move = True
                    x_back_move = False
                    x_front_move = False
                    stop_move = False
                elif event.key == pygame.K_DOWN:
                    y_back_move = True
                    x_back_move = False
                    x_front_move = False
                    y_front_move = False
                    stop_move = False
                elif event.key == pygame.K_SPACE:
                    x_front_move = False
                    x_back_move = False
                    y_front_move = False
                    y_back_move = False
        font_3 = pygame.font.Font('moment/CursedTimerUlil-Aznm.ttf', 300)
        score_text = font_3.render(str(cure_bottles_picked)+":"+str(bottles_need), False, (255, 0, 0), (0, 0, 0))
        score_textRect = score_text.get_rect()
        score_textRect.center = (800, 450)
        screen.fill((0, 0, 0))
        screen.blit(score_text, score_textRect)
        moveUpdate()
        playerMoment(player_x, player_y)
        coronaMoment(player_x, player_y)
        cureUpdate()
        pygame.display.update()
        print(bool_playing)
        distance = pow((player_x - corona_pos[0]) * (player_x - corona_pos[0]) + (player_y - corona_pos[1]) * (player_y - corona_pos[1]), 0.5)
        if distance < 19:
##            print("Game Over")
            break

    pygame.mixer.music.stop()
    screen.fill((30, 0, 0))
    font_2 = pygame.font.Font('moment/NightmarePills-BV2w.ttf', 150)
    if bool_run == False:
        end_text = font_2.render("YOU WIN", False, (255, 0, 0), (30, 0, 0))
    else:
        end_text = font_2.render("YOU LOOSE", False, (255, 0, 0), (30, 0, 0))
    end_textRect = caution_text.get_rect()
    end_textRect.center = (670, 390)
    screen.blit(end_text, end_textRect)
    pygame.display.update()
    bool_run = True
    while bool_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bool_run = False
except e:
    print(e)
