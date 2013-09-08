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
#Инициализация движка
pygame.init()
black=(  0,  0,  0)
red=  (255,  0,  0)
green=(  0,255,  0)
blue= (  0,  0,255)
white=(255,255,255)
screen=pygame.display.set_mode([700, 500])
pygame.display.set_caption("RPG: Role Playing Game")
clock=pygame.time.Clock()
m_pos=pygame.mouse.get_pos()
font=pygame.font.Font(None, 25)
#pic_gpl=pygame.image.load("./res/pic/gpl.png").convert_alpha()
pic_gpl=font.render(u"GPLv3",True,black)
t_loc=font.render(u"Copyright 2013 glade0lus",True,black)
t_loc2=font.render(u"Copyright ",True,black)
t_a1=font.render(u"2013 ",True,black)
t_a2=font.render(u"gl",True,black)
t_a3=font.render(u"ad",True,black)
t_a4=font.render(u"e0",True,black)
t_a5=font.render(u"lu",True,black)
t_a6=font.render(u"s",True,black)
t_m_pos=font.render(u"Mouse pos: "+str(m_pos),True,black)
exit=False
loc1=True
loc2=False
loc3=False
rus=True
eng=True
k1=pygame.K_1
k2=pygame.K_2
k3=pygame.K_3
k4=pygame.K_4
k5=pygame.K_5
k6=pygame.K_6
while exit==False:
    while rus==True and eng==True and exit==False:
        clock.tick(30)
        screen.fill(white)
        screen.blit(t_loc, [350, 250])
        pygame.display.flip()
        rus=False
        eng=False
        t_a1=font.render(u"Choose a language",True,black)
        t_a2=font.render(u"Выберите язык",True,black)
        t_a3=font.render(u"1.English",True,black)
        t_a4=font.render(U"2.Русский - Russian",True,black)
    while rus==False and eng==False and exit==False:
        clock.tick(30)
        t_m_pos=font.render(u"Mouse pos: "+str(m_pos),True,black)
        screen.fill(white)
        screen.blit(t_a1, [0, 0])
        screen.blit(t_a2, [0, 20])
        screen.blit(t_a3, [0, 40])
        screen.blit(t_a4, [0, 60])
        screen.blit(t_m_pos, [0, 300])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
                eng=True
            key=pygame.key.get_pressed()
            if key[k1]:
                eng=True
                t_loc=font.render(u"Prison",True,black)
                t_loc2=font.render(u"You are in prison",True,black)
            if key[k2]:
                rus=True
                t_loc=font.render(u"Тюрьма",True,black)
                t_loc2=font.render(u"Вы находитесь в тюрьме",True,black)
    while rus==True or eng==True and exit==False:
        clock.tick(30)
        screen.fill(white)
        screen.blit(t_loc, [0, 0])
        screen.blit(t_loc2, [0, 20])
        
# while exit==False:
#     while loc1==True and exit==False:
#         clock.tick(30)
#         m_pos=pygame.mouse.get_pos()
#         t_m_pos=font.render(u"Mouse pos: "+str(m_pos),True,black)
#         screen.fill(white)
#         screen.blit(t_loc1, [0, 0])
#         screen.blit(t_loc1_a1, [0, 20])
#         screen.blit(t_loc1_a2, [0, 40])
#         screen.blit(pic_gpl, [570, 450])
#         screen.blit(t_m_pos, [0, 480])
#         pygame.display.flip()
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 exit=True
#             key=pygame.key.get_pressed()
#             if key[k1]:
#                 loc1=False
#                 loc2=True
#             if key[k2]:
#                 loc1=False
#                 loc3=True
pygame.quit()
