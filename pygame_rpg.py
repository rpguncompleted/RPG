#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Copyright 2013 glade0lus
'''
'''
This file is part of "RPG is a Python Game" (or simply the RPG).

    RPG is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    RPG is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with RPG:Role Playing Game.  If not, see <http://www.gnu.org/licenses/>.

  (Этот файл — часть "RPG is a Python Game" (или просто RPG).

   RPG - свободная программа: вы можете перераспространять ее и/или
   изменять ее на условиях Стандартной общественной лицензии GNU в том виде,
   в каком она была опубликована Фондом свободного программного обеспечения;
   либо версии 3 лицензии, либо (по вашему выбору) любой более поздней
   версии.

   RPG распространяется в надежде, что она будет полезной,
   но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии ТОВАРНОГО ВИДА
   или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной
   общественной лицензии GNU.

   Вы должны были получить копию Стандартной общественной лицензии GNU
   вместе с этой программой. Если это не так, см.
   <http://www.gnu.org/licenses/>.)
'''
import pygame
pygame.init()
black=(  0,  0,  0) #Colors
red=  (255,  0,  0)
green=(  0,255,  0)
blue= (  0,  0,255)
white=(255,255,255)
screen=pygame.display.set_mode([800, 600])
pygame.display.set_caption("RPG: Role Playing Game")
clock=pygame.time.Clock()
m_pos=pygame.mouse.get_pos()
font=pygame.font.Font(None, 25)
#pic_gpl=pygame.image.load("./res/pic/gpl.png").convert_alpha()
pic_gpl=font.render(u"GPLv3",True,black)
t_d=font.render(u"",True,black) #Description
t_d2=font.render(u"",True,black) #Description 2
t_a1=font.render(u"",True,black) #Action 1-6
t_a2=font.render(u"",True,black)
t_a3=font.render(u"",True,black)
t_a4=font.render(u"",True,black)
t_a5=font.render(u"",True,black)
t_a6=font.render(u"",True,black)
t_m_pos=font.render(u"Mouse pos: "+str(m_pos),True,black) #Mouse position
exit=False #While True, exit cycle
rus=False
eng=False
t_a1=font.render(u"Choose a language",True,black)
t_a2=font.render(u"Выберите язык",True,black)
t_a3=font.render(u"1.English",True,black)
t_a4=font.render(U"2.Русский - Russian",True,black)
k1=pygame.K_1 #Keys 1-6
k2=pygame.K_2
k3=pygame.K_3
k4=pygame.K_4
k5=pygame.K_5
k6=pygame.K_6
while exit==False:
    while rus==False and eng==False and exit==False:
        clock.tick(30)
        screen.fill(white)
        screen.blit(t_a1, [0, 0])
        screen.blit(t_a2, [0, 20])
        screen.blit(t_a3, [0, 40])
        screen.blit(t_a4, [0, 60])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                eng=True
            key=pygame.key.get_pressed()
            if key[k1]:
                eng=True
                t_d=font.render(u"Prison",True,black)
                t_d2=font.render(u"You are in prison",True,black)
                t_a1=font.render(u"1.Shout",True,black)
                t_a2=font.render(u"2.Look around",True,black)
                t_a3=font.render(u"3.Wait",True,black)
                t_a4=font.render(u"4.Open door with key",True,black)
            if key[k2]:
                rus=True
                t_d=font.render(u"Тюрьма",True,black)
                t_d2=font.render(u"Вы находитесь в тюрьме",True,black)
                t_a1=font.render(u"1.Кричать",True,black)
                t_a2=font.render(u"2.Осмотреться",True,black)
                t_a3=font.render(u"3.Ждать",True,black)
                t_a4=font.render(u"4.Открыть дверь ключом",True,black)
    while rus==True or eng==True and exit==False:
        clock.tick(30)
        screen.fill(white)
        screen.blit(t_d , [0,  0])
        screen.blit(t_d2, [0, 20])
        screen.blit(t_a1, [0, 40])
        screen.blit(t_a2, [0, 60])
        screen.blit(t_a3, [0, 80])
        screen.blit(t_a4, [0,100])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            key=pygame.key.get_pressed()
            if key[k1]:
                if eng==True:
                    t_d=font.render(u"You shouted for a long time, but on your shouts no one responded.",True,black)
                    t_a1=font.render(u"1.Back",True,black)
                if rus==True:
                    t_d=font.render(u"Вы кричали очень долго, но на ваши крики никто не откликнулся.",True,black)
                    t_a1=font.render(u"1.Назад",True,black)
                exitLoc=False
                while exitLoc==False and exit==False:
                    clock.tick(30)
                    screen.fill(white)
                    screen.blit(t_d, [0,  0])
                    screen.blit(t_a1, [0,  20])
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            exit==True
                        key=pygame.key.get_pressed()
                        if key[k1]:
                            if eng==True:
                                t_d=font.render(u"Prison",True,black)
                                t_d2=font.render(u"You are in prison",True,black)
                                t_a1=font.render(u"1.Shout",True,black)
                                t_a2=font.render(u"2.Look around",True,black)
                                t_a3=font.render(u"3.Wait",True,black)
                                t_a4=font.render(u"4.Open door with key",True,black)
                            if rus==True:
                                t_d=font.render(u"Тюрьма",True,black)
                                t_d2=font.render(u"Вы находитесь в тюрьме",True,black)
                                t_a1=font.render(u"1.Кричать",True,black)
                                t_a2=font.render(u"2.Осмотреться",True,black)
                                t_a3=font.render(u"3.Ждать",True,black)
                                t_a4=font.render(u"4.Открыть дверь ключом",True,black)
                            exitLoc=True
pygame.quit()
