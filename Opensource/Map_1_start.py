import pygame
import map
import virus
import time
import GameOver
import challenge
from tower.tower import tower
from tower.shorttower import short_tower
from tower.longtower import long_tower
from tower.supporttower import support_tower






def Map_1_starting(screen) :
    chal = [0,0,0,0,0,0,0,0,0]
    chal_sv = [0,0,0,0,0,0,0,0,0]
    touer = [False, False, False, False]
    chal_scr = [500, 1000, 2000, 4000,6000,2000, 500, 3000, 5000] #도전과제 달성시 보상
    chal_money = [100,200,350,550,700,200,100,500,0]

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    back_ground = pygame.image.load("image/virus/map2.png")
    interface = pygame.image.load("image/virus/interface.png")
    map1 = map.map(screen)
    map1.ch = [[120,60],[120,420],[300,420],[300,180],[540,180],[540,420],[780,420],[780,720]]
    map1.set([0, 60], [1280, 600])

    chal_img = []
    chal_img.append(pygame.image.load("image/challenge/chal_1.png"))
    chal_img.append(pygame.image.load("image/challenge/chal_2.png"))
    chal_img.append(pygame.image.load("image/challenge/chal_3.png"))
    chal_img.append(pygame.image.load("image/challenge/chal_4.png"))
    chal_img.append(pygame.image.load("image/challenge/chal_5.png"))
    chal_img.append(pygame.image.load("image/challenge/chal_6.png"))
    chal_img.append(pygame.image.load("image/challenge/chal_7.png"))
    chal_img.append(pygame.image.load("image/challenge/chal_8.png"))


    support_index = []

    life = 20
    tower1 = []
    enemy1 = []
    index = -1
    vindex = -1
    timg = []
    timg.append(pygame.image.load("tower/normal_tower1.png"))
    timg.append(pygame.image.load("tower/short_tower1.png"))
    timg.append(pygame.image.load("tower/long_tower1.png"))
    timg.append(pygame.image.load("tower/support_tower1.png"))
    cancel_img = pygame.image.load("tower/cancel.png")
    build = 0
    build_ok = True
    game_timer = time.time()
    old_time = game_timer
    gold = 1000
    round123 = 0
    count = 0
    Font = pygame.font.Font(None, 52)
    font = pygame.font.Font(None, 26)
    vtimer = time.time()
    screen.blit(back_ground, (0, 0))
    map1.draw()
    Gameoverbool = False

## 바이러스

    badguy = []

    selectNum = -1

    count = 0
    type_virus = 0
    # bgm
    pygame.mixer.init()
    pygame.mixer.music.load("sound/gamebgm.wav")
    pygame.mixer.music.set_volume(0.1)  # 1 ~ 0.1

    pygame.mixer.music.play()

    pygame.mixer.Sound("sound/gamebgm.wav")


    while True :

        screen.blit(back_ground, (0, 0))
        screen.blit(interface, (1030, 0))
        map1.draw()
        pygame.display.flip()

        oldtime = time.time()
        curtime = time.time()




        while True : #Copyright : 노관태
            timer = Font.render("Time : " + str(int(10-(curtime-oldtime))),True,(0,0,0)) #Copyright : 노관태

            screen.blit(back_ground, (0, 0))
            screen.blit(interface, (1030, 0))
            if(curtime-oldtime < 10) :
                screen.blit(timer,(850,20))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()

                    for n in range(0, len(badguy)): # Copyright : 이동우 ~
                        badguy[n].calDistance(position[0], position[1])
                    for i in range(0, len(badguy)):
                        if badguy[i].boolDtc():
                            selectNum = i
                            break
                        selectNum = -1 # ~ Copyright : 이동우


                    if build == 0:  # made by 김재희~
                        for i in range(0, len(tower1)):
                            if tower1[i].selected:
                                if position[0] >= 1048 and position[0] <= 1048 + tower1[i].sell.get_width():
                                    if position[1] >= 512 and position[1] <= 512 + tower1[i].sell.get_height():
                                        gold += tower1[i].sell_tower()
                                        if tower1[i].is_support == True:
                                            for k in range(0, len(support_index)):
                                                if support_index[k] == i:
                                                    support_index.pop(k)
                                                    break
                                            for k in range(0, len(tower1)):
                                                if tower1[k].is_support == False:
                                                    tower1[k].plus_damage = 0
                                        tower1.pop(i)
                                        index -= 1
                                        break
                                    if position[1] >= 459 and position[1] <= 459 + tower1[i].upgrade.get_height():
                                        if tower1[i].level <= 2:
                                            if gold >= tower1[i].upgrade_price[tower1[i].level]:
                                                if tower1[i].level == 2:
                                                    tower1[i].upgrade_tower()
                                                else:
                                                    gold -= tower1[i].upgrade_tower()
                                else:
                                    tower1[i].selected = tower1[i].select_tower(position[0], position[1])
                            else:
                                tower1[i].selected = tower1[i].select_tower(position[0], position[1])

                        if position[0] >= 1050 and position[0] <= 1050 + timg[0].get_width() and \
                                position[1] >= 110 and position[1] <= 110 + timg[0].get_height():
                            if gold >= 50:
                                gold -= 50
                                index += 1
                                build += 1
                                tower1.append(tower())
                                tower1[index].timer = time.time()
                        if position[0] >= 1170 and position[0] <= 1170 + timg[1].get_width() and \
                                position[1] >= 110 and position[1] <= 110 + timg[1].get_height():
                            if gold >= 100:
                                gold -= 100
                                index += 1
                                build += 1
                                tower1.append(short_tower())
                                tower1[index].timer = time.time()
                        if position[0] >= 1050 and position[0] <= 1050 + timg[2].get_width() and \
                                position[1] >= 230 and position[1] <= 230 + timg[2].get_height():
                            if gold >= 100:
                                gold -= 100
                                index += 1
                                build += 1
                                tower1.append(long_tower())
                                tower1[index].timer = time.time()
                        if position[0] >= 1170 and position[0] <= 1170 + timg[3].get_width() and \
                                position[1] >= 230 and position[1] <= 230 + timg[3].get_height():
                            if gold >= 100:
                                gold -= 100
                                index += 1
                                build += 1
                                tower1.append(support_tower())
                                support_index.append(index)
                                tower1[index].timer = time.time()
                    elif build == 1:
                        for i in range(0, len(tower1)):
                            if (i != index):
                                if (position[0] <= tower1[i].x + timg[0].get_width() / 2 and position[0] >= tower1[
                                    i].x - timg[0].get_width() / 2 \
                                        and position[1] <= tower1[i].y + timg[0].get_height() / 2 and position[1] >=
                                        tower1[i].y - timg[0].get_height() / 2):
                                    build_ok = False
                                    break
                                else:
                                    build_ok = True
                        if build_ok == True:
                            build -= 1
                            if tower1[index].tower_name == "normal tower" :
                                touer[0] = True
                            if tower1[index].tower_name == "short tower" :
                                touer[1] = True
                            if tower1[index].tower_name == "long tower" :
                                touer[2] = True
                            if tower1[index].tower_name == "support tower" :
                                touer[3] = True

                        if position[0] >= 1150 and position[0] <= 1150 + cancel_img.get_width() and \
                                position[1] >= 615 and position[1] <= 615 + cancel_img.get_height():
                            index -= 1
                            if tower1[i].is_support:
                                support_index.pop()
                            tower1.pop()

            if build == 1:  # made by 김재희~
                position = pygame.mouse.get_pos()
                tower1[index].build_tower(position[0], position[1])

            for i in range(0, len(tower1)):
                attack_on = False
                if len(badguy) > 0:
                    for j in range(0, len(badguy)):
                        if build == 1:
                            if index == i :
                                break
                        if (tower1[i].is_support != True):
                            if (badguy[j].center[0] - tower1[i].x) * (badguy[j].center[0] - tower1[i].x) \
                                    + (badguy[j].center[1] - tower1[i].y) * (badguy[j].center[1] - tower1[i].y) <= tower1[i].range * \
                                    tower1[i].range:
                                attack_on = True
                                if tower1[i].tower_attack(game_timer):
                                    badguy[j].hp -= tower1[i].damage + tower1[i].plus_damage
                                    if badguy[j].hp <= 0:
                                        badguy[j].dead()
                                        badguy.pop(j)
                                        if selectNum == j:
                                            selectNum = -1
                                        elif selectNum > j:
                                            selectNum -= 1
                                        vindex -= 1
                                        break
                                break
                else:
                    if tower1[i].is_support == False:
                        tower1[i].attack = 0
                if tower1[i].is_support == False:
                    if attack_on == False:
                        tower1[i].attack = 0

            if build == 0:
                for i in support_index:
                    exist = False
                    for j in range(0, len(tower1)):
                        if tower1[j].is_support == False:
                            if (tower1[j].x - tower1[i].x) * (tower1[j].x - tower1[i].x) \
                                    + (tower1[j].y - tower1[i].y) * (tower1[j].y - tower1[i].y) <= tower1[i].range * \
                                    tower1[i].range:
                                tower1[j].plus_damage = tower1[i].plus_damage
                                exist = True
                                tower1[i].tower_attack(game_timer)
                    if exist == False:
                        tower1[i].attack = 0  # ~made by 김재희

            for i in range(0, len(tower1)):
                tower1[i].blit_tower(screen)

            for i in range(0, len(enemy1)):
                screen.blit(enemy1[i].enemy_img, (
                enemy1[i].x - enemy1[i].enemy_img.get_width() / 2, enemy1[i].y - enemy1[i].enemy_img.get_height() / 2))

            gold_font = font.render(str(gold), True, (0, 0, 0))
            life_font = font.render(str(life),True,(0,0,0))
            screen.blit(life_font, (1080, 32))
            screen.blit(gold_font, (1195, 32))
            screen.blit(timg[0], (1050, 112))
            screen.blit(timg[1], (1175, 115))
            screen.blit(timg[2], (1052, 238))
            screen.blit(timg[3], (1177, 233))
            screen.blit(cancel_img, (1150, 615))
            game_timer = time.time()

            map1.draw()



            chal = challenge.challenge_1_5_8_9(chal,virus.Virus.AllNum,gold,touer)

            for z in range (0,7,1) :
                if chal_sv[z] ==0 and chal[z] == 1 :
                    chal_sv[z] = 2
                    managetime = time.time()

            for z in range(0, 7, 1):
                if chal_sv[z] != 0 :
                    if curtime - managetime < 3 :
                        scr_giv = font.render("+" + str(chal_scr[z]),True,(0,0,0))
                        screen.blit(scr_giv,(1075,60))
                        mon_giv = font.render("+" + str(chal_money[z]), True, (0, 0, 0))
                        screen.blit(mon_giv, (1190, 60))
                        if chal_sv[z] == 2 :
                            gold += int(chal_money[z])
                            chal_sv[z] =1
                        screen.blit(chal_img[z],(0,0))
                    elif curtime - managetime > 3 :
                        if chal_sv[z] == 2 :
                            chal_sv[z] =1













            if(curtime-oldtime > 2) :
                # 타이머 구현 #copyright 이동우

                if count < 40 :
                    if curtime - vtimer >= 1 :
                        count += 1
                        vtimer = curtime
                        badguy.append(virus.Virus(type_virus))
                        vindex += 1
                        badguy[vindex].setType()
                        badguy[vindex].setPos([780, 720])
                        badguy[vindex].path = [[780, 720], [780, 420], [540, 420], [540, 180], [300, 180], [300, 420],
                                               [120, 420], [120, 60],
                                               [0, 60]]
                type_virus = count//10

                # 문구 출력 #copyright 이동우
                virus.draw_text("remaining virus : ", screen, 110, 20, BLACK)
                virus.draw_text(str(len(badguy)), screen, 210, 20, BLACK)
                #virus.draw_text(str(selectNum), screen, 210, 40, BLACK)
                if life < 0:
                    virus.draw_text("Game over", screen, 640, 300, BLACK)

                #바이러스 좌표 조정 #copyright 이동우
                for n in range(0, len(badguy)):
                    if badguy[n].pos[0] < badguy[n].x_size:  # 바이러스가 맵 끝에 도달하면
                        vindex -= 1
                        life -= badguy[n].dmg
                        badguy.pop(n)
                        if selectNum == n:
                            selectNum = -1
                        elif selectNum > n:
                            selectNum -= 1
                        break
                    else:
                        badguy[n].move()

                # 바이러스 화면 출력 #copyright 이동우
                for n in range(0, len(badguy)):
                    x = badguy[n].pos[0]
                    y = badguy[n].Repeat(badguy[n].pos[1])
                    screen.blit(badguy[n].img, (x, y))

                # 바이러스 클릭 시 바이러스 정보 출력 #copyright 이동우
                if selectNum == -1:
                    pass
                elif selectNum != -1:
                    badguy[selectNum].drawInfo(screen, 1085, 370)



                if(life <=0) :
                    Gameoverbool = True
                    break
                if count >= 40 :
                    if len(badguy) == 0 :
                        break






            pygame.display.flip()
            curtime = time.time()

        if Gameoverbool :
            GameOver.GameOver(screen,95000,life,gold)
            return 1

        chal = challenge.challenge_6(chal,life)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)





